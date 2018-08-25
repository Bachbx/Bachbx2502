from turtle import *

turtle_list = []
t = Turtle()
turtle_list.append(t)
while True :
    command = input("Command to move the turtle[fd , lt , rt , bd] ")
    command_list = command.split(" ")
    print(command)
    command = command.lower()
    for c in command_list:
        if c == "fd":
            t.forward(100)
        elif c == "lt":
            t.left(90)
        elif c == "rt":
            t.right(90)
        elif c == "bd":
            t.backward(90)
        else:
            print("You can only use fd , lt , rt , bd , to move the turtle")


mainloop()


