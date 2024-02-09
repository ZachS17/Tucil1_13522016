# matriks
# array untuk urutan baru concatenate dan match string dengan sekuens concatenated (is in)
# batasan kolom n+1 untuk setiap baris (horizontal)
# batasan baris n+1 untuk setiap kolom (vertical)
# cari satu-satu solusi
# selama belum ketemu dan masih ada pilihan
# catat perlunya gerakan horizontal atau vertikal karena selang-seling
# optimal = dimulai dari baris 1 dan kolom 1 naik kolom kemudian baris

# urutan harus dari jumlah sekuens minimum karena mencari solusi "optimal"
# ide : dimulai dari belokan 1 langkah sesuai ketentuan

# input matriks
import string

baris = int(input("Jumlah baris: "))
kolom = int(input("Jumlah kolom: "))

matrix = []

for i in range(baris):
    row = []
    for j in range(kolom):
        element = string(input(f"Enter the element at position ({i + 1}, {j + 1}): "))
        row.append(element)
    matrix.append(row)

# inputan dan inisialisasi nilai
buffer = int(input("Jumlah buffer (paling banyak disusun): "))
jsekuens = int(input("Jumlah sekuens (string kode untuk hadiah): "))
arrsekuens = [] # array dari sekuens yang diperbolehkan
hadiahsekuens = [] # array dari hadiah yang bertepatan dengan array sekuens
for i in range(jsekuens): # masukan sekuens dan hadiahnya
    sekuens = string(input("Sekuens ",i+1,": "))
    arrsekuens.append(sekuens)
    hadiah = int(input("Hadiah sekuens ",i+1,": "))
    hadiahsekuens.append(hadiah)
kolomawal = 1 # kolom yang ditelusuri awal (1-kolom)
jawaban = [] # array koordinat dari nilai paling besar
terbesar = 0 # nilai total jumlah terbesar (solusi optimal sementara)
solusi = "" # hasil string langsung
nilai = 0 # nilai total yang sedang ditelusuri
arah = "vertikal"
panjang = 0

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

# # proses
# while panjang <= buffer: # dari kombinasi sekuens paling sedikit (1-buffer)
#     ikolom = 0 # indeks kolom yang ditelusuri
#     jbaris = 0 # indeks baris yang ditelusuri
#     panjangsekarang = 0 # panjang string yang dikombinasi (dimulai dari panjang paling pendek supaya solusi sependek mungkin)
#     # ganjil genap beda harus dicek awal supaya g 2 kali
#     while panjangsekarang != panjang: # cari ekor terpanjang, terawal dulu
#         if panjangsekarang % 2 != 0: # ganjil maka akhirnya gerakan horizontal
#             jawaban.append([i,j])
#         else: # genap maka akhirnya gerakan vertikal
#             jawaban.append[]
#     while ikolom <= kolom: # kondisi awal blm ketemu dan kolom habis

#         # sementara = ""
#         # jawaban.append((1,ikolom)) # masukin kode awal
#         # while len(jawaban) <= buffer: # selama panjang yang ditelusuri lebih kecil dan belum ketemu
#         #     # vertikal
#         #     jawaban.append((ibaris,ikolom))
#         #     sementara += jawaban[len(jawaban)-1] # kode dengan spasi

#         #     # perhitungan
#         #     for i in range (arrsekuens):
#         #         nilai += hitung_kemunculan(jawaban,arrsekuens[i]) * hadiahsekuens[i]
                
#         #     if nilai > terbesar:
#         #         solusi = sementara
#         #         terbesar = nilai

#         #     # tambahan cek kasus
#         #     if len(jawaban) > buffer:
#         #         break

#         #     # horizontal
#         #     jawaban.append(())
#         #     sementara += jawaban[len(jawaban)-1] # kode dengan spasi


#         #     # perhitungan
#         #     for i in range (arrsekuens):
#         #         nilai += hitung_kemunculan(jawaban,arrsekuens[i]) * hadiahsekuens[i]
                
#         #     if nilai > terbesar:
#         #         solusi = sementara
#         #         terbesar = nilai
#         ikolom += 1
#     panjang += 1

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