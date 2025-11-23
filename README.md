# Praktikum-Pertemuan-Ke-10
Tugas ini dibuat guna memenuhi tugas mata kuliah matematika pengantar pemrograman
# Nama : Rifki Ade Tia
# Nim : 312510334
# Kelas : TI.25.C5
Deskripsi Program untuk mengelola data nilai mahasiswa menggunakan Dictionary Python. Program dapat menambah, mengubah, menghapus, menampilkan, dan mencari data mahasiswa.

START: Inisialisasi Dictionary kosong data_mahasiswa.
Loop Utama (Menu): Tampilkan Menu Pilihan (Tambah, Ubah, Hapus, Tampil, Cari, Keluar).
Input Pilihan: Minta input pilihan dari pengguna.
Percabangan (Switch/If-Else):
Pilihan 1 (Tambah): Ambil input data. Cek NIM duplikat. Jika valid, hitung NA, simpan ke Dictionary.
Pilihan 2 (Ubah): Ambil NIM yang diubah. Cek keberadaan NIM. Jika ada, minta pilihan komponen (Nama/Tugas/UTS/UAS) yang diubah. Jika nilai diubah, hitung ulang NA.
Pilihan 3 (Hapus): Ambil NIM. Cek keberadaan NIM. Jika ada, hapus entri dari Dictionary (del data_mahasiswa[nim]).
Pilihan 4 (Tampilkan): Loop melalui semua item di Dictionary dan tampilkan dalam format tabel.
Pilihan 5 (Cari): Ambil keyword. Loop melalui Dictionary, periksa apakah keyword cocok dengan NIM atau Nama. Tampilkan yang cocok.
Pilihan 6 (Keluar): Keluar dari loop dan menuju END.
Lainnya: Tampilkan pesan error dan kembali ke Menu.
END: Program selesai.
