print("Hello, Welcome to RobotBarista")
name=input("What is your name ? ")
if name == "Ben":

    print("You're not welcome here evil Ben")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n")

menu=("\n Frappucino 8$\n Cappucino 8$\n Latte 8$\n Latte Macha 8$\n Latte caramel 8$\n Double Expresso 8$\n ")
print("Here's the menu : " + menu )

order=input("What do you want to order ? ")
print("Well your " + order + " will be ready in a moment !" )

number_of_coffee= input("How many coffee do you want ?\n")
print("Ok your " + number_of_coffee + " coffee is ready ! ")
price= int(number_of_coffee) * 8
print("Here you go, the total is " + str(price) + "$ have a nice day !! ")
