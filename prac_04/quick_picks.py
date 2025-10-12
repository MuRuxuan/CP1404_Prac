import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6

number_picks = int(input("How many quick picks? "))


for _ in range(number_picks):
    quick_pick = []

    while len(quick_pick) < NUMBERS_PER_PICK:
        random_num = random.randint(MIN_NUMBER, MAX_NUMBER)
        if random_num not in quick_pick:
            quick_pick.append(random_num)

    quick_pick.sort()

    print(" ".join(f"{number:2}" for number in quick_pick))