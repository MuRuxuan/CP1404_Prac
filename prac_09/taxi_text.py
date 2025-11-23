"""
Client code to test the Taxi class with specific requirements
"""
from taxi import Taxi
my_taxi = Taxi("Prius 1", 100)
my_taxi.drive(40)
print("After driving 40km:")
print(my_taxi)
print(f"Current fare:${my_taxi.get_fare():.2f}\n")

my_taxi.start_fare()
my_taxi.drive(100)

print("After restarting fare and driving 100km:")
print(my_taxi)
print(f"Current fare:${my_taxi.get_fare():.2f}\n")