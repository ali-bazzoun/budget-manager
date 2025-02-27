from models.user import User


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

    def __str__(self):
        return (
            f"Budget for {self.month}:\n"
            f"Total Income: ${self.income:,.2f}\n"
            f"Total Allocated: ${sum(self.category_allocations.values()):,.2f}\n"
            f"Unallocated Funds: ${self.unallocated_funds:,.2f}"
        )

    def summary(self):
        """Returns a detailed breakdown of budget allocations."""
        breakdown = "\n".join(
            f"  - {category}: ${amount:,.2f} ({self.category_percentages[category]:.1f}%)"
            for category, amount in self.category_allocations.items()
        )
        return (
            f"Budget Breakdown for {self.month}:\n{breakdown}\n"
            f"Unallocated Funds: ${self.unallocated_funds:,.2f}"
        )
    
    def get_list(self):
        return [
            self.month,
            self.income,
            f'{self.category_allocations['savings']:,.2f} ({self.category_percentages['savings']:.1f}%)',
            f'{self.category_allocations['rent']:,.2f} ({self.category_percentages['rent']:.1f}%)',
            f'{self.category_allocations['electricity']:,.2f} ({self.category_percentages['electricity']:.1f}%)',
            self.unallocated_funds,
        ]