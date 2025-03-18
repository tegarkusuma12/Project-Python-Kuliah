# map()
#1
def count_letters(x, y):
    if len(x) == y:
        return True
    return False

x = ["hahaha", "batagor", "ultraman"]
y = (6, 7, 9)

result = list(map(count_letters, x,y))
print(result)

#2
def neuturalise(a, b):
    if a == "+" and b == "+":
        return "+"
    elif a == "-" and b == "-":
        return "-"
    else:
        return "0"
    
a = "+-+-++"
b = "-++---"

# print(''.join(map(neuturalise, a, b)))
