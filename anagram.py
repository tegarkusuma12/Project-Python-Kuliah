def is_anagram(str1, str2):
    lst_str1 = []
    for ch in str1:
        lst_str1.append(ch.lower())

    lst_str2 = []
    for ch in str2:
        lst_str2.append(ch.lower())

    if sorted(lst_str1) == sorted(lst_str2) and len(lst_str1) == len(lst_str2):
        output = print(f"{str1} dan {str2} adalah anagram")
    else:
        output = print(f"{str1} dan {str2} bukan anagram")
    
    return output

str1 = str(input("Masukkan string 1 : "))
str2 = str(input("Masukkan string 2 : "))
is_anagram(str1, str2)