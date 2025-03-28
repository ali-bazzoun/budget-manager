from controllers.budget_controller import BudgetController

class BudgetManager:
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.budget_controller = BudgetController()
        self.monthly_budgets = self.budget_controller.get_all_budgets(user_id)
        self.number_of_months = len(self.monthly_budgets)
        self.total_income = sum(budget.income for budget in self.monthly_budgets)
        self.total_category_allocations = self.calculate_category_allocations([budget.category_allocations for budget in self.monthly_budgets])
        self.total_unallocated_funds = self.total_income - sum(self.total_category_allocations.values())
        self.estimated_expenses = self.calculate_estimated_yearly_expenses(self.total_category_allocations, ['electricity', 'rent'], self.number_of_months)
        self.dream_salary = self.calculate_dream_salary(self.total_income, self.number_of_months)

    def refresh(self):
        self.monthly_budgets = self.budget_controller.get_all_budgets(self.user_id)
        self.number_of_months = len(self.monthly_budgets)
        self.total_income = sum(budget.income for budget in self.monthly_budgets)
        self.total_category_allocations = self.calculate_category_allocations([budget.category_allocations for budget in self.monthly_budgets])
        self.total_unallocated_funds = self.total_income - sum(self.total_category_allocations.values())
        self.estimated_expenses = self.calculate_estimated_yearly_expenses(self.total_category_allocations, ['electricity', 'rent'], self.number_of_months)
        self.dream_salary = self.calculate_dream_salary(self.total_income, self.number_of_months)

    def calculate_category_allocations(self, category_allocations_list: list[dict[str, float]]) -> dict[str, float]:
        total_allocations = {}
        for allocations in category_allocations_list:
            for key, value in allocations.items():
                total_allocations[key] = total_allocations.get(key, 0) + value
        return total_allocations
        
    def calculate_estimated_yearly_expenses(self, total_category_allocations: dict[str, float],  categories: list[str], number_of_months: int) -> float:
        if number_of_months == 0:
            return 0
        estimated_yearly_expenses = 0
        for category in categories:
            estimated_yearly_expenses += (total_category_allocations.get(category, 0) / number_of_months) * 12
        return estimated_yearly_expenses
    
    def calculate_dream_salary(self, total_income: float, number_of_months: int) -> int:
        if number_of_months == 0:
            return 0
        return int((total_income / number_of_months)**2)

    def get_list_of_all_budgets(self) -> list[list] | None:
        if not self.monthly_budgets:
            return None
        return [budget.get_list() for budget in self.monthly_budgets]
    
    def __str__(self) -> str:

        if not self.monthly_budgets:
            return "\nNO BUDGETS FOUND!"
        
        result = []
        
        # 1. Total Income
        result.append(f"Total Income across all months: ${self.total_income:,.2f}")
        # 2. Category Allocations (Total across all months)
        result.append("Total Allocations across all months:")
        for category, allocation in self.total_category_allocations.items():
            result.append(f"  - {category.capitalize()}: ${allocation:,.2f}")
        # 3. Unallocated Funds across all months
        result.append(f"Total Unallocated Funds: ${self.total_unallocated_funds:,.2f}")
        # 4. Estimated Yearly Expenses (for Rent and Electricity)
        result.append(f"Estimated Yearly Expenses for Rent and Electricity: ${self.estimated_expenses:,.2f}")
        # 5. Remaining Balance
        result.append(f"Remaining Balance: ${self.total_income - self.total_category_allocations['rent'] - self.total_category_allocations['electricity']:,.2f}")
        # 6. Dream Salary
        result.append(f"Your Dream Salary (based on monthly income): ${self.dream_salary:,.2f}")
        
        return "\n".join(result)