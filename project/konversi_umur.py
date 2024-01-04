import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date, timedelta
import calendar

def hitung_umur():
    try:
        tanggal = int(combobox_tanggal.get())
        bulan = bulan_choices.index(combobox_bulan.get()) + 1
        tahun = int(combobox_tahun.get())

        tanggal_lahir = datetime(tahun, bulan, tanggal)
        hari_ini = datetime.now()
        selisih = hari_ini - tanggal_lahir
        umur_tahun = selisih.days // 365
        umur_bulan = (selisih.days % 365) // 30
        umur_hari = (selisih.days % 365) % 30

        hasil_umur = f"Umur Anda adalah: {umur_tahun} tahun, {umur_bulan} bulan, {umur_hari} hari."
        messagebox.showinfo("Hasil Konversi Umur", hasil_umur)

    except ValueError:
        messagebox.showerror("Error", "Format tanggal atau tahun salah. Pastikan untuk mengisi semua kolom.")


app = tk.Tk()
app.title("Konversi Umur")

#input tanggal
label_tanggal = tk.Label(app, text="Tanggal:")
label_tanggal.grid(row=0, column=0, padx=5, pady=5)

combobox_tanggal = ttk.Combobox(app, values=list(range(1, 32)))
combobox_tanggal.set(1)
combobox_tanggal.grid(row=0, column=1, padx=5, pady=5)

#input bulan
label_bulan = tk.Label(app, text="Bulan:")
label_bulan.grid(row=0, column=2, padx=5, pady=5)

bulan_choices = list(calendar.month_name)
combobox_bulan = ttk.Combobox(app, values=bulan_choices)
combobox_bulan.set(calendar.month_name[1])
combobox_bulan.grid(row=0, column=3, padx=5, pady=5)

#input tahun
label_tahun = tk.Label(app, text="Tahun:")
label_tahun.grid(row=0, column=4, padx=5, pady=5)

tahun_sekarang = date.today().year
tahun_100_terakhir = list(range(tahun_sekarang, tahun_sekarang - 100, -1))
combobox_tahun = ttk.Combobox(app, values=tahun_100_terakhir)
combobox_tahun.set(tahun_sekarang)  # Set nilai awal dengan tahun saat ini
combobox_tahun.grid(row=0, column=5, padx=5, pady=5)

#tombol submit
tombol_hitung = tk.Button(app, text="Hitung Umur", command=hitung_umur)
tombol_hitung.grid(row=1, column=0, columnspan=6, pady=10)


app.mainloop()