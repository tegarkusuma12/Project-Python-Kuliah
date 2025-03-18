import turtle

# Membuat objek turtle
t = turtle.Turtle()

# Mengatur kecepatan
t.speed(0)

# Mengatur warna
t.color("red")

# Mengatur ketebalan garis
t.width(3)

# Menggambar setengah hati pertama
t.left(45)
t.circle(100, 180)
t.right(90)
t.circle(100, 180)

# Mengatur posisi
t.penup()
t.goto(-100, 0)
t.pendown()

# Mengatur warna
t.color("pink")

# Menggambar setengah hati kedua
t.left(90)
t.circle(100, 180)
t.right(90)
t.circle(100, 180)

# # Menyimpan gambar
# ts = turtle.getscreen()
# ts.getcanvas().postscript(file="hati.eps")

# Menutup jendela turtle
turtle.done()