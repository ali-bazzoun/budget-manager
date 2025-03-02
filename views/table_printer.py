class TablePrinter:
    def __init__(self, headers: list[str], rows: list[list]):
        self.headers = headers
        self.rows = rows

    def get_column_widths(self) -> list[int]:
        """Calculates the maximum width needed for each column."""
        table_data = [self.headers] + self.rows
        return [max(len(str(item)) for item in col) for col in zip(*table_data)]

    def format_row(self, row: list, is_header: bool = False) -> str:
        """Formats a row to align columns properly."""
        column_widths = self.get_column_widths()
        if is_header:
            # Center-align headers
            return " | ".join(f"{str(cell):^{column_widths[i]}}" for i, cell in enumerate(row))
        else:
            # Left-align data rows
            return " | ".join(f"{str(cell):<{column_widths[i]}}" for i, cell in enumerate(row))

    def generate_table(self) -> str:
        """Generates and returns the formatted table as a string."""
        column_widths = self.get_column_widths()
        divider = "-" * (sum(column_widths) + len(column_widths) * 3 - 1)

        table_lines = [self.format_row(self.headers, is_header=True), divider]
        table_lines.extend(self.format_row(row) for row in self.rows)

        return "\n".join(table_lines)


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

