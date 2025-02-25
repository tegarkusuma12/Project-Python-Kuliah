def enkripsi(nama):
    vokal = "AIUEOaiueo"
    return ''.join(['*' if char in vokal else char for char in nama])

list_nama = []
list_umur = []

n = int(input("Masukkan jumlah pekerja : "))
for i in range(1, n + 1):
    print(f"pekerja ke-{i}")
    
    while True:
        nama = str(input("Nama : "))
        if nama.isalpha() == True:
            list_nama.append(nama)
            break
        else:
            print("[Warning] Nama hanya boleh mengandung karakter alfbet")
            continue
            
    while True:
        umur = str(input("Umur : "))
        if umur.isalnum() == True:
            if umur in range(21,66):
                list_umur.append(umur)
                break
            else:
                print("[Warning] Usia pekerja 21-65")
                continue
        else:
            print("[Warning] Usia hanya boleh digit")
            continue

lama = [65 - x for x in list_umur]
bonus = [i*1000000 for i in lama]

print("Daftar Karyawan")
for i in range(1,n):
    print(f"{i}. {enkripsi(list_nama[i])} dengan usia {list_umur[i]} akan mendapat bonus sebesar Rp.{bonus[i]} ketika pensiun")

print(f"Bonus terbesar yabg akan diterima karyawan adalah {bonus.max()}")

            