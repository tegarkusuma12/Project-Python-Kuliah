n = int(input("Masukkan tinggi segitiga : "))
if n < 0:
    print("Tidak boleh negatif")
char = str(input("Masukkan karakter yang diinginkan : "))

for i in range(n, 0, -1):
    print(char * n)
    n -=1
    
# i = 0
# while i < n:
#     print(char * n)
#     n -=1