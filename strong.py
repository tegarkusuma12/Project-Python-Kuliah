n = int(input("Masukkan : "))

nums = list(map(int, str(n)))
sum = 0
for i in nums:
    factorial = 1
    for j in range(i, 0, -1):
        factorial *= j
    sum += factorial

if sum == n:
    print(f"{n} bilangan strong")
else:
    print(f"{n} bukan bilangan strong.")