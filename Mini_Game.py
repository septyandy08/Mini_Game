from random import randint, choice

print("Selamat datang di game tebak angka dan tebak kata!\n\nSilakan pilih jenis game antara tebak_angka atau tebak_kata: ")
tipegame = input("Pilihan game: ")
print()

if tipegame == "tebak_angka":
    print("Masukkan range angka yang ingin ditebak: ")
    batas_bawah = int(input("Masukkan batas bawah range angka: "))
    batas_atas = int(input("Masukkan batas atas range angka: "))
    print()

    print("Anda memiliki 3 kesempatan untuk menebak: ")

    jawaban = randint(batas_bawah, batas_atas)
    kesempatan = 3

    for i in range(3):
        if i == 0:
            angka = int(input("Pilihan pertama: "))
        else:
            angka = int(input("Pilihan selanjutnya: "))
        if angka == jawaban:
            print("Selamat! Pilihan anda benar!")
            break
        else:
            kesempatan -= 1
            if kesempatan == 0:
                print("Pilihan anda salah. Jawabannya adalah", jawaban, ".")
            else:
                print("Pilihan anda salah, silakan coba lagi.", kesempatan, "kali coba lagi.")

        

elif tipegame == "tebak_kata":
    print("Masukkan minimal 4 kata yang ingin ditebak: (Selesaikan dengan kaya 'cukup')")
    
    jumlah_kata = 0
    list_kata = []
    input_kata = input("Masukkan kata: ")

    while input_kata != 'cukup':
        list_kata.append(input_kata)
        input_kata = input("Masukkan kata: ")
        jumlah_kata += 1

    print ("\nKata-kata yang akan ditebak berjumlah", jumlah_kata, ":")

    for j in list_kata:
        print(j)

    answer = choice(list_kata)
    tebakan = 3

    for k in range(3):
        if k == 0:
            kata = input("Pilihan pertama: ")
        else:
            kata = input("Pilihan selanjutnya: ")
        if kata == answer:
            print("Selamat! Pilihan anda benar!")
            break
        else:
            tebakan -= 1
            if tebakan == 0:
                print("Pilihan anda salah. Jawabannya adalah", answer, ".")
            else:
                print("Pilihan anda salah, silakan coba lagi.", tebakan, "kali coba lagi.")



else:
    print("Masukkan pilihan game tebak_angka atau tebak_kata. ")
    print("Jalankan ulang program untuk mengulang. ")

ex = input("Ketik close untuk keluar dari program: ")