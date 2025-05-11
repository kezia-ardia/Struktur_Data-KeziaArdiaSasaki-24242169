#program kalkulator sederhana
# x + - :
oprasi = input("anda ingin mengoperasikan apa (x + - :)") 
bil1 = float(input("masukan bilangan pertama"))
bil2 = float(input("masukan bilangan kedua"))

if oprasi == "+" :
   final = bil1 + bil2
   print(final)
elif oprasi == "-" :
   final = bil1 - bil2
   print(final)
elif oprasi == "x" :
   final = bil1 * bil2
   print(final)
else :
   final = bil1/bil2
   print(final)