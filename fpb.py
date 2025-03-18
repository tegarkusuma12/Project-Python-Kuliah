a = int(input("Masukkan nilai a: "))
b = int(input("Masukkan nilai b: "))

# Mencari bilangan terkecil
if a > b:
    mini = b
else:
    mini = a

# Mulai dari bilangan terkecil hingga 1
for i in range(mini, 0, -1):
    if a % i == 0 and b % i == 0:
        fpb = i
        break

print("FPB dari", a, "dan", b, "adalah", fpb)