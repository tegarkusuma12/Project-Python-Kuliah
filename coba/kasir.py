# Inisialisasi daftar barang sebagai list
daftar_barang = []

# Fungsi untuk menambahkan barang dan harga
def tambah_barang():
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga barang: "))
    daftar_barang.append((nama_barang, harga))
    print(f'Barang "{nama_barang}" dengan harga {harga} berhasil ditambahkan.\n')
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk menghapus data barang
def hapus_barang():
    nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
    for i, (nama, harga) in enumerate(daftar_barang):
        if nama == nama_barang:
            del daftar_barang[i]
            print(f'Barang "{nama_barang}" berhasil dihapus.\n')
            break
    else:
        print(f'Barang "{nama_barang}" tidak ditemukan.\n')
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk menghitung total harga barang yang dibeli
def hitung_total_harga():
    total = sum(harga for nama, harga in daftar_barang)
    print(f'Total harga barang yang dibeli adalah: {total}\n')
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi untuk menampilkan daftar barang
def tampilkan_barang():
    if daftar_barang:
        print("Daftar barang yang dibeli:")
        for nama, harga in daftar_barang:
            print(f'- {nama}: {harga}')
    else:
        print("Belum ada barang yang dibeli.\n")
    input("Tekan Enter untuk kembali ke menu...")

# Fungsi utama untuk menampilkan menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Tambah barang")
        print("2. Hapus barang")
        print("3. Tampilkan total harga")
        print("4. Lihat daftar barang")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            hapus_barang()
        elif pilihan == '3':
            hitung_total_harga()
        elif pilihan == '4':
            tampilkan_barang()
        elif pilihan == '5':
            print("Terima kasih telah berbelanja di toko kami!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

menu()

