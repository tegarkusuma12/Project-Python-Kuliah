# Input 3 bilangan integer (nilai semester)
while True:
    try:
        # Memastikan input adalah 3 bilangan integer
        values = list(map(int, input("Masukkan 3 nilai (dipisahkan dengan spasi): ").split()))
        if len(values) == 3:
            break
        else:
            print("Masukkan tepat 3 bilangan.")
    except ValueError:
        print("Input harus berupa bilangan bulat.")

# Lambda untuk menghitung nilai akhir semester (rata-rata)
calculate_average = lambda scores: sum(scores) / len(scores)
average = calculate_average(values)

# List comprehension untuk menghitung selisih nilai dengan 100
differences = [100 - score for score in values]

# Output
print(f"Nilai semester: {values}")
print(f"Nilai akhir semester (rata-rata): {average:.2f}")
print(f"Selisih nilai dengan 100: {differences}")
