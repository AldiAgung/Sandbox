import os, time

try:
    kata = int(input("berapa lama?: "))
    os.system('shutdown /s /t '+ str(kata))
except ValueError:
    print(f"Harus berupa sebuah angka")
    time.sleep(2)
    exit()

    #python -m compileall -l laptop.py
    #python -m PyInstaller laptop.py