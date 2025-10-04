import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
What did you see on line 1?
- The number seen is a random integer between 5 and 20 (inclusive)
What was the smallest number you could have seen, what was the largest?
- minimum possible number is 5
- maximum possible number is 20

What did you see on line 2?
- The number seen is a random odd integer in the sequence starting at 3, incrementing by 2, up to but not including 10.
What was the smallest number you could have seen, what was the largest?
- minimum possible number is 3
- maximum possible number is 9
Could line 2 have produced a 4?
-No, it could not have produced a 4

What did you see on line 3?
- The number seen is a random float between 2.5 and 5.5
What was the smallest number you could have seen, what was the largest?
- minimum possible number is 2.5
- maximum possible number is 5.5

Write code, not a comment, to produce a random number between 1 and 100 inclusive.
"""
import random
print(random.randint(1, 100))