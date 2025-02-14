import os, time

while (True):
    try:
        kata = int(input("berapa lama?: "))
        os.system('shutdown /s /t '+ str(kata))
        break
    except:
        print(f"harus berupa angka")
        time.sleep(1)
        print("coba lagi")
        time.sleep(2)

#python -m compileall -l laptop.py
#pip install -U pyinstaller
#python -m PyInstaller laptop.py