# FINAL PROJECT UAS - KELOMPOK
# Anggota:
# 1. Lencana (24241189)
# 2. Kezia (24241169)

# Meet 1 - Perbandingan Boolean
def meet1_perbandingan_boolean():
    print("Perbandingan Boolean:")
    a = 24
    b = 69
    print("a < b  :", a < b)
    print("a > b  :", a > b)
    print("a >= b :", a >= b)
    print("a <= b :", a <= b)
    print("a != b :", a != b)
    print("not (a < b) :", not (a < b))


# Meet 2 - Operasi Logika
def meet2_operasi_logika():
    print("Operasi Logika:")
    x = True
    z = not x
    print("Nilai dari z =", z)

    print("\n** AND ***")
    print(True, 'and', True, '=', True and True)
    print(True, 'and', False, '=', True and False)
    print(False, 'and', True, '=', False and True)
    print(False, 'and', False, '=', False and False)

    print("\n** XOR ***")
    print(True, 'xor', True, '=', True != True)
    print(True, 'xor', False, '=', True != False)
    print(False, 'xor', True, '=', False != True)
    print(False, 'xor', False, '=', False != False)


# Meet 3 & 4 - Hitung Luas Persegi / Segitiga
def meet3_hitung_luas():
    pilihan = input("Hitung luas persegi atau segitiga? ").lower()
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
        print("Pilihan tidak valid.")


# Meet 5 - Kalkulator
def meet5_kalkulator():
    operasi = input("Operasi (+ - x :) : ")
    bil1 = float(input("Masukkan bilangan pertama: "))
    bil2 = float(input("Masukkan bilangan kedua: "))

    if operasi == "+":
        hasil = bil1 + bil2
    elif operasi == "-":
        hasil = bil1 - bil2
    elif operasi == "x":
        hasil = bil1 * bil2
    elif operasi == ":":
        hasil = bil1 / bil2
    else:
        hasil = "Operasi tidak dikenali"

    print("Hasil =", hasil)


# Meet 6 - Kondisional Admin
def meet6_kondisional_admin():
    hak_akses = "bukan admin"
    print("full akses" if hak_akses == "admin" else "akses denied")


# Meet 7 - Password Checker
def meet7_password_checker():
    password = input("Masukkan password anda: ")
    if len(password) < 8:
        print("Karakter kurang")
    else:
        print("Karakter cukup")


# Meet 8 - Manipulasi String Number
def meet8_manipulasi_number():
    number = "1234567890"
    print("Data terakhir:", number[-1])
    print("Data pertama:", number[0])
    print("Data ke-3 sampai ke-6:", number[2:6])


# Meet 9 & 10 - Pemisahan Domain
def meet9_pisah_domain():
    domain_lengkap = input("Masukkan nama domain anda (contoh: cu.net): ")
    if '.' in domain_lengkap:
        nama_domain, ekstensi = domain_lengkap.split(".")
        print("Nama domain anda :", nama_domain)
        print("Domain yg anda gunakan :", ekstensi)
    else:
        print("Format domain tidak valid.")


# MENU UTAMA
while True:
    print("\n##### KELOMPOK #####")
    print("1. Lencana")
    print("2. Kezia")
    print("####################\n")

    print("Daftar Program:")
    print("1. Meet 1 - Perbandingan Boolean")
    print("2. Meet 2 - Operasi Logika")
    print("3. Meet 3 & 4 - Perhitungan Luas")
    print("4. Meet 5 - Kalkulator Sederhana")
    print("5. Meet 6 - Kondisional Admin")
    print("6. Meet 7 - Password Checker")
    print("7. Meet 8 - Manipulasi String Number")
    print("8. Meet 9 & 10 - Pemisahan Domain")
    print("0. Keluar Program\n")

    pilihan = input("Masukkan nomor program yang ingin dijalankan: ")

    if pilihan == "1":
        meet1_perbandingan_boolean()
    elif pilihan == "2":
        meet2_operasi_logika()
    elif pilihan == "3":
        meet3_hitung_luas()
    elif pilihan == "4":
        meet5_kalkulator()
    elif pilihan == "5":
        meet6_kondisional_admin()
    elif pilihan == "6":
        meet7_password_checker()
    elif pilihan == "7":
        meet8_manipulasi_number()
    elif pilihan == "8":
        meet9_pisah_domain()
    elif pilihan == "0":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak tersedia.")