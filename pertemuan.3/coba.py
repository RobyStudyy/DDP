x = 10
y = 10

hasil = x == y
print(hasil)

print()

nama = ["yono", 18, 20.000, "Jakarta"]
hasil = 18 in nama
print(hasil)

print()

a=10
b=30
if a > 30:
    print('a lebih besar dari b') 

print()

#deklarasi dan inisialisasi variable
pelanggan = "aiman ilham"
totalBelanja = 20000
x
#struktur kendali if
if(totalBelanja > 100000):
    keterangan = "Selamat Anda Mendapatkan Skin"

else:
    keterangan  = "Terima Kasih Sudah Order"

#cetakdata
print("pelanggan",pelanggan, "\nTotal Belanja anda Rp.",totalBelanja,"\n",keterangan)

print()

#siswa dinyatakan lulus minimal 70 nilainya
nama = "reja arab"
matpel = "Matematika"
nilai = 88

#ternarty
keterangan = "Lulus" if nilai >= 70 else "Gagal"

#cetakdata
print("Nama Siswa \t:", nama, "\nMata Pelajaran \t:", matpel,
      "\nNilai\t\t:", nilai, "\nKeterangan \t:", keterangan)

print()

nama = "Coki Pardede"
matpel = "Agama"
nilai = 10
#uji grade dengan if Multi Kondisi
if(nilai >= 85 and nilai <= 100):
    grade = "A"
elif(nilai >= 75 and nilai <= 85):
    grade = "B"
elif(nilai >= 60 and nilai <= 75):
    grade = "C"
elif(nilai >= 30 and nilai <= 60):
    grade = "D"
else:
    grade = "E"
print("Nilai Akreditasi \t:",grade)