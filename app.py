# parent class
class User():
    def __init__(self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID
     
    def show_details(self):
         print("Personal Details")
         print("")
         print("Name: ", self.name)
         print("Age: ", self.age)
         print("ID: ", self.ID)

# child class
class Bank(User):
    def __init__(self, name, age, ID):
        super().__init__(name, age, ID)
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("Account balance has been updated: Kshs. ", self.balance)
       

Caren = User('Caren', 23, 1234)
Caren.show_details()
Carens_account = Bank('Caren', 23, 1234)
Carens_account.deposit(1000)
Carens_account.deposit(7000)

        