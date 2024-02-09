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