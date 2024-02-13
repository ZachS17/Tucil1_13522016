import string

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

print(len(matrix),"baris")
print(len(matrix[0]),"kolom")