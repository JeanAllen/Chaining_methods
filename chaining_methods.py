class User:
    def __init__(self, name):
        self.name = name
        self.amount = 0 

    def make_deposit(self, amount):
        self.amount += amount
        return self
    def make_withdraw(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        
    
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


adrien = User("Adrien")
billy = User("Billy Bob")
benny = User("benny")


adrien.make_deposit(100).make_deposit(300).make_deposit(200).make_withdraw(20) # returned self to chain teh methods
adrien.display_user_balance()

billy.make_deposit(2000)
billy.make_deposit(2000)
billy.make_withdraw(200)
billy.make_withdraw(500)
billy.display_user_balance()

benny.make_deposit(2000)
benny.make_withdraw(1000)
benny.make_withdraw(200)
benny.make_withdraw(500)
benny.display_user_balance()

adrien.transfer_money(400, benny)



