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

def diskon(total, diskon):
    TOTAL = total - total*diskon
    TOTAL = round(TOTAL)
    print("TOTAL                       | {}".format(total))
    print("TOTAL SETELAH DISKON        | {}".format(TOTAL))

total_1 = 0
list_baru = []
while True:
    cek = input("Apakah anda mau menginput harga barang YA/TIDAK ? ")
    if cek.lower() == "ya":
        nomor = int(input(("Masukkan kode barang ")))
        kuantitas = int(input("Masukkan kuantitas "))
        data(kuantitas, nomor)
        total_1 = total_1 + total(kuantitas, nomor)
        list_baru.append(data_total(kuantitas, nomor))

    elif cek.lower() == "tidak":
        member = input("Apakah anda member YA/TIDAK? ")
        print(tabulate(list_baru, headers=["Barang", "Kuantitas", "Harga", "Jumlah"]))
        print("=====================================")
        if member.lower() == "ya":
            if total_1 >= 50000:
                diskon(total_1, 0.05)
                break
            elif total_1 >= 500000:
                diskon(total_1, 0.1)
                break
            elif total_1 >= 1000000:
                diskon(total_1, 0.15)
                break
            else:
                diskon(total_1, 0)
                break
        elif member.lower() == "tidak":
            if total_1 >= 1000000:
                diskon(total_1, 0.05)
                break
            else:
                diskon(total_1, 0)
                break
        else:
            print("MASUKKAN YA ATAU TIDAK")


    else:
        print("MASUKKAN YA ATAU TIDAK")
