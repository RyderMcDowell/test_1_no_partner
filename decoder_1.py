def decode(encodedPassword):
    decodedPassword = " "
    for i in range(8):
        addedChar = str(int(encodedPassword[i])+3*-1)
        decodedPassword = decodedPassword + addedChar
    decodedPassword = decodedPassword.lstrip()
    print(decodedPassword)
    print(f"The encoded password is {encodedPassword}, and the original password is {decodedPassword}.")
    print(" ")