import tkinter as tk #untuk memulai GUI

# def merupakan function (pada bahasa c++ biasanya disebut "VOID")
#sticky bisa "s" , "w" , "n" , "e" (south, west, north , east). Menentukan posisi
#row=baris/urutan


def hitungbmi():
    Berat_kg = float(entry_berat.get()) # Entry di tkinter sama saja seoerti float(input())
    Tinggi_cm = float(entry_tinggi.get())

    # Menghitung BMI
    rumusbmi = Berat_kg / ((Tinggi_cm/100) ** 2)
    label_hasil.config(text=f"BMI: {rumusbmi:.2f}") # :.2f agar hanya menampilkan 2 angka dibelakang koma

# Menentukan kategori BMI
    if rumusbmi < 18.5:
        kategori = "Kurus"
    elif 18.5 <= rumusbmi <= 24.9:
        kategori = "Normal"
    else:
        kategori = "Obesitas"

    label_kategori.config(text=f"Kategori: {kategori}")

# Mengatur ukuran font untuk elemen-elemen
font_style = ("Comic sans", 10)  # Atur jenis font dan ukurannya

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator BMI")
root.geometry("400x300")

# Membuat label dan entry untuk input berat
label_berat = tk.Label(root, text="Berat (kg): ", font=font_style, bg="lightblue")
label_berat.grid(row=0, column=0, pady=10, sticky="s")
entry_berat = tk.Entry(root, font=font_style)
entry_berat.grid(row=0, column=1, pady=10)

# Membuat label dan entry untuk input tinggi
label_tinggi = tk.Label(root, text="Tinggi (cm): ", font=font_style, bg="lightblue")
label_tinggi.grid(row=1, column=0, pady=10, sticky="s")
entry_tinggi = tk.Entry(root, font=font_style) 
entry_tinggi.grid(row=1, column=1, pady=10)

# Membuat tombol untuk menghitung BMI
tombol_hitung = tk.Button(root, text="Hitung BMI", command=hitungbmi, font=font_style, bg="lightgreen")
tombol_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan hasil BMI
label_hasil = tk.Label(root, text="BMI: ", font=font_style)
label_hasil.grid(row=3, column=0, columnspan=2, pady=10, sticky="w")

# Membuat label untuk menampilkan kategori BMI
label_kategori = tk.Label(root, text="Kategori: ", font=font_style)
label_kategori.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

# Menetapkan ukuran jendela dan menjalankan aplikasi
root.mainloop()