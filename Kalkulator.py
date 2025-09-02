angkaPertama = int(input("Masukkan angka pertama: "))
angkaKedua = int(input("Masukkan angka kedua: "))
operasi = input("Masukkan operasi (+, -, *, /): ")

if operasi == "+":
    hasil = float(angkaPertama) + float(angkaKedua)
    print("Hasil: ", hasil)
