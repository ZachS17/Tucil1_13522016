# matriks
# array untuk urutan baru concatenate dan match string dengan sekuens concatenated (is in)
# batasan kolom n+1 untuk setiap baris (horizontal)
# batasan baris n+1 untuk setiap kolom (vertical)
# cari satu-satu
# catat perlunya gerakan horizontal atau vertikal (array baris dan kolom tergantung ganjil atau genap)

# urutan harus dari jumlah sekuens minimum karena mencari solusi "optimal"
# ide : dimulai dari belokan 1 langkah sesuai ketentuan

import string

# inputan dan inisialisasi nilai

baris = int(input("Jumlah baris: "))
kolom = int(input("Jumlah kolom: "))

buffer = int(input("Jumlah buffer (paling banyak disusun): "))
jsekuens = int(input("Jumlah sekuens (string kode untuk hadiah): "))
arrsekuens = [] # array dari "string" sekuens yang diperbolehkan
hadiahsekuens = [] # array dari hadiah yang sesuai dengan array sekuens
for i in range(jsekuens): # masukan sekuens dan hadiahnya
    sekuens = input("Sekuens ",i+1,": ")
    arrsekuens.append(sekuens)
    hadiah = int(input("Hadiah sekuens ",i+1,": "))
    hadiahsekuens.append(hadiah)

# telusuri semua solusi dari panjang terkecil mungkin (optimal)
# setiap panjang (dari paling kecil)
    # setiap kolom
        
kolomawal = 0 # kolom yang ditelusuri dari awal (0-(kolom-1))
panjang = 1 # catat panjang yang ditelusuri

# array of angka untuk catat
# indeks genap (termasuk 0) untuk kolom, indeks ganjil untuk baris
# tujuannya memastikan tidak ada yang sama dengan array dan untuk mencatat koordinat
# dipisah untuk catat koordinat
posisi = [0]

# setiap penulusuran ketika sudah panjang tertentu masuk ke array
# setelah masuk array diconcatenate dan diperiksa nilainya
# jika lebih besar dari yang sudah ada / awal, akan dimasukkan pada array koordinat jawaban dan solusinya (string jawaban)

sementara = [] # array koordinat (koordinat dalam array juga biar mudah akses) sementara (setiap telusuran)
# jawaban tinggal = jawabansem

jawaban = [] # array koordinat
solusi = "" # string solusi (bisa dari array ketemu)

hadiah = 0 # nilai total jumlah terbesar
nilai = 0 # nilai total yang sedang ditelusuri

def koordinat_jadi_kode(array): # gabung array kode jadi string untuk penyocokan
    gabungan = ""
    for i in range (len(array)):
        kata = (array[i])[0][1]
        gabungan = gabungan + kata + " "
    return gabungan

# panjang string
    # kolom awal yang ditelusuri
        # indeks array kedua sampe akhir maksimal?

# ide: labelin yang udah dikunjungi

# proses
while panjang != buffer:
    # # inisalisasi awal (bengkok satu-satu)
    # # otomatis kolom 1 baris 1
    # i = 0
    # j = 0
    # if panjang % 2 != 0:
    #     while len(sementara) != panjang and :
    #         i += 1
    #         sementara.append([i][j])
    #         j += 1
    #         sementara.append([i][j])


    indeks = panjang # indeks array yang diubah-ubah

    while kolomawal != kolom: # mengakhiri penulusuran suatu panjang
        # penelusuran

        # pasti dari indeks akhir
        # mulai dari atas (vertikal)
        # mulai dari kiri (horizontal)

        temp = indeks # simpan info awal sebelum dibengkok dan atur jarak

        # penyelidikan/penyocokan
        kodetelusuran = koordinat_jadi_kode(sementara)
        for i in range (jsekuens):
            indekssekuens = hitung_kemunculan_satu_sekuens(kodetelusuran,arrsekuens[i])
            nilai += hadiahsekuens[indekssekuens]
        
        # cek terbesar atau bukan
        if nilai > hadiah:
            hadiah = nilai
            solusi = kodetelusuran
            jawaban = sementara

        # pengembalian nilai
        nilai = 0

        # kondisi gerak berikutnya
        if (sementara[indeks])[0] == baris and indeks % 2 == 0: # indeks baris melebihi (genap -> gerak vertikal)
            (sementara[indeks])[0] = temp
            sementara[indeks-1][1] += 1 # sumbu y tambah
        elif (sementara[indeks])[0] == baris and indeks % 2 != 0: # indeks baris melebihi (ganjil -> gerak horizontal)
            sementara[indeks-1][0] -= 1

        kolomawal += 1
    
    # panjang berikutnya
    panjang += 1


# hasil
print("Nilai maksimal = ",hadiah)
print("Solusi =",solusi)
print("Array koordinat =",end=" ")
print_array(jawaban)

# terbesar (blm dikoreksi kebanyakan)
# masih salah (dibelokin ujungnya sampe maksimal dulu) -> buat kondisi untuk menambah dan mengurangi
# semua harus ditelusuri karena g tahu yang paling besar yang mana

# 2 kode
# 1,1 2,2 3,3 4,4 5,5

# 3 kode
# 1,1 2,1 2,2
# 1,2 2,2 2,1
# 1,2 2,2 2,3

# 4 kode
# 1,1 2,1 2,2 1,2
# 1,1 2,1 2,2 3,2

# belokin yang paling ujungnya sesuai arah dan begitu habis baru ke sebelumnya (pake while supaya tidak melebihi) 

# cek horizontal dan vertikal sampe indeks 0 (awal)
# atau dikurangi 

# kanan dan bawah dulu (kolom awal)
# cek sekiri dan seatas mungkin
# ditambah pas mau belok

matrikskunjungan = []
visited = True

# vertikal
# indeks terakhir
valid = True
ibaris = 1
ikolom = 1

# kondisi salah karena harusnya pas mau belok
temp = sementara[ibaris] # ordinat
while sementara[ibaris] != -1 and matrikskunjungan[ibaris] != visited: # selama belum paling atas

    sementara.append([ibaris,sementara[ibaris-1]])

    # penyelidikan/penyocokan
    kodetelusuran = koordinat_jadi_kode(sementara)
    for i in range (jsekuens):
        indekssekuens = hitung_kemunculan_satu_sekuens(kodetelusuran,arrsekuens[i])
        nilai += hadiahsekuens[indekssekuens]
    
    # cek terbesar atau bukan
    if nilai > hadiah:
        hadiah = nilai
        solusi = kodetelusuran
        jawaban = sementara

    sementara.pop()

    ibaris -= 1

sementara[ibaris] = temp+1 # ke bawahnya
    
while sementara[ibaris] != baris and matrikskunjungan[ibaris] != visited: # selama belum paling bawah
    # penyelidikan/penyocokan
    sementara.append([ibaris,sementara[ibaris-1]])
    kodetelusuran = koordinat_jadi_kode(sementara)
    for i in range (jsekuens):
        indekssekuens = hitung_kemunculan_satu_sekuens(kodetelusuran,arrsekuens[i])
        nilai += hadiahsekuens[indekssekuens]

    # cek terbesar atau bukan
    if nilai > hadiah:
        hadiah = nilai
        solusi = kodetelusuran
        jawaban = sementara

    sementara.pop()

    ibaris += 1

temp = sementara[ikolom]

# selama belum paling kiri
while sementara[ikolom] != kolom and matrikskunjungan[ikolom] != visited: # selama belum paling bawah
    # penyelidikan/penyocokan
    sementara.append([ikolom,sementara[ikolom-1]])
    kodetelusuran = koordinat_jadi_kode(sementara)
    for i in range (jsekuens):
        indekssekuens = hitung_kemunculan_satu_sekuens(kodetelusuran,arrsekuens[i])
        nilai += hadiahsekuens[indekssekuens]

    # cek terbesar atau bukan
    if nilai > hadiah:
        hadiah = nilai
        solusi = kodetelusuran
        jawaban = sementara

    sementara.pop()

    ikolom -= 1

sementara[ikolom] = temp

# selama belum paling kanan
while sementara[ikolom] != kolom and matrikskunjungan[ikolom] != visited: # selama belum paling bawah
    # penyelidikan/penyocokan
    sementara.append([ikolom,sementara[ikolom-1]])
    kodetelusuran = koordinat_jadi_kode(sementara)
    for i in range (jsekuens):
        indekssekuens = hitung_kemunculan_satu_sekuens(kodetelusuran,arrsekuens[i])
        nilai += hadiahsekuens[indekssekuens]

    # cek terbesar atau bukan
    if nilai > hadiah:
        hadiah = nilai
        solusi = kodetelusuran
        jawaban = sementara

    sementara.pop()

    ikolom += 1

indeks_array_sementara = 1
array_temp = [] # array untuk menyimpan nilai awal dari cabang-cabang yang mau dibengkok (semua karena bisa jadi berubah sampai indeks awal)
# pemeriksaan dari indeks sampai ujung terus
while indeks_array_sementara != -1: # pemeriksaan dikurang terus ke kiri (begitu mentok -> ujung atau kena yang lain)
    # proses pemeriksaan indeks terakhir (contoh)

    # begitu mentok
    valid = False
    while not valid: # mencari tempat valid untuk mulai pencarian lagi
        indeks -= 1 # indeks array dikurangi (sebelum yang mentok)
        # cek indeks sebelumnya udah mentok atau blm (batas kanan dan bawahnya)
        # dibandingin dengan nilai awal di temp array

    # akhir
    indeks_array_sementara -= 1