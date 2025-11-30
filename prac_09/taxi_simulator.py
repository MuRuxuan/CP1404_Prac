"""Taxi Simulator Program."""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "q":
            break
        elif choice == "c":
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            total_bill += handle_drive(current_taxi)
        else:
            print("Invalid option")

        display_current_bill(total_bill)

    display_final_summary(total_bill, taxis)


def display_menu():
    """Display the main menu options."""
    print("q)uit, c)hoose taxi, d)rive")


def get_user_choice():
    """
    Get and return the user's menu choice.

    Returns:
        str: The user's choice in lowercase
    """
    return input(">>> ").lower()


def choose_taxi(taxis):
    """
    Display available taxis and let user choose one.

    Args:
        taxis (list): List of available taxi objects

    Returns:
        Taxi or None: The selected taxi object or None if invalid choice
    """
    print("Taxis available: ")
    display_taxis(taxis)

    try:
        choice = int(input("Choose taxi: "))
        selected_taxi = taxis[choice]
        selected_taxi.start_fare()
        print(f"You chose {selected_taxi.name}")
        return selected_taxi
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def display_taxis(taxis):
    """
    Display all taxis with their index numbers.

    Args:
        taxis (list): List of taxi objects to display
    """
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def handle_drive(current_taxi):
    """
    Handle the driving process for the selected taxi.

    Args:
        current_taxi (Taxi): The currently selected taxi

    Returns:
        float: The fare amount for the trip (0 if invalid)
    """
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0
    else:
        return drive_taxi(current_taxi)


def drive_taxi(taxi):
    """
    Drive the selected taxi and return the fare.

    Args:
        taxi (Taxi): The taxi to drive

    Returns:
        float: The fare amount for the trip
    """
    try:
        distance = float(input("Drive how far? "))
        if distance <= 0:
            print("Distance must be positive")
            return 0.0

        taxi.drive(distance)
        fare = taxi.get_fare()
        print(f"Your {taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance")
        return 0.0


def display_current_bill(total_bill):
    """
    Display the current total bill.

    Args:
        total_bill (float): The current total bill amount
    """
    print(f"Bill to date: ${total_bill:.2f}")


def display_final_summary(total_bill, taxis):
    """
    Display the final summary after quitting.

    Args:
        total_bill (float): The final total bill amount
        taxis (list): List of all taxi objects
    """
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


if __name__ == "__main__":
    main()