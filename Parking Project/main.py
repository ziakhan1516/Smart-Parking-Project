from parking_project import parking_project
from parking import parking
from parking_out import parking_out
from parking_status import parking_status
def main():
    """
    Main function to handle the parking system operations.
    
    This function provides a command-line interface for users to interact with the parking system.
    Users can choose to park a car, remove a car from the parking, check the parking status, or quit the program.
    The function runs in an infinite loop until the user decides to quit.
    """
    # Initialize parking lots and reserved lots
    while True:
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("Enter the Car Number to Park")
            car_number = input("Enter the car number: ")
            print(parking(car_number))
        elif choice == '2':
            print("Parking Out the Car")
            car_number = input("Enter the car number to park out: ")
            print(parking_out(car_number))
        elif choice == '3':
            print("Showing the parking Lots Status")
            parking_status()
        elif choice == '4':
            print("Quitting the program")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
