MIN_LENGTH = 8
de


    password = get_password()
    print_asterisks(password)

def get_password():
    password = input("Enter password: ")
    while len(password) < MIN_LENGTH:
        print(f'Password must be at least {MIN_LENGTH} characters long')
        password = input("Enter password: ")
    return password
def print_asterisks(password):
    print('*' * len(password))