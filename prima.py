# Masukkan pada variable a
a = int(input("Masukkan bilangan: "))

prima = a > 1  # Asumsikan prima(true) jika a lebih dari 1

# perulangkan sebanyak variable i diamana i berisi deret dengan rentang 2 sampai a akar 2 ditambah 1
for i in range(2, int(a**0.5) + 1): 
    if a % i == 0: # jika a habis dibagi i
        prima = False # kembalikan nilai bukan prima
        break # stop perulangan 
if prima:
    # output jika prima(true)
    print(a, "adalah bilangan prima") 
else:
    # output bukan prima(false)
    print(a, "bukan bilangan prima")
