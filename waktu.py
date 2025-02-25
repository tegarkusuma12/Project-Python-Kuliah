x = int(input("Masukkan jarak dalam kilometer = "))

y = int(input("Masukkan kecepatan rata-rata dalam km/jam = "))

def waktu(x, y):
    waktu_tempuh = x / y
    print(f"Jarak {x}km")
    print(f"Kecepatan {y}km/jam")
    print(f"Waktu sebenarnya {waktu_tempuh}")
    return waktu_tempuh

hasil = waktu(x, y)

jam = int(hasil)
menit = int((hasil - jam) * 60)

print("Waktu tempuh : ", jam , "jam", menit , "menit")
