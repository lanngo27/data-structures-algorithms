class Human():
    def __init__(self, first_name, last_name, money, age):
        self.first_name = first_name
        self.last_name = last_name
        self.money = money
        self.age = age
        self.married_to = None
            
    def return_name(self):
        return self.first_name, self.last_name
        
    def increment_age(self):
        self.age +=1
        
    def return_age(self):
        return self.age
    
    def buy_something(self, money):
        if self.money < money:
            return False
        self.money-=money
        return True
        
    def pay_salary(self, amount):
        self.money += amount
        
    def return_money(self):
        return self.money
    
    def return_married_to(self):
        return self.married_to
    
    def get_married(self, human):
        self.married_to = human
        if human.married_to == None:
            human.get_married(self)
    
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
def create_humans():
    teemu = Human('Teemu', 'Teekkari', 0, 30)
    onni = Human('Onni', 'Opiskelija', 1000, 22)
    anni = Human('Anni', 'Arkkari', 2000, 23)

    teemu.buy_something(100)
    onni.buy_something(500)
    teemu.pay_salary(2500)

    anni.increment_age()
    teemu.get_married(anni)
    print(onni)
    return teemu, onni, anni

if __name__ == "__main__":
    create_humans()
    
