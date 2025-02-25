def pascal_triangle(n):
    """Mencetak segitiga Pascal hingga baris ke-n."""

    for i in range(n):
        # Menghitung koefisien untuk setiap baris
        row = [1] * (i + 1)

        # Menghitung koefisien dari baris sebelumnya
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]
        prev_row = row

        # Mencetak baris dengan spasi yang tepat
        print(" " * (n - i), end=" ")
        for num in row:
            print(num, end=" ")
        print()

# Meminta input dari pengguna
n = int(input("Masukkan jumlah baris: "))

# Mencetak segitiga Pascal
pascal_triangle(n)