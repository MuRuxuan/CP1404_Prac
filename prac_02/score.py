"""
CP1404/CP5632 - Practical
Program to determine score status
"""
from random import uniform
minimum_score = 0
maximum_score = 100

def main():
    user_score = float(input("Enter score: "))
    while user_score < minimum_score or user_score > maximum_score:
        print("Invalid score")
        user_score = float(input("Enter score: "))

    user_result = evaluate_score(user_score)
    print(user_result)

    random_score = uniform(minimum_score,maximum_score)
    random_result = evaluate_score(random_score)
    print(f"random_score:{random_score:.1f}\nrandom_result:{random_result}")

def evaluate_score(score):
    """Return the evaluation result based on the score"""
    if score >= 90:
        return"Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"
main()