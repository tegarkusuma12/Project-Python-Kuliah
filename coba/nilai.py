def input_nilai_mahasiswa():
    # Membuat dictionary kosong untuk menyimpan nama dan nilai mahasiswa
    mahasiswa = {}
    
    # Loop untuk terus meminta input sampai pengguna mengetik 'selesai'
    while True:
        nama = input("Masukkan nama mahasiswa (atau ketik 'selesai' untuk mengakhiri): ")
        
        # Jika pengguna mengetik 'selesai', loop berhenti
        if nama == 'selesai':
            break
        
        # Meminta input nilai dan mengubahnya menjadi angka desimal
        nilai = float(input(f"Masukkan nilai untuk {nama}: "))
        
        # Menyimpan nama dan nilai mahasiswa dalam dictionary
        mahasiswa[nama] = nilai
    
    # Mengembalikan data mahasiswa yang sudah dimasukkan
    return mahasiswa

def tampilkan_hasil(mahasiswa):
    # Jika tidak ada data mahasiswa, langsung keluar dari fungsi
    if not mahasiswa:
        print("Tidak ada data mahasiswa.")
        return
    
    # Menghitung total nilai dan rata-rata
    total_nilai = sum(mahasiswa.values())
    rata_rata = total_nilai / len(mahasiswa)
    
    # Mencari nilai tertinggi dan terendah
    tertinggi = max(mahasiswa.values())
    terendah = min(mahasiswa.values())
    
    # Menampilkan hasil nilai semua mahasiswa
    print("\nDaftar Nilai Mahasiswa:")
    for nama, nilai in mahasiswa.items():
        print(f"{nama}: {nilai}")
    
    # Menampilkan rata-rata, nilai tertinggi, dan terendah
    print(f"\nRata-rata nilai: {rata_rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
    
    # Menampilkan mahasiswa dengan nilai di atas rata-rata
    print("\nNilai yang lebih tinggi dari rata-rata:")
    for nama, nilai in mahasiswa.items():
        if nilai > rata_rata:
            print(f"{nama}: {nilai}")

# Bagian utama program
mahasiswa = input_nilai_mahasiswa()
tampilkan_hasil(mahasiswa)
