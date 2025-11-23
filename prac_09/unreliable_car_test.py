"""
Test program for unreliableCar class
"""
import random
from unreliable_car import UnreliableCar

def test_unreliable_car_probability():
    """Test the probabilistic drive functionality of UnreliableCar with multiple iterations."""
    random.seed(789)
    # test vehicles with 30% reliability
    car = UnreliableCar("30% Car", 10000, 30.0)
    total_attempts = 5000
    total_driven = 0

    for i in range(total_attempts):
        total_driven += car.drive(1)

    driven_ratio = total_driven / total_attempts
    print(f"30% reliability car: drove {total_driven}km out of {total_attempts} attempts.")
    print(f"Actual ratio: {driven_ratio:.2%} (expected ~30%)")
    assert 0.25 <= driven_ratio <= 0.35, "30% reliability test failed"

    # test vehicles with 100% reliability
    car = UnreliableCar("100% Car", 100, 100.0)
    total_driven = 0
    for j in range(10):
        total_driven += car.drive(5)
    assert total_driven == 50, "100% reliability test failed"
    print("100% reliability car: drove all attempted distance.")

    # test vehicles with 0% reliability
    car = UnreliableCar("0% Car", 100, 0.0)
    total_driven = 0
    for k in range(10):
        total_driven += car.drive(5)
    assert total_driven == 0, "0% reliability test failed"
    print("0% reliability car: drove 0km in all attempts.")

    print("\nAll UnreliableCar probability tests passed!")



test_unreliable_car_probability()