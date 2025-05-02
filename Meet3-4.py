# Buatlah program perhitungan luas

masukan = input("apakah anda ingin menghitung persegi atau segitiga")

# persegi
panjang = int(input("masukan panjang"))
lebar = int(input("masukan lebar"))
luas = panjang*lebar
print(f"luas persegi = {luas}")

# segitiga
alas = int(input("masukan alas"))
tinggi = int(input("masukan tinggi"))
luas = 1/2*alas*tinggi
print(f"luas segitiga = {luas}")