n = float(input("Masukkan bilangan desimal : "))

def ke_heksa(n):
    hasil = ""
    hexa = "0123456789ABCDEF"

    if n < 0:
        print("Bilangan harus positif")
    while n > 0:
        sisa = int(n % 16)
        hasil = hexa[sisa] + hasil
        n //=16

    return hasil

hasil_heksadesimal = ke_heksa(n)
print(f"Heksadesimal dari {n} adalah {hasil_heksadesimal}")    


    
