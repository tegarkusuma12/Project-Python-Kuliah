# TUGAS 1

# Kalkulator
def calculator(op, num1, num2):
    operations = { 
        "+" : lambda num1, num2 : num1 + num2,
        "-" : lambda num1, num2 : num1 - num2,
        "*" : lambda num1, num2 : num1 * num2,
        "/" : lambda num1, num2 : num1 / num2,
        "%" : lambda num1, num2 : num1 % num2,
        "^" : lambda num1, num2 : num1 ** num2
        }
    
    if op in operations:
        if num1 == 0 or num2 == 0 and op == "/":
            return "Undefined"
        else:
            return operations[op](num1, num2)
    else :
        return "Operator tidak valid"
    
print(calculator("+", 2, 2))  # 4
print(calculator("-", 5, 2))  # 3
print(calculator("*", 4, 3))  # 12
print(calculator("/", 10, 2)) # 5
print(calculator("%", 5, 3)) # 2
print(calculator("^", 20, 2)) # 400
print(calculator("/", 10, 0)) # Undefined

# num1 = int(input("Masukkan num1 : "))
# num2 = int(input("Masukkan num2 : "))
# op = int(input("Masukkan operator : "))

# print(calculator[op](num1, num2))


