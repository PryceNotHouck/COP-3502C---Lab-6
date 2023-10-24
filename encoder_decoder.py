# Pryce Houck, Sarah Cedeno

def encoder(password):
    encoded = ""
    temp = 0
    for i in range(len(password)):
        temp = int(password[i]) + 3
        if temp > 9:
            temp -= 10
        encoded += str(temp)
    return encoded


def main():
    running = True
    while running:
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Exit \n")
        valid = False
        while not valid:
            user = input("Please enter an option: ")
            if user == '1':
                password = input("Please enter a password to encode: ")
                password = encoder(password)
                print("Your password has been encoded and stored! \n")
                valid = True
            elif user == '2':
                pass
                valid = True
            elif user == '3':
                valid = True
                running = False
            else:
                print('Please enter a valid option. \n')


if __name__ == "__main__":
    main()
