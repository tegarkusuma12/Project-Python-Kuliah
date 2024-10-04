def jumlah_hari(bulan,tahun):
    if bulan == 2 :
        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0): #Kabisat
            return 29
        else:
            return 28
    else :
        if bulan in [4, 6, 9, 11] : #April, Juni, September, Oktober
            return 30
        else :
            return 31

def bulan_apa(bulan):
   list_bulan = [ #Array 0-11
       "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
   ]
   if 1 <= bulan <= 12:
       return list_bulan[bulan - 1] #karena array dimulai dari 0
   else :
       print("Apalah")

while True:
    bulan = int(input("Masukkan bulan (angka) : "))
    if bulan < 1 or bulan > 12:
        print("Bulan harus 1-12")
    else:
        break

while True:
    tahun = int(input("Masukkan tahun (Masehi): "))
    if tahun <= 0 :
        print("Tahun minimal 1 masehi")
    else:
        break

hari = jumlah_hari(bulan, tahun)
nama_bulan = bulan_apa(bulan)
print(f"Jumlah hari pada bulan {nama_bulan} pada tahun {tahun} adalah {hari}")
        
    