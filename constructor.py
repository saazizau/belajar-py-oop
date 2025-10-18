import os
os.system("cls")

class Mahasiswa:
    nim = 0
    nama = ""

    # Constructor
    def __init__(self, nama, nim):  
        self.nama = nama
        self.nim = nim
    
    # String Representation
    def __str__(self):              
        return f"Mahasiswa nim = {self.nim} - {self.nama}"
    
    # Object Comparison
    def __eq__(self, other):
        return self.nim == other.nim and self.nama == other.nama
    
    def __lt__(self, other):    # Less Then         ( < )
        pass
    
    def __gt__(self, other):    # Grater Then       ( > )
        pass
    
    def __le__(self, other):    # Less or Equal     ( <= )
        pass
    
    def __ge__(self, other):    # Grater or Equal   ( >= )
        pass

# Constructor
mhs = Mahasiswa("Aziz", "411421048")

print(mhs.nim)
print(mhs.nama)

# String Representation
print(f"Mahasiswa {mhs}")

# Object Comparison
mhs1 = Mahasiswa("Aziz", "411421048")
mhs2 = Mahasiswa("Aziz", "411421048")
print(mhs1 == mhs2)

class BankAccount:
    no = ""
    saldo = 0

    def __init__(self, no, saldo = 0):
        if saldo < 0:
            raise ValueError("Saldo harus positif")
        
        self.no = no
        self.saldo = saldo

eko = BankAccount("1212321312", 21000)
# eko = BankAccount("2112w231", -2219)
        
