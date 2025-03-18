# Tugas 2
# Membuat matriks identitas 3x3
ukuran = 3
matriks_identitas = [[1 if i == j else 0 for j in range(ukuran)] for i in range(ukuran)]
print(matriks_identitas)

# biasa
ukuran = 3
matriks_identitas = []
for i in range(ukuran):
    baris = []
    for j in range(ukuran):
        if i == j:
            baris.append(1)
        else:
            baris.append(0)
    matriks_identitas.append(baris)

print(matriks_identitas)

