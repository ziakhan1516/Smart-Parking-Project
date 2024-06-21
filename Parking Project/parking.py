from parking_project import*

# Initialize parking lots if they haven't been initialized
parking_lot_1, parking_lot_2, lot1_reserved, lot2_reserved, parking_size = parking_project()

def parking(number):
    """
    Parks a car in one of the two parking lots.

    This function attempts to park a car in the first available row of either parking lot 1 or parking lot 2.
    It prioritizes parking lot 1 if both lots have available space in the same row.

    Parameters:
    number (int): The car number to be parked.

    Returns:
    str: A message indicating where the car was parked, or if both parking lots are full.
    """
    global parking_lot_1, parking_lot_2
    
    for (park1_index, park1_row), (park2_index, park2_row) in zip(enumerate(parking_lot_1), enumerate(parking_lot_2)):
        if len(park1_row) < parking_size and len(park1_row) <= len(park2_row):
            parking_lot_1[park1_index].insert(0, number)
            return f"Parked in parking lot 1 car number {number}, Row number {park1_index}"
        elif len(park2_row) < parking_size:
            parking_lot_2[park2_index].insert(0, number)
            return f"Parked in parking lot 2 car number {number}, Row number {park2_index}"
    return "Both parking lots are full"
