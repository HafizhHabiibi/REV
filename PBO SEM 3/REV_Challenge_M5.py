from tabulate import tabulate
import os

playlist = []

class Music:
    def __init__(self, judul = "", penyanyi = "", genre = ""):
        self.judul = judul
        self.penyanyi = penyanyi
        self.genre = genre

class Japan(Music):

    jp1 = ["Shiny Days", "Asaka", "Japanese"]
    jp2 = ["Haruka Mirai", "Kankaku Piero", "Japanese"]
    jp3 = ["OTONANBLUE", "Atarashii Gakko", "Japanese"]

    japan = [jp1, jp2, jp3]

    def __init__(self, judul = "", penyanyi = "", genre = "Japanese"):
        super().__init__(judul, penyanyi, genre)

    def tambah_lagu(self):
        judul = str(input("Masukan Judul Lagu Yang Ingin Ditambahkan : "))

        for i in self.japan:
            if i[0] == judul:
                print("Judul ini sudah ada, silahkan input judul baru!")
                return
            
        penyanyi = str(input("Masukan Penyanyi Yang Ingin Ditambahkan : "))
        genre = "Japanese"

        self.japan.append([judul, penyanyi, genre])
        print("Lagu baru berhasil ditambahkan! \n")

    def lihat(self):
        print("\n")
        headers = ["JUDUL", "PENYANYI", "GENRE"]
        print(tabulate(self.japan, headers, tablefmt="fancy_grid"))
        print("\n")

    def delete(self):
        judul = str(input("Masukan Judul Lagu Yang Ingin Dihapus : "))

        for i in self.japan:
            if i[0] == judul:
                self.japan.remove(i)
                print("Lagu Berhasil Dihapus! \n")
                return

        print("Judul lagu tidak ditemukan silahakan input dengan benar! \n")

class Hiphop(Music):
    hp1 = ["Hit Em Up", "2Pac", "Hip Hop"]
    hp2 = ["My Name Is", "Eminem", "Hip Hop"]
    hp3 = ["Big Poopa", "The Notorious B.I.G", "Hip Hop"]

    hiphop = [hp1, hp2, hp3]

    def __init__(self, judul = "", penyanyi = "", genre = "Hip Hop"):
        super().__init__(judul, penyanyi, genre)

    def tambah_lagu(self):
        judul = str(input("Masukan Judul Lagu Yang Ingin Ditambahkan : "))

        for i in self.hiphop:
            if i[0] == judul:
                print("Judul ini sudah ada, silahkan input judul baru!")
                return
            
        penyanyi = str(input("Masukan Penyanyi Yang Ingin Ditambahkan : "))
        genre = "Hip Hop"

        self.hiphop.append([judul, penyanyi, genre])
        print("Lagu baru berhasil ditambahkan! \n")

    def lihat(self):
        print("\n")
        headers = ["JUDUL", "PENYANYI", "GENRE"]
        print(tabulate(self.hiphop, headers, tablefmt="fancy_grid"))
        print("\n")

    def delete(self):
        judul = str(input("Masukan Judul Lagu Yang Ingin Dihapus : "))

        for i in self.hiphop:
            if i[0] == judul:
                self.hiphop.remove(i)
                print("Lagu Berhasil Dihapus! \n")
                return

        print("Judul lagu tidak ditemukan silahakan input dengan benar! \n")

class English(Music):
    en1 = ["Bohemian Rhapsody", "Queen", "English"]
    en2 = ["Die With Smile", "Bruno Mars", "English"]
    en3 = ["American Idiot", "Green Days", "English"]

    english = [en1, en2, en3]

    def __init__(self, judul = "", penyanyi = "", genre = "English"):
        super().__init__(judul, penyanyi, genre)

    def tambah_lagu(self):
        judul = str(input("Masukan Judul Lagu Yang Ingin Ditambahkan : "))

        for i in self.english:
            if i[0] == judul:
                print("Judul ini sudah ada, silahkan input judul baru! \n")
                return
            
        penyanyi = str(input("Masukan Penyanyi Yang Ingin Ditambahkan : "))
        genre = "English"

        self.english.append([judul, penyanyi, genre])
        print("Lagu baru berhasil ditambahkan! \n")

    def lihat(self):
        print("\n")
        headers = ["JUDUL", "PENYANYI", "GENRE"]
        print(tabulate(self.english, headers, tablefmt="fancy_grid"))
        print("\n")

    def delete(self):
        judul = str(input("Masukan Judul Lagu Yang Ingin Dihapus :"))

        for i in self.english:
            if i[0] == judul:
                self.english.remove(i)
                print("Lagu Berhasil Dihapus! \n")
                return
        
        print("Judul lagu tidak ditemukan silahakan input dengan benar! \n")

japan_music = Japan()
hiphop_music = Hiphop()
english_music = English()

def menuJP():
    while True:
        try:
            print("="*20 + "JAPANESE SONG" + "="*20)
            print("1. Tampilkan Musik")
            print("2. Tambah Musik")
            print("3. Hapus Musik")
            print("4. Keluar")

            pilih = int(input("Inputkan menu yang ingin dipilih : "))

            if pilih == 1:
                japan_music.lihat()
            elif pilih == 2:
                japan_music.tambah_lagu()
            elif pilih == 3:
                japan_music.delete()
            elif pilih == 4:
                os.system("cls")
                return

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN BENAR \n")

def menuHP():
    while True:
        try:
            print("="*20 + "HIP HOP SONG" + "="*20)
            print("1. Tampilkan Musik")
            print("2. Tambah Musik")
            print("3. Hapus Musik")
            print("4. Keluar")

            pilih = int(input("Inputkan menu yang ingin dipilih : "))

            if pilih == 1:
                hiphop_music.lihat()
            if pilih == 2:
                hiphop_music.tambah_lagu()
            if pilih == 3:
                hiphop_music.delete()
            if pilih == 4:
                os.system("cls")
                return

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN BENAR \n")

def menuEN():
    while True:
        try:
            print("="*20 + "ENGLISH SONG" + "="*20)
            print("1. Tampilkan Musik")
            print("2. Tambah Musik")
            print("3. Hapus Musik")
            print("4. Keluar")

            pilih = int(input("Inputkan menu yang ingin dipilih : "))

            if pilih == 1:
                english_music.lihat()
            elif pilih == 2:
                english_music.tambah_lagu()
            elif pilih == 3:
                english_music.delete()
            elif pilih == 4:
                os.system("cls")
                return

        except ValueError:
            print("INPUTAN SALAH SILAHKAN INPUT DENGAN BENAR \n")

# Mengambil Value Array japa, hiphop, english yang beraaa di dalam child class
playlist.extend(japan_music.japan)
playlist.extend(hiphop_music.hiphop)
playlist.extend(english_music.english)

def main():
    while True:
        try:
            print("="*20 + "PLAYLIST" + "="*20)
            print("1. Japanese Song")
            print("2. Hip Hop Song")
            print("3. English Song")
            print("4. Daftar Musik")
            print("5. Cari Musik")
            print("6. Keluar")

            pilih = int(input("Inputkan menu yang ingin dipilih : "))

            if pilih == 1:
                os.system("cls")
                menuJP()

            elif pilih == 2:
                os.system("cls")
                menuHP()

            elif pilih == 3:
                os.system("cls")
                menuEN()

            elif pilih == 4:
                urut = sorted(playlist, key = lambda x: x[0])
                print("\n")
                headers = ["JUDUL", "PENYANYI", "GENRE"]
                print(tabulate(urut, headers, tablefmt="fancy_grid"))
                print("\n")

            elif pilih == 5:
                cari = str(input("Cari lagu berdasarkan nama penyanyi : "))
                cari_lagu = [lagu for lagu in playlist if cari.lower() in lagu[1].lower()]

                if cari_lagu:
                    print("\n")
                    headers = ["JUDUL", "PENYANYI", "GENRE"]
                    print(tabulate(cari_lagu, headers, tablefmt="fancy_grid"))
                    print("\n")
                else:
                    print("Lagu tidak ditemukan silahkan inputkan nama penyanyi yang benar! \n")

            elif pilih == 6:
                print("="*20 + "TERIMAKASIH" + "="*20)
                return
            
        except ValueError:
            print("INPUTAN SALAH SILAHAKAN INPUT DENGAN BENAR \n")

if __name__ == "__main__":
    main()














