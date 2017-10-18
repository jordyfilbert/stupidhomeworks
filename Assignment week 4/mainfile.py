from classes import *

arr = []
fruit1 = None
snack1 = None
meat1 = None
drink1 = None
with open("default.txt") as file_object:
    arr = file_object.readline().split(',')
    fruit1 = fruit(arr[0], arr[1], int(arr[2]), int(arr[3]))
    arr = file_object.readline().split(',')
    snack1 = snack(arr[0], arr[1], int(arr[2]), int(arr[3]))
    arr = file_object.readline().split(',')
    meat1 = meat(arr[0], arr[1], int(arr[2]))
    arr = file_object.readline().split(',')
    drink1 = drink(arr[0], arr[1], int(arr[2]), int(arr[3]))

fruits = []
snacks = []
meats = []
drinks = []
shoppingcart = []

fruits.append(fruit1)
snacks.append(snack1)
meats.append(meat1)
drinks.append(drink1)

while True:
    print("Admin/Visitor?\n[1]Admin\n[2]Visitor\n[3]Exit")
    admvis = int(input())
    if admvis == 1:
        while True:
            print("What would you like edit?")
            print("[1]Fruit\n[2]Snack\n[3]Meat\n[4]Drink\n[5]Back to menu")
            editselect = int(input())
            if editselect == 1:
                print("[1]Add\n" + "[2]Edit\n" + "[3]Remove")
                select1 = int(input())
                if select1 == 1:
                    while True:
                        name = input("Insert fruit name here\n")
                        desc = input("Insert description here\n")
                        price = input("Insert Price here\n")
                        weight = input("Insert weight here\n")
                        fruits.append(fruit(name, desc, price, weight))
                        print("Would you like to add more?")
                        selectt = int(input("[1]=Yes\n" + "[2]=No\n"))
                        if selectt == 2:
                            break
                elif select1 == 2:
                    for i in range(len(fruits)):
                        print(str(i + 1) + ". " + fruits[i].getName())
                    id = int(input('Which one do you want to edit: '))
                    fruits[id - 1].setData()

                elif select1 == 3:
                    for i in range(len(fruits)):
                        print(str(i + 1) + ". " + fruits[i].getName())
                    id = int(input("Which one do you want to remove?"))
                    del fruits[id - 1]

            elif editselect == 2:
                print("[1]Add\n" + "[2]Edit\n" + "[3]Remove")
                select1 = int(input())
                if select1 == 1:
                    while True:
                        name = input("Insert snacks name here\n")
                        desc = input("Insert description here\n")
                        price = input("Insert Price here\n")
                        calories = input("Insert Calories here\n")
                        snacks.append(snack(name, desc, price, calories))
                        print("Would you like to add more?")
                        selectt = int(input("[1]=Yes\n" + "[2]=No\n"))
                        if selectt == 2:
                            break
                elif select1 == 2:
                    for i in range(len(snacks)):
                        print(str(i + 1) + ". " + snacks[i].getName())
                    id = int(input('Which one do you want to edit: '))
                    snacks[id - 1].setData()

                elif select1 == 3:
                    for i in range(len(snacks)):
                        print(str(i + 1) + ". " + snacks[i].getName())
                    id = int(input("Which one do you want to remove?\n"))
                    del snacks[id - 1]

            elif editselect == 3:
                print("[1]Add\n" + "[2]Edit\n" + "[3]Remove")
                select1 = int(input())
                if select1 == 1:
                    while True:
                        name = input("Insert meat name here\n")
                        desc = input("Insert description here\n")
                        price = input("Insert Price here\n")
                        meats.append(meat(name, desc, price))
                        print("Would you like to add more?")
                        selectt = int(input("[1]=Yes\n" + "[2]=No\n"))
                        if selectt == 2:
                            break
                elif select1 == 2:
                    for i in range(len(meats)):
                        print(str(i + 1) + ". " + meats[i].getName())
                    id = int(input('Which one do you want to edit: '))
                    meats[id - 1].setData()

                elif select1 == 3:
                    for i in range(len(meats)):
                        print(str(i + 1) + ". " + meats[i].getName())
                    id = int(input("Which one do you want to remove?\n"))
                    del meats[id - 1]

            elif editselect == 4:
                print("[1]Add\n" + "[2]Edit\n" + "[3]Remove")
                select1 = int(input())
                if select1 == 1:
                    while True:
                        name = input("Insert Drink name here\n")
                        desc = input("Insert description here\n")
                        price = input("Insert Price here\n")
                        calories = input("Insert calory here\n")
                        drinks.append(drink(name, desc, price, calories))
                        print("Would you like to add more?")
                        selectt = int(input("[1]=Yes\n" + "[2]=No\n"))
                        if selectt == 2:
                            break
                elif select1 == 2:
                    for i in range(len(drinks)):
                        print(str(i + 1) + ". " + drinks[i].getName())
                    id = int(input('Which one do you want to edit: '))
                    drinks[id - 1].setData()

                elif select1 == 3:
                    for i in range(len(drinks)):
                        print(str(i + 1) + ". " + drinks[i].getName())
                    id = int(input("Which one do you want to remove?\n"))
                    del drinks[id - 1]
            elif editselect == 5:
                break

    elif admvis == 2:
        while True:
            print("Welcome to sfiStore!")
            print("What would you like to do?\n[1]Buy something\n[2]Remove from cart\n[3]See your shopping cart\n[4]Checkout")
            selecttt = int(input(""))
            if selecttt == 1:
                print("[1]Fruit\n[2]Snack\n[3]Meat\n[4]Drink\n")
                select2 = int(input())
                if select2 == 1:
                    for i in range(len(fruits)):
                        print(str(i + 1) + ". " + fruits[i].getName() + "//Description = " + fruits[i].getDescription() + " //Price = " + str(fruits[i].getPrice()))
                    buy = int(input("Which one do you want to buy?\n"))
                    shoppingcart.append(fruits[buy - 1])
                elif select2 == 2:
                    for i in range(len(snacks)):
                        print(str(i + 1) + ". " + snacks[i].getName() + "//Description = " + snacks[i].getDescription() + "//Calories = " + str(snacks[i].getCalories()) + " //Price = " + str(snacks[i].getPrice()))
                    buy = int(input("Which one do you want to buy?\n"))
                    shoppingcart.append(snacks[buy - 1])
                elif select2 == 3:
                    for i in range(len(meats)):
                        print(str(i + 1) + ". " + meats[i].getName() + "//Description = " + meats[i].getDescription() + " //Price = " + str(meats[i].getPrice()))
                    buy = int(input("Which one do you want to buy?\n"))
                    shoppingcart.append(meats[buy - 1])
                elif select2 == 4:
                    for i in range(len(drinks)):
                        print(str(i + 1) + ". " + drinks[i].getName() + "//Description = " + drinks[i].getDescription() + "//Calories = " + str(drinks[i].getCalories()) + " //Price = " + str(drinks[i].getPrice()))
                    buy = int(input("Which one do you want to buy?\n"))
                    shoppingcart.append(drinks[buy - 1])

            elif selecttt == 2:
                print ("What do you want to remove?")
                for i in range(len(shoppingcart)):
                    print(str(i + 1) + ". " + shoppingcart[i].getName())
                delete=int(input("Which one do you want to remove?\n"))
                shoppingcart.pop(delete-1)

            elif selecttt == 3:
                print ("Here is your current list of item")
                for i in range(len(shoppingcart)):
                    print(str(i + 1) + ". " + shoppingcart[i].getName() + "\nWith the cost of\n" + str(shoppingcart[i].getPrice()))

            elif selecttt ==4:
                total = 0
                for i in range(len(shoppingcart)):
                    total += int(shoppingcart[i].getPrice())
                print(total)
