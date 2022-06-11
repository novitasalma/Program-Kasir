from operator import index
from tabulate import tabulate
import pandas as pd

#panggil excel
df = pd.read_excel('Data Barang.xlsx')
df_baru = df.dropna()
print(df_baru.to_string(index=0))

nama_kasir = str(input("Masukkan nama kasir : "))

def Cekdaftar():
    nomor = int(input(("Masukkan kode barang ")))
    cek = nomor in df.Kode.unique()
    if cek == True:
        return nomor
    else:
        return False

def data(kuantitas, nomor):
    kode = (nomor) - 111
    data_harga = df_baru.iloc[kode, 2]
    data_barang = df_baru.iloc[kode, 1]
    kalkulasi = data_harga * (kuantitas)
    print("{} | {} | {} | {}". format(data_barang,kuantitas,data_harga, kalkulasi))

def data_total(kuantitas, nomor):
    kode = (nomor) - 111
    data_harga = df_baru.iloc[kode, 2]
    data_barang = df_baru.iloc[kode, 1]
    kalkulasi = data_harga * (kuantitas)
    return data_barang, kuantitas, data_harga, kalkulasi

#membuat dictionary supaya pandas bisa membaca perubahan yg terjadi
def csv_baru(kuantitas, nomor):
    kode = (nomor) - 111
    data_harga = df_baru.iloc[kode, 2]
    data_barang = df_baru.iloc[kode, 1]
    kalkulasi = data_harga * (kuantitas)
    history = {"Nama Barang" : [data_barang], "Harga Barang" : [data_harga], "Kuantitas" : [kuantitas],
    'Jumlah' : [kalkulasi]}
    return history

def total(kuantitas, nomor):
    kode = nomor - 111
    data_harga = df_baru.iloc[kode, 2]
    kalkulasi = data_harga * kuantitas
    return kalkulasi

def diskon(total, diskon, voucher):
    if voucher == 1:
        TOTAL = total - total*diskon 
        TOTAL = round(TOTAL)
    elif voucher == 2:
        TOTAL = total - total*diskon - 25000
        TOTAL = round(TOTAL)
    else:
        print("MASUKKAN PILIHAN YANG VALID")
    print("TOTAL                               | {}".format(total))
    print("TOTAL KESELURUHAN                   | {}".format(TOTAL + TOTAL*0.11))

def kembalian(total, diskon, voucher, nominal):
    if voucher == 1:
        TOTAL = total - total*diskon 
        TOTAL = round(TOTAL)
    elif voucher == 2:
        TOTAL = total - total*diskon - 25000
        TOTAL = round(TOTAL)
    else:
        print("MASUKKAN PILIHAN YANG VALID")
    return nominal - TOTAL 

total_1 = 0
list_baru = []
csv_2 = pd.read_csv('Output.csv')
csv_dummy = {"Nama Barang" : ['-'], "Harga Barang" : ["-"], "Kuantitas" : ["-"],
    'Jumlah' : ["-"]}
csv_dummy = pd.DataFrame(csv_dummy)
csv_2 = csv_2.append(csv_dummy)

while True:
    cek = input("Apakah anda mau menginput harga barang YA/TIDAK ? ")
    if cek.lower() == "ya":
        while True:
            nomor = Cekdaftar()
            if nomor == False:
                print("Masukkan kode valid")
            else:
                nomor = int(nomor)
                break
            
        kuantitas = int(input("Masukkan kuantitas "))
        data(kuantitas, nomor)
        csv_1 = csv_baru(kuantitas, nomor)
        csv_1 = pd.DataFrame(csv_1)        
        csv_2 = csv_2.append(csv_1)
        csv_2.to_csv("Output.csv", index=0)
        total_1 = total_1 + total(kuantitas, nomor)
        list_baru.append(data_total(kuantitas, nomor))

    elif cek.lower() == "tidak":
        member = input("Apakah anda member YA/TIDAK? ")
        print("1. Tanpa Voucher")
        print("2. Voucher 25K")
        voucher = int(input("Masukkan Pilihan Voucher Anda "))

        print("")
        print("=============================================================")
        print("KADITA MART".center(55))
        print("Jl. Kelebet Meteor No.1 JEBRES SURAKARTA".center(55))
        print("============================================================")
        print("Nama kasir \t : " , nama_kasir)
        print("")
        print(tabulate(list_baru, headers=["Barang", "Kuantitas", "Harga", "Jumlah              "]))
        print("============================================================")
        
        if member.lower() == "ya":
            if total_1 >= 50000:
                diskon(total_1, 0.05, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0.05, voucher, nominal)
            
            elif total_1 >= 500000:
                diskon(total_1, 0.1, voucher)
                nominal = int(input("Masukkan? "))
                total_harga = kembalian(total_1, 0.1, voucher, nominal)
                nominal = int(input("Uang Anda = "))
                print("Kembalian Anda =", total_harga)
                
            elif total_1 >= 1000000:
                diskon(total_1, 0.15, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0.15, voucher, nominal)
            
            elif total_1 >= 2000000:
                diskon(total_1, 0.15, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0.15, voucher, nominal)
                
            else:
                diskon(total_1, 0, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0, voucher, nominal)   
            
            
        elif member.lower() == "tidak":
            if total_1 >= 1000000:
                diskon(total_1, 0.05, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0.05, voucher, nominal)

            if total_1 >= 2000000:
                diskon(total_1, 0.05, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0.05, voucher, nominal)

            else:
                diskon(total_1, 0, voucher)
                nominal = int(input("Uang Anda = "))
                total_harga = kembalian(total_1, 0, voucher, nominal)
            
          
        else:
            print("MASUKKAN YA ATAU TIDAK")
        print("Kembalian Anda =", total_harga)
        break
        
    else:
        print("MASUKKAN YA ATAU TIDAK")

print("=============================================================")
print("T E R I M A  K A S I H".center(55))
print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
    