tinggi = int(input("Masukkan tinggi segiempat: "))
lebar = int(input("Masukkan lebar segiempat: "))
char = str(input("Masukkan karakter: "))

for i in range(tinggi):
    if i == 0 or i == tinggi - 1:
        print(char * lebar, sep=" ")
    else:
        print(f"{char}{' ' * (lebar - 2)}{char}")


# for i in range(tinggi):
#     for j in range(lebar):
#         if i == 0 or i == tinggi-1 or j == 0 or j == lebar-1 :
#             print(char, end=" ")
#         else:
#             print(" ")
    