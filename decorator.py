import os
os.system("cls")

class Matematika:

    @staticmethod
    def tambah(a, b):
        return a + b
    
print(Matematika.tambah(1, 2))

class BankAccount:
    no = ""
    balance = 0
    active = True

    def __init__(self, no, balance=0):
        self.no = no
        self.balance = balance
    
    @classmethod
    def disabled(cls, no, balance=0):
        result = cls(no, balance)
        result.active = False
        return result

bank_account1 = BankAccount("123324", 100000)
print(f"{bank_account1.no}, {bank_account1.balance}, {bank_account1.active}")


bank_account2 = BankAccount.disabled("123324", 100000)
print(f"{bank_account2.no}, {bank_account2.balance}, {bank_account2.active}")

class Category:
    __name = ""

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        if name == "":
            raise ValueError("Nama tidak boleh kosong")
        self.__name = name
    
category1 = Category()
category1.name ="A"
print(category1.__name)
