while True:
    try :
        n = int(input("Masukkan jumlah : "))
        break
    except ValueError:
        print("Masukkan integer")
        continue

def encrypt_name(name):
    vowels = "AEIOUaeiou"  
    return ''.join(['*' if char in vowels else char for char in name])

def longest_and_shortest_work_time(people, pensi):
    # Menghitung waktu kerja untuk pekerja yang belum pensiun
    work_years = {name: pensi - age for name, age in people.items() if age < pensi}

    if not work_years:  # Jika semua pekerja sudah pensiun
        return None, None

    # Mencari waktu kerja terpanjang dan terpendek
    max_time = max(work_years.values())
    min_time = min(work_years.values())

    # Mencari pekerja dengan waktu kerja terpanjang dan terpendek
    longest_workers = [name for name, years in work_years.items() if years == max_time]
    shortest_workers = [name for name, years in work_years.items() if years == min_time]

    return longest_workers, shortest_workers

people = {input("Masukkan nama orang: "): int(input("Masukkan umur: ")) for _ in range(n)}
print(people)
pensi = int(input("Masukkan umur pensiun : "))

# for name, age in people:
#     if age >= pensi:
#         print(f"{name} sudah pensiun")
#     else:
#         sisa = pensi - age
#         print(f"{name} kurang {sisa} tahun lagi untuk pensiun")

work_years = {name: pensi - age for name, age in people.items() if age < pensi}

max_year = max(work_years.values())
longest_worker = [encrypt_name(name) for name, years in work_years.items() if years == max_year]
print(f"Yang paling lama adalah {','.join(longest_worker)} : {max_year}")

min_year = min(work_years.values())
shortest_worker = [encrypt_name(name) for name, years in work_years.items() if years == min_year]
print(f"Yang paling lama adalah {','.join(shortest_worker)} : {min_year}")