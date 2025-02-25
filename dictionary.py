# dict. comprehension kuadrat
squares = {x: x**2 for x in range(1, 6)}

# Ubah value dict.
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78}
updated_grades = {name: score + 5 for name, score in grades.items()} #{'Alice': 90, 'Bob': 95, 'Charlie': 82}

# Key & Value dibalik
grades = {'Alice': 'A', 'Bob': 'B', 'Charlie': 'A'}
flipped = {grade: name for name, grade in grades.items()} # Output: {'A': 'Charlie', 'B': 'Bob'}

# Nested dictionary untuk tabel perkalian
multiplication_table = {i: {j: i * j for j in range(1, 6)} for i in range(1, 6)}

# Membuat dictionary dari dua list
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
combined = {keys[i]: values[i] for i in range(len(keys))} # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # Hitung frekuensi string
text = "hello world"
char_count = {char: text.count(char) for char in set(text)} # Output: {' ': 1, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'l': 3, 'd': 1, 'o': 2}

# Membuat dictionary dari list of tuples
pairs = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
dictionary = {name: score for name, score in pairs} # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# Ubah value dictionary
student_scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
for name, score in student_scores.items():
    if score >= 90:
        student_scores[name] = "Excellent"
    elif score >= 80:
        student_scores[name] = "Good"
    else:
        student_scores[name] = "Needs Improvement"
# Output : {'Alice': 'Good', 'Bob': 'Excellent', 'Charlie': 'Needs Improvement'}

# Dictionary dengan if-else
numbers = [1, 2, 3, 4, 5]
even_odd_dict = {num: "Even" if num % 2 == 0 else "Odd" for num in numbers} # Output: {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}

scores = [85, 72, 95, 60, 88]
grades = {
    score: "A" if score >= 90 else 
           "B" if score >= 80 else 
           "C" if score >= 70 else "D"
    for score in scores
}

nilai_siswa = {"Alice": 80, "Bob": 75, "Charlie": 90}
nilai_huruf = {
    nama: "A" if nilai >= 90 else "B" if nilai >= 80 else "C" if nilai >= 70 else "D"
    for nama, nilai in nilai_siswa.items()
}
