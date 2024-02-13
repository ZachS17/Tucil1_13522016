def find_max_reward_path(buffer, baris, kolom, matriks, jsekuens, arrsekuens, hadiahsekuens):
    def hitung_kemunculan_satu_sekuens(main, sub):
        jumlah = 0
        indeks = 0

        while True:
            index = main.find(sub, indeks)

            if index == -1:
                break

            jumlah += 1
            indeks = index + 1

        return jumlah

    def print_array(array):
        for i in range (len(array)):
            print(array[i],end=" ")

    def hitung_hadiah(array, matriks, arrsekuens, arrhadiah):
        kata = ''
        for i in range(len(array)):
            if array[i][0] < len(matriks) and array[i][1] < len(matriks[0]):
                kata = kata + matriks[array[i][0]][array[i][1]] + " "
            else:
                print("Index out of range:", array[i])
        hadiah = 0
        for i in range(len(arrsekuens)):
            hadiah += (hitung_kemunculan_satu_sekuens(kata, arrsekuens[i]) * arrhadiah[i])
        return hadiah



    def is_valid_move(x, y, buffer, matrikskunjungan):
        return 0 <= x < baris and 0 <= y < kolom and matrikskunjungan[x][y] == 0
    
    def array_to_string(array,matriks):
        kata = ''
        for i in range (len(array)):
            kata = kata + matriks[array[i][0]][array[i][1]] + " "
        return kata
    
    def array_to_array_of_coordinate(array): 
        arraykoordinat = [[1, array[0][0] + 1]]  # elemen pertama dalam array
        i = 1
        while i + 1 != len(array):
            if i % 2 == 0:  # genap -> angka kolom
                arraykoordinat.append([array[i + 1][0] + 1, array[i][0] + 1])
            else:  # ganjil -> angka baris
                arraykoordinat.append([array[i][0] + 1, array[i + 1][0] + 1])
            i += 1
        return arraykoordinat


    def backtrack(x, y, indeks, sementara, matrikskunjungan):
        nonlocal nilai, jawaban, solusi

        if indeks == buffer:
            arraykoordinat = array_to_array_of_coordinate(sementara)
            hadiah = hitung_hadiah(arraykoordinat, matriks, arrsekuens, hadiahsekuens)

            if nilai > hadiah and len(arraykoordinat) < len(jawaban):
                jawaban = arraykoordinat
                solusi = array_to_string(arraykoordinat)

            nilai = 0
            return

        # Iterate over possible moves (up, down, left, right)
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for move in moves:
            next_x, next_y = x + move[0], y + move[1]

            if is_valid_move(next_x, next_y, buffer, matrikskunjungan):
                matrikskunjungan[next_x][next_y] = 1
                sementara.append((next_x, next_y))
                backtrack(next_x, next_y, indeks + 1, sementara, matrikskunjungan)
                matrikskunjungan[next_x][next_y] = 0
                sementara.pop()

    # Initialize variables
    kolomawal = 0
    indeks = 0
    sementara = []
    matrikskunjungan = [[0 for _ in range(baris)] for _ in range(kolom)]
    jawaban = [1 for _ in range(buffer)]
    solusi = ""
    nilai = 0

    # Main loop
    while kolomawal < kolom:
        for i in range(baris):
            matrikskunjungan[i][kolomawal] = 1
            sementara.append((i, kolomawal))
            backtrack(i, kolomawal, indeks + 1, sementara, matrikskunjungan)
            matrikskunjungan[i][kolomawal] = 0
            sementara.pop()

        kolomawal += 1

    # Print results
    print("Nilai maksimal =", nilai)
    print("Solusi =", solusi)
    print("Array koordinat =", end=" ")
    print_array(jawaban)


# Example usage
with open('input.txt', 'r') as file:
    lines = file.readlines()

i = 0
buffer = int(lines[0].strip())
baris, kolom = map(int, lines[1].split())
i += 1
matriks = [lines[i + 2].split() for i in range(baris)]
i += baris
jsekuens = lines[2 + baris].strip()
arrsekuens = [lines[i + 3 + baris].strip() for i in range(int(jsekuens))]
hadiahsekuens = [int(token.strip(), 16) for token in lines[i].split()]

find_max_reward_path(buffer, baris, kolom, matriks, jsekuens, arrsekuens, hadiahsekuens)
