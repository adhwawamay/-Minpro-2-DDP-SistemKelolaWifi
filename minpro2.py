import os
from datetime import datetime
import pwinput
from prettytable import PrettyTable

MAKS_PERCOBAAN_LOGIN = 3
MIN_PANJANG_PASSWORD_WIFI = 8

akun_pengguna = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}

data_wifi = {
    "WT001": {
        "nama": "WiFi Gedung C",
        "lokasi": "Gedung C",
        "password": "Teknikunmul",
        "diperbarui": "-"
    },
    "WT002": {
        "nama": "WiFi Lab Komputer",
        "lokasi": "Lab Komputer",
        "password": "123456789",
        "diperbarui": "-"
    },
    "WT003": {
        "nama": "WiFi Perpustakaan",
        "lokasi": "Perpustakaan",
        "password": "Perpus.bersama",
        "diperbarui": "-"
    }
}

def waktu_sekarang():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def jeda():
    input("\nNEXT - ENTER")

def input_teks(pesan, boleh_kosong=False):
    while True:
        nilai = input(pesan)
        if nilai == "":
            if boleh_kosong:
                return nilai
            else:
                print("Input tidak boleh kosong. Silakan coba lagi.")
        else:
            return nilai

def input_password_wifi(pesan, boleh_kosong=False):
    while True:
        nilai = input(pesan)

        if nilai == "" and boleh_kosong:
            return nilai
        if nilai == "":
            print("Password tidak boleh kosong.")
        elif len(nilai) < MIN_PANJANG_PASSWORD_WIFI:
            print("Password minimal 8 karakter.")
        elif " " in nilai:
            print("Password tidak boleh mengandung spasi.")
        else:
            return nilai

def input_menu(pesan, batas_bawah, batas_atas):
    while True:
        try:
            angka = int(input(pesan))

            if batas_bawah <= angka <= batas_atas:
                return angka

            print("Pilihan harus antara", batas_bawah, "dan", batas_atas)

        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")

def nama_sudah_ada(data, nama, kecuali_id=None):
    for id_wifi in data:
        if id_wifi != kecuali_id:
            if data[id_wifi]["nama"] == nama:
                return True

    return False

def buat_id_baru(data):
    angka_terbesar = 0

    for id_wifi in data:
        try:
            angka = int(id_wifi[2:])

            if angka > angka_terbesar:
                angka_terbesar = angka

        except ValueError:
            pass

    angka_baru = angka_terbesar + 1

    if angka_baru < 10:
        return "WT00" + str(angka_baru)
    elif angka_baru < 100:
        return "WT0" + str(angka_baru)
    else:
        return "WT" + str(angka_baru)

def pilih_id_wifi(data, pesan):
    tampilkan_ringkas(data)

    while True:
        id_wifi = input(pesan)

        if id_wifi == "0":
            return None

        if id_wifi in data:
            return id_wifi

        print("ID tidak ditemukan.")
        print("Contoh ID yang benar: WT001")
        print("Ketik 0 untuk membatalkan.")

def buat_tabel(data, lengkap=True):
    tabel = PrettyTable()

    if lengkap:
        tabel.field_names = [
            "No",
            "ID",
            "Nama WiFi",
            "Lokasi",
            "Password",
            "Diperbarui"
        ]
    else:
        tabel.field_names = [
            "No",
            "ID",
            "Nama WiFi",
            "Lokasi"
        ]

    nomor = 1

    for id_wifi in data:
        info = data[id_wifi]

        baris = [
            nomor,
            id_wifi,
            info["nama"],
            info["lokasi"]
        ]

        if lengkap:
            baris.append(info["password"])
            baris.append(info["diperbarui"])

        tabel.add_row(baris)
        nomor = nomor + 1

    tabel.align = "l"

    return tabel

def tampilkan_ringkas(data):
    print(buat_tabel(data, lengkap=False))

def tampilkan_wifi(data):
    print("\n=== DAFTAR JARINGAN WIFI ===")

    if len(data) == 0:
        print("Belum ada data WiFi yang tersimpan.")
        return

    print(buat_tabel(data))
    print("Total:", len(data), "jaringan WiFi")

def tambah_wifi(data):
    print("\n=== TAMBAH JARINGAN WIFI BARU ===")

    nama = input_teks("Masukkan nama WiFi     : ")

    if nama_sudah_ada(data, nama):
        print("Nama WiFi sudah terdaftar.")
        print("Penambahan dibatalkan.")
        return

    lokasi = input_teks("Masukkan lokasi WiFi   : ")

    password = input_password_wifi(
        "Masukkan password WiFi : "
    )

    id_baru = buat_id_baru(data)

    data[id_baru] = {
        "nama": nama,
        "lokasi": lokasi,
        "password": password,
        "diperbarui": waktu_sekarang()
    }

    print("Jaringan WiFi berhasil ditambahkan.")
    print("ID WiFi baru:", id_baru)

def ubah_wifi(data):
    print("\n=== UBAH DATA WIFI ===")

    if len(data) == 0:
        print("Belum ada data WiFi yang tersimpan.")
        return

    id_wifi = pilih_id_wifi(
        data,
        "Masukkan ID WiFi yang ingin diubah (0 = batal): "
    )

    if id_wifi is None:
        print("Perubahan dibatalkan.")
        return

    lama = data[id_wifi]

    print("\nData saat ini:")
    print("Nama     :", lama["nama"])
    print("Lokasi   :", lama["lokasi"])
    print("Password : tidak ditampilkan")

    print("\nKosongkan input jika tidak ingin mengubah data.")

    nama = input(
        "Nama WiFi baru [" + lama["nama"] + "]: "
    )

    if nama != "":
        if nama_sudah_ada(data, nama, id_wifi):
            print("Nama WiFi sudah dipakai jaringan lain.")
            print("Perubahan dibatalkan.")
            return

    lokasi = input(
        "Lokasi baru [" + lama["lokasi"] + "]: "
    )

    password = input_password_wifi(
        "Password baru [kosongkan jika tidak berubah]: ",
        boleh_kosong=True
    )

    if nama != "":
        lama["nama"] = nama

    if lokasi != "":
        lama["lokasi"] = lokasi

    if password != "":
        lama["password"] = password

    lama["diperbarui"] = waktu_sekarang()

    print("Data WiFi berhasil diubah.")

def hapus_wifi(data):
    print("\n=== HAPUS DATA WIFI ===")

    if len(data) == 0:
        print("Belum ada data WiFi yang tersimpan.")
        return

    id_wifi = pilih_id_wifi(
        data,
        "Masukkan ID WiFi yang ingin dihapus (0 = batal): "
    )

    if id_wifi is None:
        print("Penghapusan dibatalkan.")
        return

    print("WiFi yang dipilih:", data[id_wifi]["nama"])

    konfirmasi = input("Yakin hapus? (y/n): ")

    if konfirmasi == "y" or konfirmasi == "Y":
        del data[id_wifi]
        print("Data WiFi telah dihapus.")

    elif konfirmasi == "n" or konfirmasi == "N":
        print("Penghapusan dibatalkan.")

    else:
        print("Pilihan tidak valid.")
        print("Penghapusan dibatalkan.")

def cari_wifi(data):
    print("\n=== CARI JARINGAN WIFI ===")

    kata_kunci = input(
        "Masukkan nama atau lokasi yang dicari: "
    )

    hasil = {}

    for id_wifi in data:
        info = data[id_wifi]

        if (
            kata_kunci.lower() in info["nama"].lower()
            or
            kata_kunci.lower() in info["lokasi"].lower()
        ):
            hasil[id_wifi] = info

    if len(hasil) == 0:
        print("Data tidak ditemukan.")
        return

    print("\nDitemukan", len(hasil), "hasil:")
    print(buat_tabel(hasil))

def login():
    print("=================================================")
    print("     SISTEM DATA JARINGAN WIFI - FAKULTAS TEKNIK")
    print("=================================================")

    for percobaan in range(1, MAKS_PERCOBAAN_LOGIN + 1):

        username = input("Username : ")

        password = pwinput.pwinput(
            prompt="Password : ",
            mask="*"
        )

        if username in akun_pengguna:
            if akun_pengguna[username]["password"] == password:

                print("\nLogin berhasil.")
                print("Selamat datang,", username)
                print("Role:", akun_pengguna[username]["role"])

                return username, akun_pengguna[username]["role"]

        sisa = MAKS_PERCOBAAN_LOGIN - percobaan

        if sisa > 0:
            print("Username atau password salah.")
            print("Sisa percobaan:", sisa)
            print()
        else:
            print("Username atau password salah.")
            print("Kesempatan login habis.")

    return None, None

def menu_admin(username, data):
    while True:
        bersihkan_layar()

        print("=================================================")
        print("MENU ADMIN | Login sebagai:", username)
        print("=================================================")
        print("1. Tambah Jaringan WiFi")
        print("2. Tampilkan Seluruh Jaringan WiFi")
        print("3. Ubah Jaringan WiFi")
        print("4. Hapus Jaringan WiFi")
        print("5. Cari Jaringan WiFi")
        print("6. Logout")
        print("=================================================")

        pilihan = input_menu(
            "Pilih menu (1-6): ",
            1,
            6
        )

        if pilihan == 1:
            tambah_wifi(data)

        elif pilihan == 2:
            tampilkan_wifi(data)

        elif pilihan == 3:
            ubah_wifi(data)

        elif pilihan == 4:
            hapus_wifi(data)

        elif pilihan == 5:
            cari_wifi(data)

        elif pilihan == 6:
            print("\nLogout berhasil.")
            return

        jeda()

def menu_user(username, data):
    while True:
        bersihkan_layar()

        print("=================================================")
        print("MENU USER | Telah login sebagai:", username)
        print("=================================================")
        print("1. Tampilkan Seluruh Jaringan WiFi")
        print("2. Cari Jaringan WiFi")
        print("3. Logout")
        print("=================================================")

        pilihan = input_menu(
            "Pilih menu (1-3): ",
            1,
            3
        )

        if pilihan == 1:
            tampilkan_wifi(data)

        elif pilihan == 2:
            cari_wifi(data)

        elif pilihan == 3:
            print("\nLogout berhasil.")
            return

        jeda()

def main():

    while True:

        username, role = login()

        if username is None:
            print("\nProgram dihentikan karena gagal login.")
            break

        if role == "admin":
            menu_admin(username, data_wifi)

        elif role == "user":
            menu_user(username, data_wifi)

        lagi = input("\nLogin dengan akun lain? (y/n): ")

        if lagi != "y" and lagi != "Y":
            print("Sistem berhasil dihentikan.")
            print("Terima kasih.")
            break

        bersihkan_layar()

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        print("\n\nProgram dihentikan oleh pengguna.")
