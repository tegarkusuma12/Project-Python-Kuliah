def heron(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a) :
        s = (a+b+c)/2 
        A = (s*(s-a)*(s-b)*(s-c)**0.5)
        print(f"Luas area segitiga : {A}")
    else:
        print("Bukan merupakan segitiga")

a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

heron(a,b,c)