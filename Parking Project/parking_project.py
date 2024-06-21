def parking_project():
    global parking_lot_1, parking_lot_2, lot1_reserved, lot2_reserved, parking_size
    if 'parking_lot_1' not in globals():
        parking_lot_1 = [[] for _ in range(4)]  # Creates a 2D list representing parking lot 1 with 4 rows
    if 'parking_lot_2' not in globals():
        parking_lot_2 = [[] for _ in range(4)]  # Creates a 2D list representing parking lot 2 with 4 rows
    if 'lot1_reserved' not in globals():
        lot1_reserved = []  # Initializes an empty list for reserved spots in parking lot 1
    if 'lot2_reserved' not in globals():
        lot2_reserved = []  # Initializes an empty list for reserved spots in parking lot 2
    if 'parking_size' not in globals():
        parking_size = 4  # Sets the maximum number of parking slots per row in each lot

    return parking_lot_1, parking_lot_2, lot1_reserved, lot2_reserved, parking_size
