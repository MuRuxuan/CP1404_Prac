"""
Test program for SilverServiceTaxi class
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    """Test the SilverServiceTaxi class inheritance, fancy pricing and flagfall."""

    fancy_taxi = SilverServiceTaxi("Hummer", 200.0, 2.0)
    print("1. Initial silverServiceTaxi state: ")
    print(fancy_taxi)
    assert fancy_taxi.name == "Hummer"
    assert fancy_taxi.fuel == 200.0
    assert fancy_taxi.fanciness == 2.
    assert fancy_taxi.price_per_km == 1.23 * 2.0
    assert fancy_taxi.flagfall == 4.50

    print("\n2. Driving 18km: ")
    fancy_taxi.drive(18)
    fare = fancy_taxi.get_fare()
    print(f"Total fare for 18km: ${fare}")
    assert fare == 48.78, f"Expected fare $48.78, got ${fare}"

    print("\n3. Restarting fare and driving 10km:")
    fancy_taxi.start_fare()  # 修正：fancy.taxi → fancy_taxi
    fancy_taxi.drive(10)
    fare = fancy_taxi.get_fare()
    print(f"Total fare for 10km: ${fare}")
    # Expected cost: 4.50 + (1.23×2×10) = 4.50 + 24.60 = 29.10
    assert fare == 29.10, f"Expected fare $29.10, got ${fare}"

    print("\n4. Testing parent class price_per_km update:")
    original_price_per_km = Taxi.price_per_km
    Taxi.price_per_km = 1.50
    new_fancy_taxi = SilverServiceTaxi(name="Tesla", fuel=150.0, fanciness=1.5)
    assert new_fancy_taxi.price_per_km == 1.50 * 1.5
    print(f"New SilverServiceTaxi price_per_km: ${new_fancy_taxi.price_per_km:.2f} (expected $2.25)")
    Taxi.price_per_km = original_price_per_km

    print("\n5. Fuel limit test (driving 200km with 200L fuel):")
    fancy_taxi2 = SilverServiceTaxi(name="Range Rover", fuel=200.0, fanciness=3.0)
    fancy_taxi2.drive(200)
    fare = fancy_taxi2.get_fare()
    print(f"Total fare for 200km: ${fare}")
    # Expected cost：4.50 +（1.23×3×200）= 4.50 + 738.00 = 742.50
    assert fare == 742.50, f"Expected fare $742.50, got ${fare}"

    print("\nAll SilverServiceTaxi tests passed!")

test_silver_service_taxi()


