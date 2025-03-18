def is_palindrome(word):
    return word == word[::-1]

# Input kata
list_kata = input("Masukkan kata-kata, dipisahkan dengan spasi: ").split()

# Dictionary comprehension dan periksa setiap kata
palindrome_dict = {kata: is_palindrome(kata) for kata in list_kata}

# Menampilkan hasil
for word, is_palindrome in palindrome_dict.items():
    if is_palindrome:
        print(f"{word} adalah kata palindrome")
    else:
        print(f"{word} bukan kata palindrome")
