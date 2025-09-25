minimum_length = 6

def main():
    password = get_password()
    print_asterisks(password)

"""get a valid password"""
def get_password():
    password = input(f"Enter your password (no shorter than {minimum_length} characters):")
    while len(password) < minimum_length:
        print("Password is too short")
        password = input(f"Enter your password (no shorter than {minimum_length} characters):")
    return password

"""Print a line of asterisks with the length of password"""
def print_asterisks(password):
    print("password hidden:" + len(password) * "*")
main()

