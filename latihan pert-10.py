print("Nama  : Rifki Ade Tia")
print("Nim   : 312510334")
print("Kelas : TI.25.C5")
print()
# latihan1_kontak.py
# Menyiapkan dictionary sesuai soal dan menjalankan operasi yang diminta

def latihan1():
    # buat dictionary awal
    contacts = {
        "Ari": "081267888",
        "Dina": "087677776"
    }

    print("Kontak awal:", contacts)
    print()

    # Tampilkan kontak Ari
    print("Nomor Ari:", contacts.get("Ari"))
    print()

    # Tambah kontak Riko
    contacts["Riko"] = "087654544"
    print("Setelah tambah Riko:", contacts)
    print()

    # Ubah kontak Dina
    contacts["Dina"] = "088999776"
    print("Setelah ubah nomor Dina:", contacts)
    print()

    # Tampilkan semua Nama
    print("Semua nama:", list(contacts.keys()))
    # Tampilkan semua Nomor
    print("Semua nomor:", list(contacts.values()))
    print()

    # Tampilkan daftar Nama dan nomornya (iterasi)
    print("Daftar nama dan nomor:")
    for name, number in contacts.items():
        print(f" - {name}: {number}")
    print()

    # Hapus kontak Dina
    if "Dina" in contacts:
        del contacts["Dina"]
        print("Setelah hapus Dina:", contacts)
    else:
        print("Dina tidak ditemukan untuk dihapus.")

if __name__ == "__main__":
    latihan1()