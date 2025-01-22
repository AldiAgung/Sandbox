import tkinter as tk
from tkinter import messagebox
from ip_grab import alamatip, interstatus
import os
from datetime import datetime, timedelta

#inisiasi variable
m = tk.Tk()
# m.geometry('800x600')
m.title("Hallooooo")
m.frame()
m.grid()
waktu_lokal = datetime.now().strftime('%H:%M:%S')

waktu_offline = None
durasi_offline = "Belom pernah offline"
label_lama = None

# Fungsi #
def refresh():
    m.destroy()
    os.system(__file__)
    #m.after(5000, refresh)

def lihatip():
    try:
        alamat = alamatip()
        if alamat:
            label_ip.config(text= f'{alamat}')
    except Exception as e:
        messagebox.showerror("Terjadi kesalahan", str(e))

def status():
    global waktu_offline, durasi_offline, label_lama
    try:
        kondisi = interstatus()
        if kondisi:
            if waktu_offline:
                waktu_terhubung = datetime.now()
                durasi_offline = lamaoffline(waktu_offline, waktu_terhubung)
                waktu_offline = None
                if label_lama:
                    label_lama.config(text = durasi_offline)
            label_status.config(text= f'Terhubung')
        else:
            label_status.config(text= f'Tidak terhubung')
    except Exception as e:
        messagebox.showerror("Terjadi kesalahan", str(e))

def lamaoffline(mulai, selesai):
    perbandingan = selesai - mulai
    detik = perbandingan.total_seconds()
    return str(timedelta(seconds=detik)).split(".")[0]

# inisiasi label dll
tk.Label(m, text= 'Ip Internet: ').grid(row = 1, column= 0, pady = 5, padx= 5, sticky='w')
tk.Label(m, text= 'Status internet: ').grid(row = 2, column= 0, pady= 5, padx= 5, sticky= 'w')
tk.Label(m, text= 'Lama offline: ').grid(row = 3, pady = 5, column= 0, sticky= 'w', padx= 5)
tk.Label(m, text= 'Waktu lokal: ').grid(row= 0, pady= 5, column= 0, sticky= 'w', padx= 5)

label_ip = tk.Label(m, text= "")
label_status = tk.Label(m, text= "")
label_lama = tk.Label(m, text= durasi_offline)
waktu_lokal = tk.Label(m, text= f"{waktu_lokal}")

#lokasi label
label_ip.grid(row=1, column=1, pady=5, sticky= 'w')
label_status.grid(row = 2, column= 1, pady= 5, sticky= 'w')
waktu_lokal.grid(row= 0, column= 1, columnspan= 2, padx= 5, pady= 5, sticky= 'w')
label_lama.grid(row = 3, column= 1, pady= 5, sticky= 'w' )

## Tombol ##
tombol_refresh = tk.Button(m, text= "Refresh", command= refresh).grid(row = 4, column= 0, columnspan= 2, pady= 10)

if __name__ == "__main__":
    lihatip()
    status()
    m.mainloop()