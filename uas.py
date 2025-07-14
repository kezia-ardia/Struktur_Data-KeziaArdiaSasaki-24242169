# FINAL PROJECT UAS - KELOMPOK 
# Anggota:
# 1. Lencana (24241189)
# 2. Kezia (24241169)

def meet1_perbandingan_bolean():
    print("Program Perbandingan (Boolean)")

    a = 24
    b = 69
    print("a < b =", a < b)
    print("a > b =", a > b)
    print("a >= b =", a >= b)
    print("a <= b =", a <= b)
    print("a != b =", a != b)
    print("not (a < b) =", not (a < b))


def meet2__tabel_kebenaran():
    x = True
    y = False

    print("Program Tabel Kebenaran / Operasi Logika")
    print("AND:", x and y)
    print("OR :", x or y)
    print("XOR:", x != y)
    print("NOT x:", not x)


def meet3_hitung_luas():
    pilihan = input("Ingin menghitung luas persegi atau segitiga? ").lower()
    if pilihan == "persegi":
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        luas = panjang * lebar
        print(f"Luas persegi: {luas}")
    elif pilihan == "segitiga":
        alas = int(input("Masukkan alas: "))
        tinggi = int(input("Masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print(f"Luas segitiga: {luas}")
    else:
        print("Pilihan tidak valid")


def meet4_kalkulator():
    operasi = input("Operasi (x + - :) : ")
    bil1 = float(input("Masukkan bilangan pertama: "))
    bil2 = float(input("Masukkan bilangan kedua: "))

    if operasi == "+":
        print("Hasil =", bil1 + bil2)
    elif operasi == "-":
        print("Hasil =", bil1 - bil2)
    elif operasi == "x":
        print("Hasil =", bil1 * bil2)
    elif operasi == ":":
        print("Hasil =", bil1 / bil2)
    else:
        print("Operasi tidak dikenal")


def meet5_password_checker():
    password = input("Masukkan password anda: ")
    if len(password) < 8:
        print("Karakter kurang")
    else:
        print("Karakter cukup")


def meet6_manipulasi_number():
    number = "1234567890"
    print("Data terakhir:", number[-1])
    print("Data pertama:", number[0])
    print("Data ke-3 sampai ke-6:", number[2:6])


def meet7_pisah_domain():
    domain_lengkap = input("Masukkan nama domain anda (contoh: cu.net): ")
    if '.' in domain_lengkap:
        nama_domain, ekstensi = domain_lengkap.split(".")
        print("Nama domain:", nama_domain)
        print("Ekstensi:", ekstensi)
    else:
        print("Format domain tidak valid")


# MAIN PROGRAM MENU
while True:
    print("\n######## FINAL PROJECT MENU ########")
    print("Kelompok:")
    print("1. Lencana")
    print("2. Kezia")
    print("#####################################")
    print("\nDaftar Program:")
    print("1. Perbandingan Boolean")
    print("2. Tabel Kebenaran / Logika")
    print("3. Perhitungan Luas")
    print("4. Kalkulator Sederhana")
    print("5. Password Checker")
    print("6. Manipulasi String Number")
    print("7. Pemisahan Domain")
    print("0. Keluar")

    pilihan = input("Masukkan nomor program yang ingin dijalankan: ")

    if pilihan == "1":
        meet1_perbandingan_bolean()
    elif pilihan == "2":
        meet2_tabel_kebenaran()
    elif pilihan == "3":
        meet3_hitung_luas()
    elif pilihan == "4":
        meet4_kalkulator()
    elif pilihan == "5":
        meet5_password_checker()
    elif pilihan == "6":
        meet6_manipulasi_number()
    elif pilihan == "7":
        meet7_pisah_domain()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")