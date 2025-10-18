import os
os.system("cls")

class Kampus:
    nama = ""
    alamat = ""
    pass

class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Hallo nama saya {self.nama}")
    
    def hello(self, nama):
        print(f"Halo {nama}, nama saya {self.nama}")

    pass


kampus1 = Kampus()
kampus2 = Kampus()

print(type(kampus1))
print(type(kampus2))

mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 4111421
mahasiswa1.nama = "Sab"

print(mahasiswa1.nim)
print(mahasiswa1.nama)
print(mahasiswa1.perkenalan())
print(mahasiswa1.hello("Boss"))

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 232990
mahasiswa2.nama = "Aziz"

print(mahasiswa2.nim)
print(mahasiswa2.nama)
print(mahasiswa2.perkenalan())
print(mahasiswa2.hello("Boss"))


print(type(mahasiswa1))
print(type(mahasiswa2))

