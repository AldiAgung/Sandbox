import os
import time
import random

pilihan = input("Apakah tetap ingin melanjutkan? (Ya/Tidak)")
kata = pilihan.upper()

if kata == "YA":
    for i in range(3,0,-1):
        print("Komputer mati dalam "+ str(i))
        time.sleep(1)
        if i <= 1:
            print("tapi aku masih bakalan kasih kesempatan satu kali lagi")
            time.sleep(2)
            print("jika bener jawabannya gabakalan ke restart")
            time.sleep(1.5)
            print("kalau salah yah tetep aja ke restart lmao")
            time.sleep(1)
            print("siap?")
            time.sleep(2)
            angka = random.randrange(1,10)
            print(angka)
            
            while True:
                try:
                    tebak = int(input("tebak angkanya: "))
                    break
                except ValueError:
                    print("harus berupa angka")

            while (tebak != angka):
                if os.path.exists('Halo.txt'):
                    try:
                        os.startfile('Halo.txt')
                        exit()
                    except AttributeError:
                        os.system(f"open Halo.txt")
                        exit()
                try:
                    print("sayang sekali jawaban kamu salah")
                    time.sleep(2)
                    print("jawabannya adalah: "+ str(angka))
                    time.sleep(1.5)
                    print("jadi sekarang pc kamu ke restart deh HAHAHAHA")
                    time.sleep(2)
                    os.system('shutdown /r /t 30')
                    berkas = open('Halo.txt', 'w')
                    berkas.write("komputer kamu mati hahah")
                    os.path.sameopenfile('Halo.txt')
                    break
                except (ValueError):
                    print(f"harus berupa sebuah angka")
            else:
                print("jawaban yang benar adalah: "+ str(angka))
                print("selamat pc kammu tidak ke restart")
                time.sleep(2)
                exit()
elif kata == "TIDAK":
    exit()