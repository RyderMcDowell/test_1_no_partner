from encoder import encode
from decoder import decode
def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print(" ")
    menuChoice = int(input("Please enter an option:"))
    return menuChoice
def main():  
    menuChoice = 0   
    while menuChoice < 3:
        menuChoice = menu()
        if menuChoice == 1: encodedPassword = encode()
        if menuChoice == 2: decode(encodedPassword)
        if menuChoice == 3: quit()
main()

