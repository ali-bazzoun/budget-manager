from typing import List


def print_table(data: List[List]):
    # Find the maximum length for each column
    column_widths = [max(len(str(item)) for item in column) for column in zip(*data)]
    
    # Print the header row
    for i, header in enumerate(data[0]):
        print(f"{header:{column_widths[i]}}", end=" | ")
    print("\n" + "-" * (sum(column_widths) + len(column_widths) * 3 - 1))  # Divider line
    
    # Print the data rows
    for row in data[1:]:
        for i, cell in enumerate(row):
            print(f"{cell:{column_widths[i]}}", end=" | ")
        print()

# # Example data
# data = [
#     ["ID", "Name", "Age"],
#     [1, "Alice", 30],
#     [2, "Bob", 25],
#     [3, "Charlie", 35],
#     [4, "David", 28]
# ]
# 
# # Call the function to print the table
# print_table(data)
# 
# 
# 
# ID  | Name    | Age  | 
# -------------------------
# 1   | Alice   | 30   | 
# 2   | Bob     | 25   | 
# 3   | Charlie | 35   | 
# 4   | David   | 28   | 

