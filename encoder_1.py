def encode():
    inputPassword = input("Please enter your password to encode:")
    encodedPassword = " "
    for i in range(8):
        addedChar = str(3 + int(inputPassword[i]))
        encodedPassword = encodedPassword + addedChar
    encodedPassword = encodedPassword.lstrip()
    print("Your password has been encoded and stored!")
    print(" ")
    return encodedPassword