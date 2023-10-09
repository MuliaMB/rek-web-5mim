# var1 = 1
# var2 = 2
# var3 = 1 + 2

# print(var1)
# print(var3)

# varteks = "Ini isi variabel"
# print(varteks)
# type(varteks)

# panjang = 10
# lebar = 20
# luas = panjang * lebar
# print(luas)

# teks1 = "Wildan"
# teks2 = "Haikhal"
# print(teks1 + teks2)

# nama = "Jisoo"
# umur = 27
# tinggi = 170,5
# statusmenikah = False
# kelas = "5MIM"

# print("Nama : ", nama)
# print("Umur : ", umur)
# print("Tinggi : ", tinggi)
# print("Statusmenikah : ", statusmenikah)
# print("Kelas : ", kelas)

# if statusmenikah:
#     print("Menikah")
# else:
#     print("Belum Menikah")

#Kondisi If adalah kondisi yang akan dieksekusi programman jika bernilai benar atau true

nilai = 6

# Jika kondisi benar / truee maka program akan mengeksekusi perintah dibawahnya

if(nilai > 5):
    print("Enam lebih besar dari 5") #kondisi benar akan di eksekusi

# Jika kondisi salah /false maka program tidak akan mengeksekusi perintah dibawahnya

if(nilai > 8):
    print("Enam lebih kecil dari angka 8") #kondisi salah tidak akan di eksekusi

# else if adalah kondisi jika bernilai truee maka akan dieksekusi pada if
# tapi jika kondisi false maka akan dieksekusi pada kode else

nilai = 8

if(nilai > 7):
    print("Selamat anda lulus")
else:
    print("Anda tidak lulus")

#Kondisi ELIF
#contoh kondisi elif

jadwal = "Senin"

if(jadwal == "Senin"):
    print("jadwal kuliah")
elif(jadwal == "Selasa"):
    print("jadwal kuliah")
elif(jadwal == "Rabu"):
    print("jadwal kuliah")
elif(jadwal == "Kamis"):
    print("jadwal kuliah")
elif(jadwal == "Jumat"):
    print("jadwal kuliah")
elif(jadwal == "Sabtu"):
    print("jadwal kuliah")
else:
    print("Libur")

# contoh login
password = "Annie"
passwordinput = input()
    
if password == passwordinput:
    print("Selamat anda berhasil login")
else:
    print("Anda gagal login")