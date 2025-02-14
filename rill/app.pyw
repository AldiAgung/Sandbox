import tkinter as tk
from tkinter import messagebox, IntVar, Checkbutton
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

#inisiasi tombol variable
waktu_offline = None
durasi_offline = "Belom pernah offline"
label_lama = None
tombol_refresh = None
refresh_id = None
interval_waktu = 5000
mulai_refresh = None

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

def klik():
    global refresh_id, interval_waktu
    if var1.get() == 1:
        mulai_penghitungan()
    else:    
        stop_auto()

def mulai_penghitungan():
    global refresh_id, mulai_refresh
    stop_auto()
    mulai_refresh = datetime.now()
    refresh_id = m.after(interval_waktu, refresh)
    update_count_label()

def stop_auto():
    global refresh_id
    if refresh_id:
        m.after_cancel(refresh_id)
        refresh_id = None
    durasi_refresh.config(text="")

def update_count_label():
    global refresh_id, mulai_refresh
    if refresh_id and mulai_refresh:
        sisa_waktu = interval_waktu - (datetime.now() - mulai_refresh).total_seconds() * 1000 
        if sisa_waktu == 0:
            durasi_refresh.config(text= "Sedang mengulang...")
        else:
            sisa_detik = int(sisa_waktu / 1000) + 1
            durasi_refresh.config(text= f"Refresh dalam {sisa_detik}")
            m.after(1000, update_count_label)

#Intvar
var1 = IntVar()

# inisiasi label dll
tk.Label(m, text= 'Ip Internet: ').grid(row = 1, column= 0, pady = 5, padx= 5, sticky='w')
tk.Label(m, text= 'Status internet: ').grid(row = 2, column= 0, pady= 5, padx= 5, sticky= 'w')
tk.Label(m, text= 'Lama offline: ').grid(row = 3, pady = 5, column= 0, sticky= 'w', padx= 5)
tk.Label(m, text= 'Waktu lokal: ').grid(row= 0, pady= 5, column= 0, sticky= 'w', padx= 5)

#cekbutton
cek_ulang = Checkbutton(m, text = "Auto?", variable= var1, onvalue= 1, offvalue= 0, command= klik)

#label tulisan
label_ip = tk.Label(m, text= "")
label_status = tk.Label(m, text= "")
label_lama = tk.Label(m, text= durasi_offline)
waktu_lokal = tk.Label(m, text= f"{waktu_lokal}")
durasi_refresh = tk.Label(m, text= "")

#lokasi label
label_ip.grid(row=1, column=1, pady=5, sticky= 'w')
label_status.grid(row = 2, column= 1, pady= 5, sticky= 'w')
waktu_lokal.grid(row= 0, column= 1, columnspan= 2, padx= 5, pady= 5, sticky= 'w')
label_lama.grid(row = 3, column= 1, pady= 5, sticky= 'w' )
cek_ulang.grid(row= 4, column= 0, padx= 0, sticky= 'w')
durasi_refresh.grid(row = 4, column= 1, padx= 0, stick= 'w')

## Tombol ##
tombol_refresh = tk.Button(m, text= "Refresh", command= refresh)
tombol_refresh.grid(row = 5, column= 0, columnspan= 2, pady= 10)

#Inisiasi aplikasi
if __name__ == "__main__":
    lihatip()
    status()
    m.mainloop()