print("Program untuk mengururtkan bilangan yang diinputkan user.")

angka = []
tambah = True
while tambah:
    input_angka = float(input("Masukkan angka(pecahan boleh) : "))
    angka.append(input_angka)
    print(angka)
    while True:
        lanjut = input("Udah?(y=udah, n=nambah): ")
        if lanjut == 'y':
            tambah = False
            break
        elif lanjut == 'n':
            tambah = True
            break
        else:
            print("y atau n woi!")

def urut():
    while True:
        urutan = int(input("1 untuk Ascending, 2 untuk Descending : ")) 
        if urutan == 1 or urutan == 2 :
            return urutan 
        else:
            print("Apalah") 

urutan = urut()
if urutan == 1:
    for i in range(len(angka)-1):
        for j in range(len(angka)-i-1):
            if angka[j] > angka[j+1]:
                angka[j], angka[j+1] = angka[j+1], angka[j]
elif urutan == 2:
   for i in range(len(angka)-1):
        for j in range(len(angka)-i-1):
            if angka[j] < angka[j+1]:
                angka[j], angka[j+1] = angka[j+1], angka[j]
                

print(angka)

