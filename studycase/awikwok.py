from datetime import datetime

# Inisialisasi variabel
penjualan_harian = []  # List untuk menyimpan data penjualan harian

def tambah_barang_terjual(hari, nama_barang, jumlah):
    """
    Menambahkan barang terjual ke dalam list penjualan harian.
    """
    penjualan_harian.append({"hari": hari, "nama_barang": nama_barang, "jumlah": jumlah})

def hitung_total_dan_rata_rata_penjualan():
    """
    Menghitung total penjualan barang dan rata-rata penjualan per hari.
    """
    if not penjualan_harian:
        return 0, {}

    total_penjualan = sum(item["jumlah"] for item in penjualan_harian)
    
    # Menghitung total dan jumlah penjualan per hari
    penjualan_per_hari = {}
    for item in penjualan_harian:
        hari = item["hari"]
        jumlah = item["jumlah"]

        if hari in penjualan_per_hari:
            penjualan_per_hari[hari]["total"] = penjualan_per_hari[hari]["total"] + jumlah
            penjualan_per_hari[hari]["jumlah_transaksi"] = penjualan_per_hari[hari]["jumlah_transaksi"] + 1
        else:
            penjualan_per_hari[hari] = {"total": jumlah, "jumlah_transaksi": 1}

    # Menghitung rata-rata penjualan per hari
    rata_rata_penjualan_per_hari = {hari: data["total"] / data["jumlah_transaksi"] for hari, data in penjualan_per_hari.items()}

    return total_penjualan, rata_rata_penjualan_per_hari

def tentukan_barang_terjual_terbanyak_dan_tersedikit():
    """
    Menentukan barang mana yang terjual terbanyak dan tersedikit.
    """
    if not penjualan_harian:
        return None, None
    
    jumlah_penjualan = {}
    for item in penjualan_harian:
        jumlah_penjualan[item['nama_barang']] = jumlah_penjualan.get(item['nama_barang'], 0) + item['jumlah']

    barang_terbanyak = max(jumlah_penjualan, key=jumlah_penjualan.get)
    barang_tersedikit = min(jumlah_penjualan, key=jumlah_penjualan.get)
    
    return barang_terbanyak, barang_tersedikit

# Contoh penggunaan
while True:
    hari = input("Hari penjualan (format YYYY-MM-DD): ")
    try:
        # Validasi format tanggal
        datetime.strptime(hari, "%Y-%m-%d")
    except ValueError:
        print("Masukkan tanggal yang valid dengan format YYYY-MM-DD.")
        continue

    nama_barang = input("Nama barang yang terjual: ")
    try:
        jumlah_barang = int(input("Jumlah barang yang terjual: "))
        if jumlah_barang <= 0:
            print("Jumlah barang harus lebih dari 0.")
            continue
    except ValueError:
        print("Masukkan jumlah barang yang valid.")
        continue

    tambah_barang_terjual(hari, nama_barang, jumlah_barang)

    sudah = input("Sudah? (y/n): ")
    if sudah.lower() == 'y':
        break
    elif sudah.lower() != 'n':
        print("Masukkan 'y' untuk selesai atau 'n' untuk menambah data lagi.")

total, rata_rata_per_hari = hitung_total_dan_rata_rata_penjualan()
barang_terbanyak, barang_tersedikit = tentukan_barang_terjual_terbanyak_dan_tersedikit()

print("\nPenjualan harian:", penjualan_harian)
print("Total penjualan:", total)
print("Rata-rata penjualan per hari:")
for hari, rata_rata in rata_rata_per_hari.items():
    print(f"{hari}: {rata_rata}")
print("Barang terjual terbanyak:", barang_terbanyak)
print("Barang terjual tersedikit:", barang_tersedikit)




