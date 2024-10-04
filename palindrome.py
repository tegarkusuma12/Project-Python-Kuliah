while True:
    try:
        kata = str(input("Masukkan kata :"))
        break
    except ValueError:
        print("Apalah")
        continue

palindrome = True
for i in range(len(kata) // 2):
    if kata[i] != kata[len(kata) - i - 1]:
        palindrome = False
        break  

if palindrome == True :
    print(f"{kata} adalah kata palindrome")
elif palindrome == False : 
    print(f"{kata} bukan kata palindrome")

