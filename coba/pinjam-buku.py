from datetime import datetime

# Daftar buku yang dipinjam
peminjaman = []

# Fungsi utama untuk mengelola peminjaman
def kelola_buku(aksi, nama_anggota=None, judul_buku=None, tanggal=None):
    if aksi == 'tambah':
        peminjaman.append({
            'nama_anggota': nama_anggota,
            'judul_buku': judul_buku,
            'tanggal_pinjam': datetime.strptime(tanggal, "%Y-%m-%d"),
            'tanggal_kembali': None
        })
        print(f"Buku '{judul_buku}' berhasil dipinjam oleh {nama_anggota}.")
    
    elif aksi == 'kembali':
        for buku in peminjaman:
            if buku['nama_anggota'] == nama_anggota and buku['judul_buku'] == judul_buku:
                buku['tanggal_kembali'] = datetime.strptime(tanggal, "%Y-%m-%d")
                denda = hitung_denda(buku['tanggal_pinjam'], buku['tanggal_kembali'])
                print(f"Buku '{judul_buku}' telah dikembalikan oleh {nama_anggota}. Denda: Rp {denda}")
                peminjaman.remove(buku)
                return
        print(f"Buku '{judul_buku}' oleh {nama_anggota} tidak ditemukan di daftar peminjaman.")
    
    elif aksi == 'lihat':
        if not peminjaman:
            print("Tidak ada buku yang sedang dipinjam.")
        else:
            print("Daftar Buku yang Sedang Dipinjam:")
            for buku in peminjaman:
                print(f"{buku['nama_anggota']} meminjam '{buku['judul_buku']}' sejak {buku['tanggal_pinjam'].strftime('%Y-%m-%d')}.")
    
# Fungsi untuk menghitung denda
def hitung_denda(tanggal_pinjam, tanggal_kembali):
    batas_hari_pinjam = 7  # Batas peminjaman adalah 7 hari
    biaya_denda_per_hari = 1000  # Denda keterlambatan per hari
    lama_pinjam = (tanggal_kembali - tanggal_pinjam).days
    if lama_pinjam > batas_hari_pinjam:
        return (lama_pinjam - batas_hari_pinjam) * biaya_denda_per_hari
    return 0

# Fungsi untuk meminta input dari pengguna
def input_pengguna():
    while True:
        print("\n--- Menu ---")
        print("1. Pinjam buku")
        print("2. Kembalikan buku")
        print("3. Lihat buku yang sedang dipinjam")
        print("4. Keluar")
        pilihan = input("Pilih aksi (1-4): ")

        if pilihan == '1':
            nama_anggota = input("Masukkan nama anggota: ")
            judul_buku = input("Masukkan judul buku: ")
            tanggal_pinjam = input("Masukkan tanggal peminjaman (YYYY-MM-DD): ")
            kelola_buku('tambah', nama_anggota, judul_buku, tanggal_pinjam)
        elif pilihan == '2':
            nama_anggota = input("Masukkan nama anggota: ")
            judul_buku = input("Masukkan judul buku: ")
            tanggal_kembali = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ")
            kelola_buku('kembali', nama_anggota, judul_buku, tanggal_kembali)
        elif pilihan == '3':
            kelola_buku('lihat')
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Jalankan program
input_pengguna()

