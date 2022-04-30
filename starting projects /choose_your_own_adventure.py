from cgi import print_arguments

name = input("Type in your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and ou can go left or right. Which way would you like to go? "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: "
    ).lower()

    if answer == "swim":
        print("you swim across and was eaten by an a crocodile")
    elif answer == "walk":

        print(
            "you walked for many miles, and ran out of water. You lost the game."
        )
    else:
        print("not a valid option. You lose")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbbly do you want to cross it or head back (cross/back)? "
    )

    if answer == "back":
        print("you go back and loose!")

    elif answer == "cross":
        print(
            "You cross the bridge and meet a stranger. Do you talk to them ? (yes/no) "
        )

        if answer == "yes":
            print("You talk to the stanger and they give you gold. you win!")
        elif answer == "no":
            print("You ignore the stranger, they are offended. You LOSE!")
        else:
            print("You lose!")

    else:
        print("not a valid option. You lose")

else:
    print("not a valid option. You lose")
