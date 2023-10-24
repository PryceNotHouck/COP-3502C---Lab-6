# Pryce Houck, Sarah Cedeno

def encoder(password):
    encoded = ""
    temp = 0
    for i in range(len(password)):
        temp = int(password[i]) + 3
        if temp > 9:
            temp -= 10
        encoded += str(temp)
    return temp


def main():
    running = True
    while running:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Exit")
        user = input("Please enter an option: ")
        valid = False
        while not valid:
            if user == '1':
                password = input("Please enter a password to encode: ")
                password = encoder(password)
                print("Your password has been encoded and stored!")
                valid = True
            if user == '2':
                pass
                valid = True
            if user == '3':
                valid = True
                running = False
            else:
                print('Please enter a valid option.')


if __name__ == "__main__":
    main()
