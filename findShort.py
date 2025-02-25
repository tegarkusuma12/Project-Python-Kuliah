# Tugas 2
def find_short(list_kata):
    panjang = [len(kata) for kata in list_kata]

    index_terpendek = panjang.index(min(panjang))

    return list_kata[index_terpendek]

print(find_short(["Aiueo", "Hahahaha", "Ok"]))
    
