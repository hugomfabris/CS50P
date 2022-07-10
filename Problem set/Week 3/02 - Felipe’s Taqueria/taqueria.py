#This dict represents the taqueria's catalogue
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
#This while loop will prompt the user again until "crtl d" keys are pressed
while True:
    try:
        item = input("Item: ").strip().title()
        if item in menu:
            total += menu[item]
            print("Total: $", end="")
            print("{:.2f}".format(total))
    #The except block get us out of the loop
    except EOFError:
        print()
        print(f"Total: ${total:.2f}")
        break
    except KeyError:
        pass




