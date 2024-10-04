def input_nilai(jenis_nilai):
        while True:
            nilai = int(input(f"Masukkan nilai {jenis_nilai} (0-100): "))
            if 0 <= nilai <= 100:
                return nilai
            else:
                print("Nilai tidak valid. Masukkan nilai antara 0 dan 100.")

def input_bobot():
    while True:
        bobot_tugas = float(input("Masukkan bobot nilai Tugas (0-100): "))
        bobot_uts = float(input("Masukkan bobot nilai UTS (0-100): "))
        bobot_uas = float(input("Masukkan bobot nilai UAS (0-100): "))
        if 0 <= bobot_tugas <= 100 and 0 <= bobot_uts <= 100 and 0 <= bobot_uas <= 100 and bobot_tugas + bobot_uts + bobot_uas == 100:
            return bobot_tugas, bobot_uts, bobot_uas
        else:
            print("Total bobot harus 100%. Silakan masukkan ulang.")

def hitung_nilai_akhir(tugas, uts, uas, bobot_tugas, bobot_uts, bobot_uas):
    nilai_akhir = (tugas * bobot_tugas/100) + (uts * bobot_uts/100) + (uas * bobot_uas/100)
    return nilai_akhir

while True:
    nilai_tugas = input_nilai("Tugas")
    nilai_uts = input_nilai("UTS")
    nilai_uas = input_nilai("UAS")
    bobot_tugas, bobot_uts, bobot_uas = input_bobot()

    nilai_akhir = hitung_nilai_akhir(nilai_tugas, nilai_uts, nilai_uas, bobot_tugas, bobot_uts, bobot_uas)
    print("Nilai akhir Anda adalah:", nilai_akhir)

    ulang = input("Apakah mau mengulangi? (y/n): ")
    if ulang != 'y':
        break






# def input_nilai(jenis_nilai):
#         nilai = int(input(f"Masukkan nilai {jenis_nilai} (0-100): "))
#         if 0 <= nilai <= 100:
#             return nilai
#         else:
#             print("Nilai tidak valid. Masukkan nilai antara 0 dan 100.")

# def input_bobot():
#     while True:
#         bobot_tugas = float(input("Masukkan bobot nilai Tugas (0-100): "))
#         bobot_uts = float(input("Masukkan bobot nilai UTS (0-100): "))
#         bobot_uas = float(input("Masukkan bobot nilai UAS (0-100): "))
#         if 0 <= bobot_tugas <= 100 and 0 <= bobot_uts <= 100 and 0 <= bobot_uas <= 100 and bobot_tugas + bobot_uts + bobot_uas == 100:
#             return bobot_tugas, bobot_uts, bobot_uas
#         else:
#             print("Total bobot harus 100%. Silakan masukkan ulang.")

# def hitung_nilai_akhir(tugas, uts, uas, bobot_tugas, bobot_uts, bobot_uas):
#     nilai_akhir = (tugas * bobot_tugas/100) + (uts * bobot_uts/100) + (uas * bobot_uas/100)
#     return nilai_akhir

# while True:
#     tugas = input_nilai("Tugas")
#     uts = input_nilai("UTS")
#     uas = input_nilai("UAS")
#     bobot_tugas, bobot_uts, bobot_uas = input_bobot()

#     nilai_akhir = hitung_nilai_akhir(tugas, uts, uas, bobot_tugas, bobot_uts, bobot_uas)
#     print("Nilai akhir Anda adalah:", nilai_akhir)

#     ulang = input("Apakah mau mengulangi? (y/n): ")
#     if ulang != 'y':
#         break
