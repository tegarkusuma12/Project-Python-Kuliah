print("Program untuk memisahlkan kata dari input user berdasarkan delimiter.")

kalimat = str(input("Masukkan kalimat : "))
delimiter  = str(input("Masukkan delimiter : "))

kalimat += delimiter  # Tambahkan delimiter di akhir kalimat
list_kata = []
kata_sementara = ""

for karakter in kalimat:
    if karakter != delimiter:  # Jika bukan delimiter, tambahkan ke kata_sementara
        kata_sementara += karakter
    else:  # Jika delimiter ditemukan, tambahkan kata ke list_kata
        if kata_sementara:  # Pastikan kata_sementara tidak kosong sebelum ditambahkan
            list_kata.append(kata_sementara)
            kata_sementara = ""  # Reset kata_sementara

print(list_kata)
