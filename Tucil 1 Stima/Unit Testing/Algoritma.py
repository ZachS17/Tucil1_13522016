# matriks
# array untuk urutan baru concatenate dan match string dengan sekuens concatenated (is in)
# batasan kolom n+1 untuk setiap baris (horizontal)
# batasan baris n+1 untuk setiap kolom (vertical)
# cari satu-satu
# catat perlunya gerakan horizontal atau vertikal (array baris dan kolom tergantung ganjil atau genap)

# urutan harus dari jumlah sekuens minimum karena mencari solusi "optimal"
# ide : dimulai dari belokan 1 langkah sesuai ketentuan

# matriks
baris = int(input("Jumlah baris: "))
kolom = int(input("Jumlah kolom: "))

matrix = []

for i in range(baris):
    row = []
    for j in range(kolom):
        element = input(f"Elemen posisi ({i + 1},{j + 1}): ")
        row.append(element)
    matrix.append(row)

for i in range (baris):
    for j in range(kolom):
        print(matrix[i][j], end=" ")
    print("")

def hitung_kemunculan_satu_sekuens(main,sub):
    jumlah = 0
    indeks = 0

    while True:
        index = main.find(sub, indeks)

        # If no more occurrences are found, break out of the loop
        if index == -1:
            break

        # Increment the count and update the start index for the next search
        jumlah += 1
        indeks = index + 1

    return jumlah

def print_array(array):
    for i in range (len(array)):
        print(array[i],end=" ")

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

# 0 untuk blm, 1 untuk udah
matrikskunjungan = [[0 for i in range(baris)] for j in range (kolom)]

# matriks belokan untuk melihat semua kemungkinan yang sudah dikunjungi dan blm di indeks tertentu
matriksbelokan = [[] for i in range (buffer)]
# masukan sama kayak matriks
# dilakukan "in" untuk lihat di indeks mana blm dimasukkin
# dibiarin yang nggak dipake

def is_element(array,elemen):
    i = 0
    isElement = False
    while i != len(array) and not isElement:
        if array[i] == elemen:
            isElement = True
        i += 1
    return isElement

# proses
while kolomawal != kolom: # mengakhiri penulusuran suatu panjang

    # g pake inisialisasi karena dicheck setiap kali ada tambahan/perubahan
    i = 0
    j = kolomawal
    matrix[i][j] = 1

    indeks = len(sementara) # indeks penelusuran array sementara (belokan)

    # vertikal
    
    # kondisi panjang tidak melebihi
    # maks di indeks dari paling akhir ke paling awal (g ada pilihan lagi)

    # begitu mentok (g bisa gerak kemanapun) -> balikin dan kurangi indeks sampe ketemu valid (dibandingin indeks di array harus lebih besar (kanan bawah))
    
    # kondisi setiap kali mau lihat ada opsi
    if len(sementara) <= buffer: # baru tambahin (kondisi karena g selalu sepanjang buffer)
        sementara.append(1)

    while indeks != -1: # semua indeks sudah maks dan dikunjungi
        # digunakan untuk menelusuri semua kemungkinan pada satu indeks, hanya indeksnya yang dipindahkan, pengecekan juga hanya horizontal atau vertikal

        if indeks % 2 == 0: # genap -> horizontal
            # cek indeks yang masih bisa
            if matrik

        elif indeks % 2 != 0: # ganjil -> vertikal
        elif indeks != len(sementara): # di indeks sebelumnya
            # cek dulu semua kemungkinan dalam indeks
            # tambah indeks
            indeks += 1
        else: # mentok di manapun
            # mundur tapi pengecekan sama
            valid = False
            while not valid: # cari indeks untuk diubah
                indeks -= 1
                if indeks % 2 == 0: # genap -> horizontal
                    batasatas = indeks
                    batasbawah = indeks
                    for i in range (kolom):

    # cek horizontal untuk pilihan
    batasatas = indeks # sejauh mana bisa diambil ke atas (ditambah)
    batasbawah = indeks # sejauh mana bisa diambil ke bawah (dikurang)
    # gerakan horizontal (kolom)
    while matrikskunjungan[sementara[indeks-1]][batasatas] != 1 or matrikskunjungan[sementara[indeks-1]][batasbawah] != 1: # selama g ada halangan
        batasatas += 1
        batasbawah -= 1
        matriksbelokan[indeks].append(batasatas)
        matriksbelokan[indeks].append(batasbawah)

    # penelusuran horizontal
    for i in range (len(matriksbelokan[indeks])):
        if len(sementara) == buffer:
            matriksbelokan[indeks].pop()
            sementara.pop()
            matriksbelokan[indeks].append(matriksbelokan[i])
            sementara.append(matriksbelokan[i])
            # gabung dan nilai

    # cek vertikal untuk pilihan
    batasatas = indeks # sejauh mana bisa diambil ke atas (ditambah)
    batasbawah = indeks # sejauh mana bisa diambil ke bawah (dikurang)
    # gerakan horizontal (kolom)
    while matrikskunjungan[batasatas][sementara[indeks-1]] != 1 or matrikskunjungan[batasbawah][sementara[indeks-1]] != 1: # selama g ada halangan
        batasatas += 1
        batasbawah -= 1
        matriksbelokan[indeks].append(batasatas)
        matriksbelokan[indeks].append(batasbawah)

    # penelusuran vertikal
    for i in range (len(matriksbelokan[indeks])):
        if len(sementara) == buffer:
            matriksbelokan[indeks].pop()
            sementara.pop()
            matriksbelokan[indeks].append(matriksbelokan[i])
            sementara.append(matriksbelokan[i])
            # gabung dan nilai

    if i == 0 or matrikskunjungan[i-1][j] == 1: # tidak bisa ke atas
        if i == baris-1 or matrikskunjungan[i+1][j] == 1: # tidak bisa ke bawah
            break
        else: # bisa ke bawah
            i += 1
    else: # bisa ke bawah
        i -= 1
    sementara.append(i)

    # horizontal
    if j == 0 or matrikskunjungan[i][j-1] == 1: # tidak bisa ke kiri
        if j == kolom-1 or matrikskunjungan[i][j+1] == 1: # tidak bisa ke kanan
            break
        else: # bisa ke kanan
            j += 1
    else: # bisa ke kiri
        i -= 1
    sementara.append(i)

    # penelusuran untuk bengkokin

    # pasti dari indeks akhir
    # mulai dari atas (vertikal)
    # mulai dari kiri (horizontal)

    # pengembalian nilai
    nilai = 0

    kolomawal += 1


# hasil
print("Nilai maksimal = ",hadiah)
print("Solusi =",solusi)
print("Array koordinat =",end=" ")
print_array(jawaban)

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

# selama belum indeks -1 (semua udah maks)
# dikurangi indeks -1 sambil cari valid (cek sebelum dan sesudah) dan dicatat temp_array
  # selama belum sampe indeks terakhir
  # di maks indeks terakhir baru kurangi lagi
# (ulang terus dan pengecekan setiap kali)
# (kondisi visited dan ujung)