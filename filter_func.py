# filter()
#1
def jam_tidur_sehat(pair):
    jam_tidur, usia = pair
    if usia <= 12:
        return 9 <= jam_tidur <= 11  # Anak-anak
    elif 13 <= usia <= 18:
        return 8 <= jam_tidur <= 10  # Remaja
    elif 19 <= usia <= 64:
        return 7 <= jam_tidur <= 9   # Dewasa
    else:
        return 7 <= jam_tidur <= 8   # Lansia

jam_tidur = [5, 9, 7, 6, 10, 8, 4, 11, 7, 6, 8, 9, 7, 12, 5]
usia = [6, 15, 30, 65, 10, 17, 25, 8, 40, 35, 13, 18, 12, 5, 70]

result = list(filter(jam_tidur_sehat, zip(jam_tidur, usia)))
print(result)

#2
def segitiga(x):
    if sum(x) == 180:
        return True
    return False

sudut = sudut = [(60, 60, 60), (90, 45, 45), (120, 30, 30), (100, 40, 40)]

print(list(map(segitiga, sudut)))