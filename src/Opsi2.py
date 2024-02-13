with open('input.txt','r') as file:
    lines = file.readlines()
buffer = lines[0].strip()
baris,kolom = map(int,lines[1].split())
indeksline = 2
matriks = []
for i in range (baris):
    stringtemp = lines[indeksline]
    # print(stringtemp)
    arrtemp = stringtemp.split()
    matriks.append(arrtemp)
    indeksline += 1
jsekuens = lines[indeksline].strip()
indeksline += 1
arrsekuens = [] # array dari "string" sekuens yang diperbolehkan
hadiahsekuens = [] # array dari hadiah yang sesuai dengan array sekuens
for i in range(int(jsekuens)): # masukan sekuens dan hadiahnya
    sekuens = lines[indeksline].strip()
    arrsekuens.append(sekuens)
    indeksline += 1
    hadiah = lines[indeksline].strip()
    hadiahsekuens.append(hadiah)
    indeksline += 1
arrtoken = []
count = 0
for i in range (baris):
    for j in range (kolom):
        # print(matriks[i][j])
        count += 1
        if matriks[i][j] not in arrtoken:
            # print(matriks[i][j])
            arrtoken.append(matriks[i][j])
buffer = int(buffer)
jsekuens = int(jsekuens)
for i in range (len(hadiahsekuens)):
    hadiahsekuens[i] = int(hadiahsekuens[i])

# def print_array(array):
#     for i in range (len(array)):
#         print(array[i],end=" ")
#     print("")

# def print_matriks(matriks):
#     for i in range (len(matriks)):
#         for j in range(len(matriks[0])):
#             print(matriks[i][j], end=" ")
#         print("")

# debug
# print_array(arrsekuens)
# print_array(hadiahsekuens)
# print_array(arrtoken)
# print(arrsekuens[0])
# print(hadiahsekuens[0])
# print(baris)
# print(kolom)
            
kolomawal = 0 # kolom yang ditelusuri dari awal (0-(kolom-1))

# array of angka untuk catat
# indeks genap (termasuk 0) untuk kolom, indeks ganjil untuk baris
# tujuannya memastikan tidak ada yang sama dengan array dan untuk mencatat koordinat
# dipisah untuk catat koordinat

sementara = []

# setiap penulusuran ketika sudah panjang tertentu masuk ke array
# setelah masuk array diconcatenate dan diperiksa nilainya
# jika lebih besar dari yang sudah ada / awal, akan dimasukkan pada array koordinat jawaban

jawaban = [1 for i in range (buffer)] # array koordinat
solusi = "" # string solusi (bisa dari array ketemu)

hadiah = 0 # nilai total jumlah terbesar
nilai = 0 # nilai total yang sedang ditelusuri

def koordinat_jadi_kode(array): # gabung array kode jadi string untuk penyocokan
    gabungan = ""
    for i in range (len(array)):
        kata = (array[i])[0][1]
        gabungan = gabungan + kata + " "
    return gabungan

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

# labelin yang udah dikunjungi

# 0 untuk blm, 1 untuk udah
matrikskunjungan = [[0 for i in range(baris)] for j in range (kolom)]

# matriks belokan untuk melihat semua kemungkinan yang sudah dikunjungi dan blm di indeks tertentu
matriksbelokan = [[] for i in range (buffer+1)] # pengecekan maksimal di indeks buffer
# indeks matriks untuk gerakan ke berapa
# elemennya array dengan isi array angka kemungkinan

def print_array(array):
        for i in range (len(array)):
            print(array[i],end=" ")

def is_element(array,elemen):
    i = 0
    isElement = False
    while i != len(array) and not isElement:
        if array[i] == elemen:
            isElement = True
        i += 1
    return isElement

def array_to_array_of_coordinate(array): # ubah jadi array koordinat
    arraykoordinat = [[1,array[0]+1]] # elemen pertama dalam array
    i = 1
    while i+1 != len(array):
        if i % 2 == 0: # genap -> angka kolom
            arraykoordinat.append([array[i+1]+1,array[i]+1])
        else: # ganjil -> angka baris
            arraykoordinat.append([array[i]+1,array[i+1]+1])
        i += 1
    return arraykoordinat

def print_koordinat(array):
    for i in range (len(array)):
        print('[',array[i][0],',',array[i][1],']')

def hitung_hadiah(array,matriks,arrsekuens,arrhadiah):
    kata = ''
    for i in range (len(array)):
        kata = kata + matriks[array[i][0]][array[i][1]] + " "
    hadiah = 0
    for i in range (len(arrsekuens)):
        hadiah += (hitung_kemunculan_satu_sekuens(kata,arrsekuens[i]) * arrhadiah[i])
    return hadiah

def array_to_string(array,matriks):
    kata = ''
    for i in range (len(array)):
        kata = kata + matriks[array[i][0]][array[i][1]] + " "
    return kata

# proses
    # g pake inisialisasi karena dicheck setiap kali ada tambahan/perubahan

    # begitu mentok (g bisa gerak kemanapun) -> balikin dan kurangi indeks sampe ketemu valid (dibandingin indeks di array harus lebih besar (kanan bawah))
    
    # kondisi setiap kali mau lihat ada opsi

    # penelusuran untuk bengkokin

    # pasti dari indeks akhir
    # mulai dari atas (vertikal)
    # mulai dari kiri (horizontal)

    # pengembalian nilai

# belokin yang paling ujungnya sesuai arah dan begitu habis baru ke sebelumnya (pake while supaya tidak melebihi) 

# cek horizontal dan vertikal sampe indeks 0 (awal)

# arah nggak begitu penting karena dicatat semua

# selama belum indeks -1 (semua udah habis)
# dikurangi indeks -1 sambil cari valid (cek sebelum dan sesudah) dan dicatat temp_array
# selama belum sampe indeks -1 dan array tidak kosong
    # begitu habis -> kurangi indeks sampe g kosong
# (kondisi visited dan ujung)
    
# masukin dulu elemen kolom pertama
while kolomawal != kolom: # batas kolom awal
    for i in range (1,baris): # gerakan/elemen pertama pasti sebanyak baris
        matriksbelokan[0].append(i) # tambahin semua kemungkinan
    indeks = 1 # indeks array untuk ditelusuri
    # selama masih ada arah dan panjangnya blm sama dengan buffer

    # indeks terakhir kosong -> kurangi satu indeks (pencarian dari ujung dibelokin)
    sudahakhir = False # mentok atau panjang sudah ngepas
    # sampai bertemu yang tidak kosong

    while len(matriksbelokan[0]) != 0: # masih ada pilihan di indeks awal
        if indeks % 2 == 0: # indeks genap -> gerakan vertikal (baris ke berapa) -> cek 
            if len(matriksbelokan[indeks]) == 0: # mau diisi
                if indeks == buffer: # panjangnya sudah maksimal
                    indeks -= 1 # balik ke indeks sebelumnya yang sudah pilih rute
                    sudahakhir = True # sudah terakhir
                else: # masih bisa ditambahkan
                    # cari dulu
                    temp = sementara[indeks-2] # nilai untuk dibengkokkan
                    # cek vertikal untuk pilihan
                    batasatas = temp # sejauh mana bisa diambil ke atas (ditambah)
                    batasbawah = temp # sejauh mana bisa diambil ke bawah (dikurang)
                    # gerakan vertikal (baris)
                    while True: # selama g ada halangan
                        if batasatas >= baris:
                            if batasbawah < 0: # tidak memenuhi
                                break
                        else:
                            if matrikskunjungan[batasatas][sementara[indeks-1]] != 1 and batasatas < baris:
                                batasatas += 1
                                matriksbelokan[indeks].append(batasatas)
                            if matrikskunjungan[batasbawah][sementara[indeks-1]] != 1 and batasbawah >= 0:
                                batasbawah -= 1
                                matriksbelokan[indeks].append(batasbawah)

                    # tergantung panjangnya dilihat mentok atau tidak
                    if len(matriksbelokan[indeks]) == 0: # tidak ada kemungkinan lagi
                        indeks -= 1
                        sudahakhir = True # mentok -> mulai menghabiskan kemungkinan
                    else: # ada pilihan
                        indeks += 1
                        sementara.append(matriksbelokan[indeks][len(matriksbelokan[indeks])-1]) # masukin nilai terakhir setelah pencarian

                    # pengecekan nilai
                    arraykoordinat = array_to_array_of_coordinate(sementara)
                    hadiah = hitung_hadiah(arraykoordinat,matriks,arrsekuens,hadiahsekuens)
                    if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                        jawaban = arraykoordinat
                        solusi = array_to_string(arraykoordinat)
                    nilai = 0 # reset

            else: # sudah diisi (masih ada yang blm dikunjungi)
                if not sudahakhir: # bukan terakhir -> dipilih sebagai rute saja (ditandai)
                    temp = matriksbelokan[indeks][len(matriksbelokan[indeks])-1] # temp = yang mau dikunjungi berikutnya
                    sementara[indeks] = temp # update ke array sementara
                    # pengecekan nilai
                    arraykoordinat = array_to_array_of_coordinate(sementara)
                    hadiah = hitung_hadiah(arraykoordinat,matriks,arrsekuens,hadiahsekuens)
                    if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                        jawaban = arraykoordinat
                        solusi = array_to_string(arraykoordinat)
                    nilai = 0 # reset
                    # label yang sudah dilewati
                    if temp > sementara[indeks-2]: # turun
                        awal = sementara[indeks-2]
                    elif temp < sementara[indeks-2]: # naik
                        awal = temp
                    for i in range (awal,temp+1): # kecil ke besar
                        matriksbelokan[i][sementara[indeks-1]] = 1 # label dikunjungi
                    indeks += 1
                else: # sudah mentok (indeks yang ditelusuri sudah terakhir)
                    # habiskan semua pilihan indeks terakhir
                    while len(matriksbelokan[indeks]) != 0:
                        # pengecekan nilai
                        arraykoordinat = array_to_array_of_coordinate(sementara)
                        hadiah = hitung_hadiah(arraykoordinat,matriks,arrsekuens,hadiahsekuens)
                        if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                            jawaban = arraykoordinat
                            solusi = array_to_string(arraykoordinat)
                        nilai = 0 # reset
                        # pop elemen
                        matriksbelokan[indeks].pop()
                    # reset pengunjungan
                    # genap
                    if indeks != 0:
                        if sementara[indeks-2] > sementara[indeks]: # belok ke atas
                            # reset ke bawah
                            for i in range (sementara[indeks],sementara[indeks-2]):
                                matrikskunjungan[i][sementara[indeks-1]] = 0
                        else: # belok ke bawah
                            # reset ke atas
                            for i in range (sementara[indeks-2]+1,sementara[indeks]+1):
                                matrikskunjungan[i][sementara[indeks-1]] = 0
                    else:
                        for i in range (baris):
                            matrikskunjungan[i][kolomawal] = 0
                    sementara.pop() # hapus juga nilai di sementara
                    while len(matriksbelokan[indeks]) == 0: # cari sampai tidak kosong
                        indeks -= 1
                        sementara.pop()
                        matriksbelokan[indeks].pop() # hapus indeks sebelumnya yang dipakai sebagai rute
                        # reset pengunjungan
                        if indeks % 2 != 0:
                            # ganjil
                            if indeks != 1:
                                if sementara[indeks-2] > sementara[indeks]: # belok ke kiri
                                    # reset ke kanan
                                    for i in range (sementara[indeks],sementara[indeks-2]):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                                else: # belok ke kanan
                                    # reset ke kiri
                                    for i in range (sementara[indeks-2]+1,sementara[indeks]+1):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                            else:
                                if kolomawal > sementara[indeks]: # belok ke kiri
                                    # reset ke kanan
                                    for i in range (sementara[indeks],kolomawal):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                                else: # belok ke kanan
                                    # reset ke kiri
                                    for i in range (kolomawal+1,sementara[indeks]+1):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                        else:
                            # genap
                            if indeks != 0:
                                if sementara[indeks-2] > sementara[indeks]: # belok ke atas
                                    # reset ke bawah
                                    for i in range (sementara[indeks],sementara[indeks-2]):
                                        matrikskunjungan[i][sementara[indeks-1]] = 0
                                else: # belok ke bawah
                                    # reset ke atas
                                    for i in range (sementara[indeks-2]+1,sementara[indeks]+1):
                                        matrikskunjungan[i][sementara[indeks-1]] = 0
                            else:
                                for i in range (baris):
                                    matrikskunjungan[i][kolomawal] = 0
                    if len(matriksbelokan[indeks]) != 0: # masih ada pilihan lagi
                        sudahakhir = False # reset karena masih ada pilihan jadi jatuhnya ke "anggap sebagai rute"

        elif indeks % 2 != 0: # indeks ganjil -> gerakan horizontal (kolom ke berapa) -> cek
            if len(matriksbelokan[indeks]) == 0: # mau diisi
                if indeks == buffer: # panjang sudah maksimal
                    indeks -= 1 # balik ke indeks sebelumnya
                    sudahakhir = True # sudah terakhir
                else: # masih bisa ditambahkan
                    # cari dulu
                    if indeks == 1: # data tidak ada di array sementara
                        temp = kolomawal
                    else: # ada di array sementara
                        temp = sementara[indeks-2]

                    # cek horizontal untuk pilihan
                    batasatas = temp # sejauh mana bisa diambil ke atas (ditambah)
                    batasbawah = temp # sejauh mana bisa diambil ke bawah (dikurang)
                    # gerakan horizontal (kolom)
                    print_array(sementara)
                    # gerakan vertikal (baris)
                    while True:  # selama g ada halangan
                        if batasatas >= baris:
                            if batasbawah < 0:  # tidak memenuhi
                                break
                        else:
                            # Check the range of the index before accessing the list
                            if 0 <= sementara[indeks-1] < baris and 0 <= batasatas < kolom and matrikskunjungan[batasatas][sementara[indeks-1]] != 1:
                                batasatas += 1
                                matriksbelokan[indeks].append(batasatas)

                            if 0 <= sementara[indeks-1] < kolom and matrikskunjungan[batasbawah][sementara[indeks-1]] != 1 and batasbawah >= 0:
                                batasbawah -= 1
                                matriksbelokan[indeks].append(batasbawah)

                    # tergantung panjangnya dilihat mentok atau tidak
                    if len(matriksbelokan[indeks]) == 0: # tidak ada kemungkinan lagi
                        indeks -= 1
                        sudahakhir = True
                    else: # ada pilihan
                        indeks += 1
                        sementara.append(matriksbelokan[indeks][len(matriksbelokan[indeks])-1])
                    
                    # pengecekan nilai
                    arraykoordinat = array_to_array_of_coordinate(sementara)
                    hadiah = hitung_hadiah(arraykoordinat,matriks,arrsekuens,hadiahsekuens)
                    if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                        jawaban = arraykoordinat
                        solusi = array_to_string(arraykoordinat)
                    nilai = 0 # reset

            else: # sudah diisi (msh ada yang blm dikunjungi)
                if not sudahakhir: # bukan terakhir -> dipilih sebagai rute saja (ditandai)
                    temp = matriksbelokan[indeks][len(matriksbelokan[indeks])-1]
                    sementara[indeks] = temp # update ke array temp
                    # pengecekan nilai
                    arraykoordinat = array_to_array_of_coordinate(sementara)
                    hadiah = hitung_hadiah(arraykoordinat,matriks,arrsekuens,hadiahsekuens)
                    if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                        jawaban = arraykoordinat
                        solusi = array_to_string(arraykoordinat)
                    nilai = 0 # reset
                    # label yang sudah dilewati
                    if indeks == 1: # sebelumnya dari baris 0 (data blm ada di array sementara)
                        if temp > kolomawal: # kanan
                            awal = kolomawal
                        elif temp < kolomawal: # kiri
                            awal = temp
                    else: # datanya ada di array sementara
                        if temp > sementara[indeks-2]: # kanan
                            awal = sementara[indeks-2]
                        elif temp < sementara[indeks-2]: # kiri
                            awal = temp
                    for i in range (awal,temp+1): # kecil ke besar
                        matriksbelokan[sementara[indeks-1]][i] = 1 # label dikunjungi
                    indeks += 1
                else: # sudah mentok (indeks yang ditelusuri sudah terakhir)
                    # habiskan semua pilihan indeks terakhir
                    while len(matriksbelokan[indeks]) != 0:
                        # pengecekan nilai
                        arraykoordinat = array_to_array_of_coordinate(sementara)
                        hadiah = hitung_hadiah(arraykoordinat,matriks,arrsekuens,hadiahsekuens)
                        if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                            jawaban = arraykoordinat
                            solusi = array_to_string(arraykoordinat)
                        nilai = 0 # reset
                        # pop elemen
                        matriksbelokan[indeks].pop()

                    # reset pengunjungan
                    # ganjil
                    if indeks != 1:
                        if sementara[indeks-2] > sementara[indeks]: # belok ke kiri
                            # reset ke kanan
                            for i in range (sementara[indeks],sementara[indeks-2]):
                                matrikskunjungan[sementara[indeks-1]][i] = 0
                        else: # belok ke kanan
                            # reset ke kiri
                            for i in range (sementara[indeks-2]+1,sementara[indeks]+1):
                                matrikskunjungan[sementara[indeks-1]][i] = 0
                    else:
                        if kolomawal > sementara[indeks]: # belok ke kiri
                            # reset ke kanan
                            for i in range (sementara[indeks],kolomawal):
                                matrikskunjungan[sementara[indeks-1]][i] = 0
                        else: # belok ke kanan
                            # reset ke kiri
                            for i in range (kolomawal+1,sementara[indeks]+1):
                                matrikskunjungan[sementara[indeks-1]][i] = 0

                    sementara.pop() # hapus juga nilai di sementara
                    while len(matriksbelokan[indeks]) == 0: # cari sampai tidak kosong
                        indeks -= 1
                        sementara.pop()
                        matriksbelokan[indeks].pop() # hapus indeks sebelumnya yang dipakai sebagai rute
                        # reset pengunjungan
                        if indeks % 2 != 0:
                            # ganjil
                            if indeks != 1:
                                if sementara[indeks-2] > sementara[indeks]: # belok ke kiri
                                    # reset ke kanan
                                    for i in range (sementara[indeks],sementara[indeks-2]):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                                else: # belok ke kanan
                                    # reset ke kiri
                                    for i in range (sementara[indeks-2]+1,sementara[indeks]+1):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                            else:
                                if kolomawal > sementara[indeks]: # belok ke kiri
                                    # reset ke kanan
                                    for i in range (sementara[indeks],kolomawal):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                                else: # belok ke kanan
                                    # reset ke kiri
                                    for i in range (kolomawal+1,sementara[indeks]+1):
                                        matrikskunjungan[sementara[indeks-1]][i] = 0
                        else:
                            # genap
                            if indeks != 0:
                                if sementara[indeks-2] > sementara[indeks]: # belok ke atas
                                    # reset ke bawah
                                    for i in range (sementara[indeks],sementara[indeks-2]):
                                        matrikskunjungan[i][sementara[indeks-1]] = 0
                                else: # belok ke bawah
                                    # reset ke atas
                                    for i in range (sementara[indeks-2]+1,sementara[indeks]+1):
                                        matrikskunjungan[i][sementara[indeks-1]] = 0
                            else:
                                for i in range (baris):
                                    matrikskunjungan[i][kolomawal] = 0
                    if len(matriksbelokan[indeks]) != 0: # masih ada pilihan lagi
                        sudahakhir = False # reset karena masih ada pilihan jadi jatuhnya ke "anggap sebagai rute"
        # hasil
        print("Nilai maksimal = ",hadiah)
        print("Solusi =",solusi)
        print("Array koordinat =",end=" ")
        print_array(jawaban)
    # pengembalian dan penambahan nilai
    kolomawal += 1
    indeks = 0
    sudahakhir = False
    sementara = []
    matrikskunjungan = [[0 for i in range(baris)] for j in range (kolom)]
    matriksbelokan = [[] for i in range (buffer+1)]