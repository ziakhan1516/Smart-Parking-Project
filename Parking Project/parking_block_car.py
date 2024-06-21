from parking_project import*
parking_lot_1, parking_lot_2, lot1_reserved, lot2_reserved, parking_size = parking_project()

def parking_block_car(block_car, sorted_index, car_row, lot):
    for short_indexes in sorted_index:
        for (park1_index, park1_row), (park2_index, park2_row) in zip(enumerate(parking_lot_1), enumerate(parking_lot_2)):
            if lot == 1:
                if park1_index == short_indexes and park1_index != car_row and len(park1_row) < parking_size and len(park1_row) <= len(park2_row):
                    parking_lot_1[park1_index].insert(0, block_car)
                    print(f"Block car Parked in parking lot 1 car number {block_car}, Row number {park1_index}")
                    return (f"Block car Parked in parking lot 1 car number {block_car}, Row number {park1_index}")
                elif park2_index == short_indexes and len(park2_row) < parking_size:
                    parking_lot_2[park2_index].insert(0, block_car)
                    print(f"Block car Parked in parking lot 2 car number {block_car}, Row number {park2_index}")
                    return (f"Block car Parked in parking lot 2 car number {block_car}, Row number {park2_index}")

            if lot == 2:
                if park2_index == short_indexes and park2_index != car_row and len(park2_row) < parking_size and len(park2_row) <= len(park1_row):
                    parking_lot_2[park1_index].insert(0, block_car)
                    return (f"Block car Parked in parking lot 2 car number {block_car}, Row number {park2_index}")
                elif park1_index == short_indexes and len(park1_row) < parking_size:
                    parking_lot_1[park1_index].insert(0, block_car)
                    print(f"Block car Parked in parking lot 1 car number {block_car}, Row number {park1_index}")
                    return (f"Block car Parked in parking lot 1 car number {block_car}, Row number {park1_index}")
    if len(lot1_reserved) < parking_size:
        lot1_reserved.insert(0, block_car)
        print(f"Block car Parked in reserved lot 1 car number {block_car}, Slot Number {len(lot1_reserved)}")
        return (f"Block car Parked in reserved lot 1 car number {block_car}, Slot Number {len(lot1_reserved)}")
    elif len(lot2_reserved) < parking_size:
        lot2_reserved.insert(0, block_car)
        print(f"Block Car Parked in reserved lot 2 car number {block_car}, Slot Number {len(lot2_reserved)}")
        return (f"Block Car Parked in reserved lot 2 car number {block_car}, Slot Number {len(lot2_reserved)}")
    else:
        return "Both regular and reserved parking lots are full"
