profilKendaran = ["xsr25","motor","250cc","hitam",2]
profilKendaran.append("40000000")
profilKendaran.append("motor sport")
profilKendaran.insert(2,"yamaha")
print(profilKendaran)

soal = int(input("Menghitung Luas Bangun Datar(pilih dari 1-3) :"))
match soal:
    case 1:
        print("Menghitung luas Persegi")
        sisipersegi = int(input("Masukkan sisi :"))
        luaspersegi = sisipersegi * sisipersegi
        print("Luas Persegi = " , luaspersegi)
    case 2:
        print("Menghitung luas Lingkaran\n")
        jariJariLingkaran = int(input("Masukkan Jari jari lingkaran ;"))
        luasLingkaran = 3.14 * jariJariLingkaran * jariJariLingkaran
        print("Luas lingkaran = " , float(luasLingkaran))
    case 3:
        print("Menghitung luas Segitiga")
        alasSegitiga = int(input("Masukan Alas Segitiga :"))
        tinggiSegitiga = int(input("Masukan Tinggi Segitiga :"))
        luasSegitiga = 1/2 * alasSegitiga * tinggiSegitiga
        print("Luas Segitiga = " , int(luasSegitiga))

