# Input dari pengguna
total_balok = int(input("Masukkan jumlah balok: "))

# Cek jika input negatif
if total_balok < 0:
    print("Jumlah balok tidak boleh negatif")
else:
    # Fungsi untuk menghitung tinggi piramida dan sisa balok
    def hitung_sisa_balok(total_balok):
        tinggi = 0
        sisa_balok = total_balok
        
        while sisa_balok >= (tinggi + 1):
            tinggi += 1
            jumlah_balok = tinggi
            sisa_balok -= tinggi
            print(f"Tingkat ke-{tinggi}: ada {jumlah_balok} balok sisa {sisa_balok} balok")
        
        return tinggi, sisa_balok

    # Menghitung tinggi dan sisa balok
    tinggi, sisa_balok = hitung_sisa_balok(total_balok)

    # Output hasil
    print(f"Tinggi piramida adalah {tinggi}, sisa balok {sisa_balok}")



