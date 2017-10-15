class food():
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getPrice(self):
        return self.price

class fruit(food):
    def __init__(self, name, description, price, weight):
        self.weight = weight
        super().__init__(name, description, price)

    def setData(self):
        self.name = input('Name: ')
        self.description = input('Description: ')
        self.price = int(input('Price: '))
        self.weight = int(input('Weight: '))

class snack(food):
    def __init__(self, name, description, price, calories):
        self.calories = calories
        super().__init__(name, description, price)

    def getCalories(self):
        return self.calories

    def setData(self):
        self.name = input('Name: ')
        self.description = input('Description: ')
        self.price = int(input('Price: '))
        self.calories = int(input('Calories: '))

class meat(food):
    def __init__(self, name, description, price):
        super().__init__(name, description, price)
    def setData(self):
        self.name = input('Name: ')
        self.description = input('Description: ')
        self.price = int(input('Price: '))

class drink(snack):
    def __init__(self, name, description, price, calories):
        super().__init__(name, description, price, calories)
