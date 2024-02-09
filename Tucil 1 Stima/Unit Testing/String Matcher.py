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

jumlah = hitung_kemunculan_satu_sekuens("alalala","ala")
print(jumlah)