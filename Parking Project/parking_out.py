from parking_project import*
parking_lot_1, parking_lot_2, lot1_reserved, lot2_reserved, parking_size = parking_project()
from parking_block_car import parking_block_car

def parking_out(number):
    lot_1 = 1
    lot_2 = 2
    found = False

    for park1_index, park1_list in enumerate(parking_lot_1):
        if number in park1_list:
            print(f"Car is found in parking lot 1 at index {park1_list.index(number)}, row number {park1_index}")
            index = park1_list.index(number)
            if index == 0:
                parking_lot_1[park1_index].remove(number)
                return f"Car {number} has been successfully removed from parking lot 1"
            else:
                diff = [(i, abs(park1_index - i)) for i in range(len(parking_lot_1))]
                sorted_diff = sorted(diff, key=lambda x: x[1])
                sorted_index = [idx for idx, _ in sorted_diff]
                for i in range(len(park1_list)):
                    block_car = parking_lot_1[park1_index].pop(0)
                    if block_car == number:
                        return f"Car {number} has been successfully removed from parking lot 1"
                    else:
                        parking_block_car(block_car, sorted_index, park1_index, lot_1)
            found = True

    for park2_index, park2_list in enumerate(parking_lot_2):
        if number in park2_list:
            print(f"Car is found in parking lot 2 at index {park2_list.index(number)}, row number {park2_index}")
            index = park2_list.index(number)
            if index == 0:
                parking_lot_2[park2_index].remove(number)
                return f"Car {number} has been successfully removed from parking lot 2"
            else:
                diff = [(i, abs(park2_index - i)) for i in range(len(parking_lot_2))]
                sorted_diff = sorted(diff, key=lambda x: x[1])
                sorted_index = [idx for idx, _ in sorted_diff]
                for i in range(len(park2_list)):
                    block_car = parking_lot_2[park2_index].pop(0)
                    if block_car == number:
                        return f"Car {number} has been successfully removed from parking lot 2"
                    else:
                        parking_block_car(block_car, sorted_index, park2_index, lot_2)
            found = True
    if not found:
        return f"Car {number} is not present in either parking lot 1 or parking lot 2"
