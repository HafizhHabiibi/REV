def bilanganPrima():

    print("="*5 + "Menu Bilangan Prima" + "="*5)
    angkaAwal = int(input("Masukan Angka Awal : "))
    angkaAkhir = int(input("Masukan Angka Akhir : "))

    tampungPrima = []

    def cekPrima (x):
        if x < 2:
            return False
        for i in range(2, x):
            if x % i == 0:
                return False
        return True
    
    for x in range (angkaAwal, angkaAkhir + 1):
        if cekPrima(x):
            tampungPrima.append(x)

    print(f"Yang Termasuk Bilangan Prima adalah \n\n{tampungPrima}\n")
    
def bilanganGanjil():
    print("="*5 + "Menu Bilangan Ganjil" + "="*5)
    angkaAwal = int(input("Masukan Angka Awal : "))
    angkaAkhir = int(input("Masukan Angka Akhir : "))

    tampungGanjil = []

    for i in range(angkaAwal, angkaAkhir + 1):
        if i % 2 != 0:
            tampungGanjil.append(i)

    print(f"Yang Termasuk Bilangan Ganjil adalah \n\n{tampungGanjil}\n")
    
def bilanganGenap():
    print("="*5 + "Menu Bilangan Genap" + "="*5)
    angkaAwal = int(input("Masukan Angka Awal : "))
    angkaAkhir = int(input("Masukan Angka Akhir :"))

    tampungGenap = []

    for i in range(angkaAwal, angkaAkhir + 1):
        if i % 2 == 0:
            tampungGenap.append(i)

    print(f"Yang Termasuk Bilangan Genap adalah \n\n{tampungGenap}\n")
    

def menu():
    while True:
        try:
            print("="*5 + "Menu Bilangan" + "="*2)
            print("1. Bilangan Prima")
            print("2. Bilangan Ganjil")
            print("3. Bilangan Genap")
            print("0. Keluar")

            menu = int(input("Masukan Pilihan Menu : "))

            if menu == 1:
                bilanganPrima()
            elif menu == 2:
                bilanganGanjil()
            elif menu == 3:
                bilanganGenap()
            elif menu == 0:
                print("Terimakasih Sudah Menggunakan Menu Bilangan")
                return
            else:
                print("Pilihan Tidak Tersedia Silahkan Pilih Lagi")

        except ValueError:
            print("Masukan Inputan Dengan Benar!!")
            continue

menu()
