minimum_length = 6

def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    """get a valid password"""
    password = input(f"Enter your password (no shorter than {minimum_length} characters):")
    while len(password) < minimum_length:
        print("Invalid")
        password = input(f"Enter your password (no shorter than {minimum_length} characters):")
    return password

def print_asterisks(password):
    """Print a line of asterisks with the length of password"""
    print("password hidden:" + len(password) * "*")

main()

