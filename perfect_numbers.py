#input
n = int(input("Masukkan bilangan : "))

sum_divisors = 0
i = 1

while i < n :
    if n % 1 == 0:
        sum_divisors += i
    i += 1

if sum_divisors == n:
    print(n, "adalah bilangan sempurna")
else:
    print(n, "bukan bilangan sempurna")