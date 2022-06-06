from re import A
from tabulate import tabulate
import pandas as pd

#panggil excel
df = pd.read_excel('Data Barang.xlsx')
df_baru = df.dropna()

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
        TOTAL = total - total*diskon - 15000
        TOTAL = round(TOTAL)
    elif voucher == 3:
        TOTAL = total - total*diskon - 25000
        TOTAL = round(TOTAL)
    else:
        print("MASUKKAN PILIHAN YANG VALID")
    print("TOTAL                               | {}".format(total))
    print("TOTAL KESELURUHAN                   | {}".format(TOTAL + TOTAL*0.11))

total_1 = 0
list_baru = []
while True:
    cek = input("Apakah anda mau menginput harga barang Y/T ? ")
    if cek.lower() == "y":
        nomor = int(input(("Masukkan kode barang ")))
        kuantitas = int(input("Masukkan kuantitas "))
        data(kuantitas, nomor)
        total_1 = total_1 + total(kuantitas, nomor)
        list_baru.append(data_total(kuantitas, nomor))

    elif cek.lower() == "t":
        member = input("Apakah anda member YA/TIDAK? ")
        print("1. Tanpa Voucher")
        print("2. Voucher 15K")
        print("3. Voucher 25K")
        voucher = int(input("Masukkan Pilihan Voucher Anda "))
        print(tabulate(list_baru, headers=["Barang", "Kuantitas", "Harga", "Jumlah              "]))
        print("===========================================")
        if member.lower() == "ya":
            if total_1 >= 50000:
                diskon(total_1, 0.05, voucher)
                break
            elif total_1 >= 500000:
                diskon(total_1, 0.1, voucher)
                break
            elif total_1 >= 1000000:
                diskon(total_1, 0.15, voucher)
                break
            else:
                diskon(total_1, 0, voucher)
                break
        elif member.lower() == "tidak":
            if total_1 >= 1000000:
                diskon(total_1, 0.05, voucher)
                break
            else:
                diskon(total_1, 0, voucher)
                break
        else:
            print("MASUKKAN YA ATAU TIDAK")


    else:
        print("MASUKKAN YA ATAU TIDAK")
