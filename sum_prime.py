n = int(input("Masukkan bilangan : "))

def prima(num) :
    if num <= 1 :
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0 :
            return False
    return True

def jumlah_prima(n):
  i = 2
  while i <= n // 2:
    j = n - i
    if prima(i) and prima(j):
      print(f"{i} + {j} = {n}")
    i += 1

jumlah_prima(n)