MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit"""

MAXIMUM_SCORE = 100
MINIMUM_SCORE = 0

def main():
    user_score = 0
    print(MENU)
    choice = input("Enter your choice: ").upper()

    while choice != "Q":
        if choice == "G":
            user_score = get_valid_score()
        elif choice == "P":
            user_result = evaluate_score(user_score)
            print(user_result)
        elif choice == "S":
            show_stars(user_score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Farewell")


def get_valid_score():
    """get valid score"""
    score = float(input("Enter your score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = float(input("Enter your score: "))
    return score

def evaluate_score(score):
    """Return the evaluation result based on the score"""
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print the same number of asterisks as the score."""
    print('*'* round(score))
main()