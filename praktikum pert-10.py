# Program Input Nilai Menggunakan Dictionary

data = {}

def hitung_akhir(tugas, uts, uas):
    return (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)


def tampilkan_data():
    print("="*60)
    print("| NO |  NIM   |  NAMA  | TUGAS | UTS | UAS | AKHIR |")
    print("="*60)

    if not data:
        print("|                    TIDAK ADA DATA                 |")
        print("="*60)
        return

    for i, (nim, mhs) in enumerate(data.items(), start=1):
        print(f"| {i:<2} | {nim:<6} | {mhs['nama']:<6} |"
              f" {mhs['tugas']:<5} | {mhs['uts']:<3} | {mhs['uas']:<3} | {mhs['akhir']:<5.2f} |")
    print("="*60)


def tambah_data():
    print("Tambah Data")
    nim = input("NIM        : ")
    nama = input("Nama       : ")
    uts = int(input("Nilai UTS  : "))
    uas = int(input("Nilai UAS  : "))
    tugas = int(input("Nilai Tugas: "))

    akhir = hitung_akhir(tugas, uts, uas)

    data[nim] = {"nama": nama, "uts": uts, "uas": uas, "tugas": tugas, "akhir": akhir}
    print(">>> Data berhasil ditambah.\n")


def ubah_data():
    nim = input("Masukkan NIM yang akan diubah: ")
    if nim in data:
        print("Ubah Data")
        nama = input("Nama baru       : ")
        uts = int(input("Nilai UTS baru  : "))
        uas = int(input("Nilai UAS baru  : "))
        tugas = int(input("Nilai Tugas baru: "))

        akhir = hitung_akhir(tugas, uts, uas)

        data[nim] = {"nama": nama, "uts": uts, "uas": uas, "tugas": tugas, "akhir": akhir}
        print(">>> Data berhasil diubah.\n")
    else:
        print(">>> Data tidak ditemukan.\n")


def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in data:
        del data[nim]
        print(">>> Data berhasil dihapus.\n")
    else:
        print(">>> Data tidak ditemukan.\n")


def cari_data():
    nim = input("Masukkan NIM yang dicari: ")
    if nim in data:
        print("Data Ditemukan:")
        mhs = data[nim]
        print(f"NIM   : {nim}")
        print(f"Nama  : {mhs['nama']}")
        print(f"Tugas : {mhs['tugas']}")
        print(f"UTS   : {mhs['uts']}")
        print(f"UAS   : {mhs['uas']}")
        print(f"Akhir : {mhs['akhir']:.2f}\n")
    else:
        print(">>> Data tidak ditemukan.\n")


# Menu utama
while True:
    print("Program Input Nilai")
    print("===================")
    print("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar]")
    pilih = input("Pilih menu: ").lower()

    if pilih == "l":
        tampilkan_data()
    elif pilih == "t":
        tambah_data()
    elif pilih == "u":
        ubah_data()
    elif pilih == "h":
        hapus_data()
    elif pilih == "c":
        cari_data()
    elif pilih == "k":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.\n")