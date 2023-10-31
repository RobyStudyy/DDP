nama = "Tretan"
umur = 25

if(umur <=17):
    kategori = "Anak-Anak"
elif(umur >= 18 and umur <=65):
    kategori = "Dewasa"
elif(umur >=65):
    kategori = "Lanjut Usia"

print("Nama \t:" , nama,"\nUmur \t:" , umur,"\nKategori \t:" , kategori)

print()

nilai1 = 19
nilai2 = 15

if(nilai1 > nilai2):
    hasil = "Nilai 1 Lebih Besar Dari Nilai 2"

elif(nilai1 < nilai2):
    hasil = "Nilai 1 Lebih Kecil Dari Nilai 2"

print("Nilai 1 = ", nilai1, "\nNilai 2 = ", nilai2 , "\n",hasil)

