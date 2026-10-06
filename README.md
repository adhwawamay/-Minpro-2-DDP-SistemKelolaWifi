# -Minpro-2-DDP-SistemKelolaWifi
Nama : Adhwa Maysura
Nim : 2609116103
Kelas C

## Penjelasan Sistem Kelola Jaringan Wifi
<img width="792" height="295" alt="mp 2 1" src="https://github.com/user-attachments/assets/569b7f27-6495-481a-9444-863cf93a0983" />

1. Melakukan import libary
- os → digunakan untuk membersihkan layar.
- datetime → mengambil tanggal dan waktu saat data diubah.
- pwinput → membuat password tidak terlihat saat diketik.
- PrettyTable → membuat tampilan data berbentuk tabel.
2. Membuat ketentuan dengan konstanta
- Login maksimal 3 kali.
- Password WiFi minimal 8 karakter.
3. Menyimpan username, password & role pengguna

<img width="1557" height="667" alt="mp  2" src="https://github.com/user-attachments/assets/e090ddfa-268b-46f2-ac3a-7d623df7c8ef" />

1. Menyimpan data jaringan WiFi berupa :
- ID
- Nama WiFi
- Lokasi
- Password
- Waktu terakhir diperbarui

<img width="1579" height="647" alt="mp 2 3" src="https://github.com/user-attachments/assets/9a59e06d-665b-43ec-885f-f3d6b1fee45f" />
Berikut adalah sebuah fuction

1. **def waktu_sekarang():** = Mengambil waktu saat ini untuk mencatat kapan data WiFi terakhir diubah.
2. **def bersihkan_layar():** = Membersihkan tampilan terminal agar menu terlihat lebih rapi.
3. **def jeda():** = Program berhenti sementara sampai pengguna menekan ENTER.
4. **def input_teks(...):** = Memastikan input teks tidak kosong, kecuali memang diperbolehkan kosong.

<img width="1564" height="817" alt="Screenshot (86)" src="https://github.com/user-attachments/assets/83968357-1e4d-4b27-adad-a68117e091bb" />

1. **def input_password_wifi(...):** Mevalidasi password WiFi
- Tidak kosong.
- Minimal 8 karakter.
- Tidak mengandung spasi.

2. **def input_menu(...):** Memvalidasi pilihan menu
Memastikan pengguna memasukkan angka sesuai batas menu, jika memasukkan huruf atau angka di luar pilihan, program meminta input kembali.

<img width="1428" height="935" alt="Screenshot (87)" src="https://github.com/user-attachments/assets/e4162e2d-f8c3-4d25-be47-49952f38ca5e" />

1. **def nama_sudah_ada(...):** Mengecek nama WiFi udah digunakan oleh jaringan lain agar tidak terjadi nama yang sama.
2. **def buat_id_baru(...):** Mencari ID terbesar yang ada, kemudian membuat ID berikutnya secara otomatis.
Contoh:
WT001, WT002, WT003, WT004.

<img width="785" height="250" alt="2026-10-07 (1)" src="https://github.com/user-attachments/assets/08586414-0160-4bf4-bf7d-98a21924ab21" /> 

1. **def pilih_id_wifi(...):** Menampilkan daftar WiFi kemudian meminta pengguna memilih ID.
0 digunakan untuk membatalkan.

<img width="788" height="314" alt="2026-10-07 (2)" src="https://github.com/user-attachments/assets/33412214-064e-4511-a430-67549f5b7c03" /> 

1. **def buat_tabel(...):** Mengubah data WiFi menjadi tabel agar lebih mudah dibaca.

<img width="1411" height="903" alt="Screenshot (90)" src="https://github.com/user-attachments/assets/fed23070-ae9b-4713-8a39-f3d6a2e78c19" />

1. **def buat_tabel(...):** Mengubah data WiFi menjadi tabel agar lebih mudah dibaca.
2. **def tampilkan_ringkas(...):** Menampilkan data WiFi secara singkat tanpa password dan waktu pembaruan.
3. **def tampilkan_wifi(...):** Menampilkan semua data WiFi secara lengkap. Namun jika data tidak ada, program memberikan pesan bahwa data masih kosong.

<img width="1415" height="447" alt="Screenshot (91)" src="https://github.com/user-attachments/assets/9683ee54-d899-4f80-81b4-f4f92fd20d56" /> 

1. **def tambah_wifi(...):** Yang nantinya program akan mengecek Meminta nama WiFi, mengecek nama yang sama, meminta lokasi,
meminta password, membuat ID otomatis, menyimpan data baru.

<img width="1585" height="383" alt="Screenshot (93)" src="https://github.com/user-attachments/assets/9d3ccde7-5251-4349-abf2-3ab017573ab6" />

1. **def ubah_wifi(...):** Untuk memilih ID wiFi menampilkan data saat ini, meminta data baru, data yang dikosongkan tidak akan diubah, waktu pembaruan diperbarui.

<img width="1568" height="453" alt="Screenshot (95)" src="https://github.com/user-attachments/assets/fbb370ab-4729-4e8c-a925-4e6bd1b2634d" /> 

1. **def hapus_wifi(...):** Menghapus jaringan WiFi dengan alur Alur memilih ID WiFi, menampilkan nama WiFi, meminta konfirmasi, jika memilih opsi y(yes) data dihapus, jika n(no) penghapusan dibatalkan.

<img width="1451" height="339" alt="Screenshot (96)" src="https://github.com/user-attachments/assets/25693e84-6ec5-4edb-8a9f-6400e2be3515" /> 

1. **def cari_wifi(...):** Pengguna memasukkan kata kunci berupa nama atau lokasi. Program kemudian akan otomatis menampilkan permintaan pengguna berserta tabel



















  


