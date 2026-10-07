# -Minpro-2-DDP-SistemKelolaJaringanWifi
Nama : Adhwa Maysura<br>
Nim : 2609116103<br>
Kelas C

## Penjelasan Sistem Kelola Jaringan Wifi
<img width="792" height="295" alt="mp 2 1" src="https://github.com/user-attachments/assets/569b7f27-6495-481a-9444-863cf93a0983" />
<img width="1579" height="389" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/00aa72ce-225f-4cb5-92bc-3b7dbed05f78" />

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

<img width="1579" height="389" alt="Screenshot (97)" src="https://github.com/user-attachments/assets/ec934fe7-b548-4689-84f1-7a39fe9e0cff" />

1. **def login():** Yang nantinya akan diarahkan untuk memasukan username, dilanjutkan dengan password, lalu sistem akan otomatis mengecek akun, jika benar login dinyatakan berhasil jika salah login dinyatakan gagal. Jika gagal hingga 3x kesempatan untuk login habis setelah itu program akan dihentikan

<img width="1576" height="642" alt="Screenshot (98)" src="https://github.com/user-attachments/assets/cd0b2e19-1109-4384-b90a-1f7a24cd9d5b" /> 

1. **def menu_admin(...):** Login menu admin akan diarahkn ke 6 menu yaitu
- Tambah WiFi
- Tampilkan WiFi
- Ubah WiFi
- Hapus WiFi
- Cari WiFi
- Logout

<img width="784" height="265" alt="2026-10-07 (4)" src="https://github.com/user-attachments/assets/b1845933-5386-47c8-9074-15068d6c8e7a" />

1. **def menu_user(...):** untuk user hanya memiliki 3 pilihan:
- Tampilkan WiFi
- Cari WiFi
- Logout
User hanya dapat melihat dan mencari data

<img width="1593" height="727" alt="Screenshot (100)" src="https://github.com/user-attachments/assets/a81438d0-0400-44a7-a51c-88d749429ec4" /> 

<img width="1573" height="214" alt="Screenshot (101)" src="https://github.com/user-attachments/assets/da18a09f-07be-484d-b5c4-4a6fbda42e41" />


1. **def main():** fungsi utama untuk menjalankan semua program seperti
- Menampilkan login.
- Mengecek role pengguna.
- Mengarahkan ke menu admin atau user.
Setelah logout, pengguna ditanya apakah ingin login dengan akun lain.
Jika tidak, program berhenti.

2. **if __name__ == "__main__":** Bagian ini memastikan fungsi main() dijalankan ketika sistem Python dijalankan secara langsung.

3. **except KeyboardInterrupt:** Penanganan KeyboardInterrupt. Jika pengguna menghentikan program secara manual, misalnya dengan Ctrl + C, program menampilkan pesan bahwa program dihentikan oleh pengguna


## Hasil Run
### Hasil Run (User)

<img width="1596" height="287" alt="Screenshot (103)" src="https://github.com/user-attachments/assets/3d12e21e-1f4e-43e1-a3a2-7fa595fc1875" />

<img width="803" height="324" alt="2026-10-07 (5)" src="https://github.com/user-attachments/assets/586c0381-e473-4bf5-827f-68fbb6f0503d" />

<img width="1606" height="595" alt="Screenshot (107)" src="https://github.com/user-attachments/assets/2ddec44d-dff9-4f06-a1ed-378427826a12" />

<img width="1598" height="417" alt="Screenshot (109)" src="https://github.com/user-attachments/assets/554e9989-9d73-4aeb-b0b8-8a025e67acac" />

### Hasil Run (Admin)
<img width="1597" height="361" alt="Screenshot (110)" src="https://github.com/user-attachments/assets/6a7fc004-ddf4-4372-a7b1-d7bf003cc622" />

<img width="1606" height="611" alt="Screenshot (113)" src="https://github.com/user-attachments/assets/802caeb7-a214-49c7-9033-20afa9e48ada" />

<img width="1577" height="950" alt="Screenshot (115)" src="https://github.com/user-attachments/assets/af25fb92-1a07-4908-acd6-d209bda63b49" />

<img width="1598" height="875" alt="Screenshot (116)" src="https://github.com/user-attachments/assets/768c9da2-5191-4a2f-8a59-ceae78b6e86d" />

<img width="1593" height="682" alt="Screenshot (118)" src="https://github.com/user-attachments/assets/a7dbeeb0-37ff-405d-b762-edee763d15e4" />

<img width="1589" height="692" alt="Screenshot (119)" src="https://github.com/user-attachments/assets/7bbd4678-fd1c-41b5-aed0-369510c6e99a" />

<img width="1920" height="1080" alt="Screenshot (117)" src="https://github.com/user-attachments/assets/ac66ac50-6de8-4f0f-81a6-b60352a88aa4" />

## Flowchart

<img width="3704" height="2398" alt="mini projek 2 drawio" src="https://github.com/user-attachments/assets/b3bcb021-2429-473f-8e56-b9f58aa2dbb8" />

1. Start
   - Sistem dijalankan dan menampilkan header “SISTEM DATA JARINGAN WIFI”.
   - Percobaan login dimulai dari angka 1.
2. Login
   - Pengguna memasukkan username dan password.
   - Sistem mengecek apakah username terdaftar dan password sesuai.
   - Jika salah, sistem menampilkan pesan kesalahan dan jumlah percobaan yang tersisa.
   - Jika sudah 3 kali gagal, program dihentikan.
   - Jika benar, sistem menampilkan username dan role pengguna.
3. Pengecekan Role
   - Jika role adalah admin, pengguna masuk ke Menu Admin dengan 6 pilihan.
   - Jika role adalah user, pengguna masuk ke Menu User dengan 3 pilihan.
4. Menu Admin
   Admin dapat:
   - Tambah WiFi → memasukkan nama, lokasi, dan password WiFi. Sistem memvalidasi data sebelum menyimpan.
   - Tampilkan WiFi → menampilkan seluruh data jaringan WiFi dalam bentuk tabel.
   - Ubah WiFi → memilih ID WiFi kemudian mengubah nama, lokasi, atau password.
   - Hapus WiFi → memilih data WiFi dan melakukan konfirmasi sebelum menghapus.
   - Cari WiFi → mencari jaringan berdasarkan nama atau lokasi.
   - Logout → keluar dari akun dan kembali ke proses utama.
5. Menu User
   User memiliki akses yang lebih terbatas, yaitu:
   - Tampilkan WiFi
   - Cari WiFi
   - Logout
6. Logout dan Selesai
   - Setelah logout, sistem menanyakan apakah pengguna ingin login dengan akun lain.
   - Jika Ya, sistem kembali ke proses login.
   - Jika Tidak, sistem menampilkan pesan bahwa sistem berhasil dihentikan dan proses berakhir.
     
Kesimpulan singkat alur<br>
login - pengecekan role - menu Admin/User - pengelolaan atau pencarian data WiFi - logout - selesai.




























  


