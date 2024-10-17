while True:
    try :
        rentang = int(input("Masukkan rentang : "))
        break
    except ValueError:
        print("Apalah")
        continue

list_prima = []
for i in range(2, rentang):
    prima = True
    for j in range(2, i):
      if i % j == 0:
        prima = False
        break
    if prima:
      list_prima.append(i)

print(f"Bilangan prima dalam rentang 1 s.d {rentang} adalah {list_prima}")