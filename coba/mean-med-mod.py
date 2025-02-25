# Program digunakan untuk menghitung rata-rata dari data yang ada
def RataRata(angka):
    rata_rata = sum(angka)/len(angka)
    print('Hasil Rata-Ratanya adalah:',rata_rata)

def SortMedian(angka):
    # Sort
    angka.sort()
    print('Hasil Pengurutan Angka adalah:',angka)
    # Median
    n = len(angka)
    if n % 2 == 0:
        median = (angka[n//2-1]+angka[n//2])/2
        print('Mediannya adalah:',median)
    else:
        median = (angka[n//2])
        print('Mediannya adalah:',median)
# 

# def Modus(angka):
#     modus = 0
#     frekuensi_terbanyak = 0

#     for elemen in angka:
#         frekuensi = angka.count(elemen)  
        
#         if frekuensi > frekuensi_terbanyak:
#             frekuensi_terbanyak = frekuensi
#             modus = elemen
            
#     print('Modusnya adalah:',modus)
# # 

def Modus(angka):
    modus = []
    frekuensi_terbanyak = 0

    for elemen in angka:
        frekuensi = angka.count(elemen)
        if frekuensi > frekuensi_terbanyak:
            frekuensi_terbanyak = frekuensi
            modus = [elemen]
        elif frekuensi == frekuensi_terbanyak:
            modus.append(elemen)

    if len(modus) == len(angka):
        print("Tidak ada modus yang unik.")
    else:
        print("Modusnya adalah:", modus)

list_angka = []
indeks = 1
jumlah_angka = int(input('Jumlah Angka Yang diinginkan: '))

while indeks <= jumlah_angka:
    angka = int(input(f'Masukkan Angka ke-{indeks}: ')) 
    list_angka.append(angka)
    indeks += 1

RataRata(list_angka)
SortMedian(list_angka)
Modus(list_angka)
