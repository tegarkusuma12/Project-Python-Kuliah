# angka1 = float(input("Masukkan angka pertama : " ))
# angka2 = float(input("Masukkan angka kedua : " ))
# operator = str(input("Masukkan operator (+,-,*,/) : "))

def operasi(angka1, angka2, operator) :
    if operator == "+":
        hasil = angka1 + angka2
    elif operator == "-":
       hasil = angka1 - angka2
    elif operator == "*":
       hasil = angka1 * angka2
    elif operator == "/":
       hasil = angka1 / angka2
    return hasil

# hasil_operasi = operasi(angka1, angka2, operator)

# print("Hasil : ", hasil_operasi)

