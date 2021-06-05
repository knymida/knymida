# Password is a list. So that in the later development,
# a feature to change the password can be introduced.
password = ['0530']
chances = 3
user_input = str(input("Enter Password to login: "))


def login_working():
    """This block will execute when user has entered the right password."""

    def mul(a, b):
        return a * b

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def div(a, b):
        return a / b

    print("""
1. Enter 'sum' to add two integers
2. Enter 'sub' to subtract one integer from another.
3. Enter 'div' to divide one integer by another.
4. Enter 'mul' to multiply two integers
""")

    # Here the user will enter which operation he intends to perform.
    # Response will be converted into lowercase strings
    # If the initial_response is not present as one of the keys in allowed_response,
    # program will print "Wrong input" and will terminate.
    initial_response = str(input("Your response: ").lower())

    # allowed_response is a dictionary, in which values of the corresponding
    # keys are the referenced to the functions defined above.
    allowed_response = {'sum': add, 'sub': sub, 'div': div, 'mul': mul}
    if initial_response in allowed_response:
        try:
            n1 = int(input('Enter first number: '))
            n2 = int(input('Enter second number: '))
        except TypeError:
            print("Only integers allowed. ")
        except ValueError:
            print("Only integers allowed. ")
        else:
            print("\nThe answer is :", allowed_response[initial_response](n1, n2))

            def another():
                another_input = str(input("\nDo you want to perform another operation? "
                                          "\nEnter 'yes' or 'no': ")).lower()
                while another_input == 'yes' or another_input == 'no':
                    if another_input == "yes":
                        login_working()
                    elif another_input == "no":
                        print('\nA legend once said - "THAND AUR BEZZATI JITNI MEHSOOS KARO UTNI LAGTI HAI".'
                              '\nThanks for operating MIXING.OS')
                        break
                    break
                else:
                    print("Invalid Input")
                    return another()
            another()
    else:
        print("Invalid input")
        login_working()


while user_input != password[0]:
    chances -= 1

    if chances != 0:
        print(f'Wrong password, {chances} chances left!! ')
        user_input = str(input("Enter Password to login: "))
        if user_input != password[0]:
            continue

        elif user_input == password[0]:
            print("\n   Welcome to MIXING.OS ")
            login_working()
        break

    else:
        print("\nChances Exhausted!! MIXING.OS shutting down. ")
        break
else:
    print("\n   Welcome to MIXING.OS ")
    login_working()
