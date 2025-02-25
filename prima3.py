def prime(n):
    lst = []
    i = 2
    while i <= n:
        is_prime = True
        for j in range(2,i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            lst.append(i)
        i += 1
    print(f"Menampilkan bilangan prima sebanyak {n} : {lst}")        

while True :
    try:
        n = int(input("Masukkan jumlah : "))
        break
    except ValueError:
        print("Apalah")
        continue

prime(n)