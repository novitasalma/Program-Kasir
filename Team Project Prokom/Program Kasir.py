from operator import index
from tkinter.tix import Tree
from tabulate import tabulate
import pandas as pd

#panggil excel
df = pd.read_excel('Data Barang.xlsx')
df2 = pd.read_excel('Data Pengguna.xlsx')
df_baru = df.dropna()
print(df_baru.to_string(index=0))



def CekPengguna():
    while True:
        try:
            nama = input("Masukkan Username : ")
            password = input('Masukkan Password : ')
            ceknama = nama in df2.Username.unique()
            cekpassword =  password in df2.Password.unique()
            if ceknama == False or cekpassword == False:
                raise ValueError
            print('Data karyawan dikenali, silahkan lanjut')
            print('=======================================')
            return nama
        except ValueError:
            print("NAMA ATAU PASSWORD SALAH, SILAHKAN COBA LAGI")
    
def Cekdaftar_1():
    while True :        
        try:
            num = int(input("Masukkan Kode Barang "))
            cek = num in df.Kode.unique()
            if num < 111 or cek == False:
                raise ValueError
            return num  # Replacing break with return statement 
        except ValueError:
            print("Tolong masukkan opsi yang valid") 

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
        TOTAL = TOTAL + TOTAL*0.11
    elif voucher == 2:
        TOTAL = total - total*diskon - 25000
        TOTAL = TOTAL + TOTAL*0.11
    else:
        print("MASUKKAN PILIHAN YANG VALID")
    return nominal - TOTAL 

def input_voucher():
    while True :        
        try:
            num = int(input("Masukkan Pilihan Voucher Anda "))
            if num < 1 or num > 2:
                raise ValueError
            return num  # Replacing break with return statement 
        except ValueError:
            print("Tolong masukkan opsi yang valid") 

def input_member():
    while True:
        member = input("Apakah anda member YA/TIDAK? ")
        if member.lower() == 'ya':
            return member
            break
        elif member.lower() == 'tidak':
            return member
            break
        else: 
            print('PILIH YA ATAU TIDAK')
        
def input_kuantitas():
    while True :        
        try:
            num = int(input("Masukkan Kuantitas "))
            if num < 0:
                raise ValueError
            return num  # Replacing break with return statement 
        except ValueError:
            print("Tolong masukkan opsi yang valid") 


nama_kasir = CekPengguna()

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
            nomor = Cekdaftar_1()
            
            if nomor == False:
                print("Masukkan kode valid")
            else:
                nomor = int(nomor)
                break
            
        kuantitas = input_kuantitas()
        data(kuantitas, nomor)
        csv_1 = csv_baru(kuantitas, nomor)
        csv_1 = pd.DataFrame(csv_1)        
        csv_2 = csv_2.append(csv_1)
        csv_2.to_csv("Output.csv", index=0)
        total_1 = total_1 + total(kuantitas, nomor)
        list_baru.append(data_total(kuantitas, nomor))

    elif cek.lower() == "tidak":
        member = input_member()

        if member.lower() == "ya":
            print("1. Tanpa Voucher")
            print("2. Voucher 25K")
            voucher = input_voucher()
            print("")
            print("=============================================================")
            print("KADITA MART".center(55))
            print("Jl. Kelebet Meteor No.1 JEBRES SURAKARTA".center(55))
            print("============================================================")
            print("Nama kasir \t : " , nama_kasir)
            print("")
            print(tabulate(list_baru, headers=["Barang", "Kuantitas", "Harga", "Jumlah              "]))
            print("============================================================")
            if total_1 >= 50000 and total_1 < 500000:
                diskon(total_1, 0.05, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0.05, voucher, nominal)
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print()  
           
            elif total_1 >= 500000 and total_1 < 1000000:
                diskon(total_1, 0.1, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0.1, voucher, nominal)
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print()  
  
                
            elif total_1 >= 1000000 and total_1 < 2000000:
                diskon(total_1, 0.15, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0.15, voucher, nominal)     
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print()


            elif total_1 >= 2000000:
                diskon(total_1, 0.15, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0.15, voucher, nominal)                
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print("DAPAT VOUCHER".center(55))
                
            else:
                diskon(total_1, 0, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0, voucher, nominal)               
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print()

            break 
            
            
        elif member.lower() == "tidak":
            print("1. Tanpa Voucher")
            print("2. Voucher 25K")
            voucher = input_voucher()
            print("")
            print("=============================================================")
            print("KADITA MART".center(55))
            print("Jl. Kelebet Meteor No.1 JEBRES SURAKARTA".center(55))
            print("============================================================")
            print("Nama kasir \t : " , nama_kasir)
            print("")
            print(tabulate(list_baru, headers=["Barang", "Kuantitas", "Harga", "Jumlah              "]))
            print("============================================================")
            if total_1 >= 1000000 and total_1 < 2000000:
                diskon(total_1, 0.05, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0.05, voucher, nominal)
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print()    

            elif total_1 >= 2000000:
                diskon(total_1, 0.05, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0.05, voucher, nominal)
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print("DAPAT VOUCHER".center(55))   

            else:
                diskon(total_1, 0, voucher)
                nominal = int(input("TOTAL TUNAI                         | "))
                total_harga = kembalian(total_1, 0, voucher, nominal)   
                print("KEMBALIAN                           | {}".format(total_harga))
                print("=============================================================")
                print("T E R I M A  K A S I H".center(55))
                print("Barang yang sudah dibeli tidak dapat dikembalikan".center(55))
                print()  
            break
                  
        else:
            print("MASUKKAN YA ATAU TIDAK")
        
        
        
    else:
        print("MASUKKAN YA ATAU TIDAK")