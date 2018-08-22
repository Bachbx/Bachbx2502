shop_list = ["T-Shirt", "Sweater"]

while True:
    command = input("Welcome to our shop, what do you want (C, R, U, D)? ")
    command = command.lower()
    if command == "R" or command == "r":
        print("Our items:", shop_list)
    elif command == "C" or command == "c":
        shop_list.append(input("Enter new item: "))
        print("Our items:", shop_list)
    elif command == "U" or command == "u":
        Updateposition = int(input("Update position? "))
        Update = Updateposition - 1
        shop_list.pop(Update)
        shop_list.insert(Update, input("New item? "))
        print("Our items:", shop_list)
    elif command == "D" or command == "d":
        Updateposition = int(input("Delete position? "))
        Update = Updateposition - 1
        shop_list.pop(Update)
        print("Our items:", shop_list)
    else:
        print("What?")
        print("I do not know what you are talking about")