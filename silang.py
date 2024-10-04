n = int(input("Masukkan angka : "))
char = str(input("masukkan karakter : "))

for i in range(1,n):
    for j in range(1,n):
        if i == 1 or j == 1 and i == n or j == n :
            print(char, end=" ")
    print()