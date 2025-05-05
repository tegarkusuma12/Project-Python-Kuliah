import re

while True:
    try:
        file = str(input("Masukkan nama file yang ingin dibaca: "))

        match = re.search(r"\.log$", file)

        if not match:
            print(f"File {file} bukan merupakan file log")
            continue
        else:
            directory = r"C:\Users\ASUS\OneDrive\Belajar-Ngoding\Belajar-py"
            open(directory + "\\"+ file, "r").close()
            print(f"File '{file}' berhasil dibaca.")
            break
    except ValueError:
         print("ValueError")
    except FileNotFoundError:
        print(f"File '{file}' tidak  ditemukan")

print("\nDaftar aktivitas yang ditemukan")
with open(file, "r") as file:
    data = file.read()

pattern = r'@\w+\s([a-z ]+)'
hasil = re.findall(pattern, data)
for n, i in enumerate(hasil):
    print(f"{n+1}. {i}")

print("\nSimpan hasil ke dalam file")
hasil_set = set(hasil)
with open("log.txt", "w") as file:
    for n, i in enumerate(hasil_set):
        tulis = f"{n+1}. {i} : {hasil.count(i)}\n"
        file.write(tulis)
print("File log.txt berhasil dibuat")
