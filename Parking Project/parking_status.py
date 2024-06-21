from tabulate import tabulate
from parking_project import*
parking_lot_1, parking_lot_2, lot1_reserved, lot2_reserved, parking_size = parking_project()

def parking_status():
    def colorize(text, color):
        """
        Function to wrap text with ANSI color codes.
        """
        colors = {
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
        }
        return f"{colors.get(color, '')}{text}\033[0m"

    print("Parking Lot 1 Status:")
    table1 = []
    for i, row in enumerate(parking_lot_1):
        row_data = []
        for j in range(parking_size):
            if j < len(row):
                row_data.append(row[j])  # Display the actual data in the slot
            else:
                row_data.append("0")  # Display '0' instead of 'Empty'
        table1.append([colorize(f"Row {i}", 'green')] + row_data)

    print(tabulate(table1, headers=[colorize(f"Slot {j}", 'cyan') for j in range(parking_size)], tablefmt="grid"))

    print("\nParking Lot 2 Status:")
    table2 = []
    for i, row in enumerate(parking_lot_2):
        row_data = []
        for j in range(parking_size):
            if j < len(row):
                row_data.append(row[j])  # Display the actual data in the slot
            else:
                row_data.append("0")  # Display '0' instead of 'Empty'
        table2.append([colorize(f"Row {i}", 'green')] + row_data)

    print(tabulate(table2, headers=[colorize(f"Slot {j}", 'cyan') for j in range(parking_size)], tablefmt="grid"))

    print("\nReserved Lot 1:")
    reserved_lot1_table = []
    for i in range(4):
        if i < len(lot1_reserved):
            reserved_lot1_table.append([colorize(f"Slot {i}", 'magenta'), lot1_reserved[i]])  # Display the actual data in the slot
        else:
            reserved_lot1_table.append([colorize(f"Slot {i}", 'magenta'), "0"])  # Display '0' instead of 'Empty'

    print(tabulate(reserved_lot1_table, headers=[colorize("Slot", 'cyan'), colorize("Car", 'cyan')], tablefmt="grid"))

    print("\nReserved Lot 2:")
    reserved_lot2_table = []
    for k in range(4):
        if k < len(lot2_reserved):
            reserved_lot2_table.append([colorize(f"Slot {k}", 'magenta'), lot2_reserved[k]])  # Display the actual data in the slot
        else:
            reserved_lot2_table.append([colorize(f"Slot {k}", 'magenta'), "0"])  # Display '0' instead of 'Empty'

    print(tabulate(reserved_lot2_table, headers=[colorize("Slot", 'cyan'), colorize("Car", 'cyan')], tablefmt="grid"))

    print("*" * 100)  # Remove extra parenthesis
