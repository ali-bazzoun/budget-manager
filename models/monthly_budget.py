
class MonthlyBudget:
    def __init__(self, user_id: int, month: str, income: float, category_percentages: dict[str, float]):
        if income < 0:
            raise ValueError("Total income cannot be negative.")
        
        total_percentage = sum(category_percentages.values())
        if total_percentage > 100:
            raise ValueError("Total category allocations cannot exceed 100%.")

        self.user_id = user_id
        self.month = month
        self.income = income
        self.category_percentages = category_percentages

        # Calculate monetary allocations for each category
        self.category_allocations = {
            category: (percentage / 100) * income
            for category, percentage in category_percentages.items()
        }

        # Calculate unallocated funds
        self.unallocated_funds = income - sum(self.category_allocations.values())

        # Calculate estimated expenses (electricity and rent)
        self.estimated_expenses = (self.category_allocations['electricity'] + self.category_allocations['rent']) * 12

    def __str__(self):
        result = []

        result.append(f"Budget for {self.month.capitalize()}:")

        # 1. Total Income
        result.append(f"Total Income: ${self.income:,.2f}")
        # 2. Category Allocations
        result.append(f"Total Allocations across {self.month.capitalize()}:")
        for category, allocation in self.category_allocations.items():
            result.append(f"  - {category.capitalize()}: ${allocation:,.2f}")
        # 3. Unallocated Funds
        result.append(f"Unallocated Funds: ${self.unallocated_funds:,.2f}")
        # 4. Estimated Yearly Expenses (for Rent and Electricity) according to this month
        result.append(f"Estimated Yearly Expenses (for Rent and Electricity) according to {self.month.capitalize()}: ${self.estimated_expenses:,.2f}")
        # 5. Remaining Balance
        result.append(f"Remaining Balance: ${self.income - self.category_allocations['rent'] - self.category_allocations['electricity']:,.2f}")
        # 6. Dream Salary
        result.append(f"Your Dream Salary (based on {self.month.capitalize()} income): ${self.income**2:,.2f}")

        return "\n".join(result)
    
    
    def get_list(self):
        return [
            self.month,
            self.income,
            f'{self.category_allocations['savings']:,.2f} ({self.category_percentages['savings']:.1f}%)',
            f'{self.category_allocations['rent']:,.2f} ({self.category_percentages['rent']:.1f}%)',
            f'{self.category_allocations['electricity']:,.2f} ({self.category_percentages['electricity']:.1f}%)',
            self.unallocated_funds,
        ]