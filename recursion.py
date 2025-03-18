#soal no 6
def recursion(n):
    if n <= 3:
        return n
    else:
        if n % 4 == 0:
            return recursion(n - 1) - 1
        else:
            return recursion(n - 1) + 1

# Input dari 1 hingga 12
input_values = [x for x in range(1, 13)]
print(f"input : {input_values}")
print(f"hasil : {[recursion(x) for x in input_values]}")
