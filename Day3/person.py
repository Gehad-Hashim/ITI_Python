class Person:
    money = 0
    mood = 'happy'
    healthRate = 100

    def __init__(self, name):
        self.name = name

    def sleep(self,when):
        print(self.name+' sleep '+when)

    def eat(self):
        pass

    def buy(self):
        pass
