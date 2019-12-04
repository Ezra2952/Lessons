MINIMUM_LENGTH = 4


def ask_password():
    password = input("Enter password of minimum {} characters: ".format(MINIMUM_LENGTH))
    while len(password) < MINIMUM_LENGTH:
        password = input("Enter password of minimum {} characters: ".format(MINIMUM_LENGTH))

    print('*' * len(password))


ask_password()
