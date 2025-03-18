# def ke_heksa(n):
#     hasil = ""
#     hexa = "0123456789ABCDEF"

#     if n < 0:
#         print("Bilangan harus positif")
#     while n > 0:
#         sisa = int(n % 16)
#         hasil = hexa[sisa] + hasil
#         n //=16

#     return hasil

def ke_heksa(n):
    hexa = "0123456789ABCDEF"

    if n == 0:
        return ""
    elif n < 0:
        return print("Bilangan harus positif")
        
    return ke_heksa(n // 16) + hexa[n % 16]

n = int(input("Masukkan bilangan desimal : "))

print(f"Heksadesimal dari {n} adalah {ke_heksa(n)}")    


    
