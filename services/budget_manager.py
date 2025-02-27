from typing import List, Dict
from models.user import User
from models.monthly_budget import MonthlyBudget
from repositories import get_budget_data

class BudgetManager:
    def __init__(self, user: User):
        self.monthly_budgets = get_budget_data(user.user_id)
        self.number_of_months = len(self.monthly_budgets)
        self.total_income = sum(budget.income for budget in self.monthly_budgets)
        self.total_category_allocations = self.calculate_category_allocations([budget.category_allocations for budget in self.monthly_budgets])
        self.total_unallocated_funds = self.total_income - sum(self.total_category_allocations.values())
        self.estimated_expensed = self.calculate_estimated_yearly_expenses(self.total_category_allocations, ['electricity', 'rent'], self.number_of_months)
        self.dream_salary = self.calculate_dream_salary(self.total_income, self.number_of_months)

    def calculate_category_allocations(self, category_allocations_list: List[Dict[str, float]]) -> Dict[str, float]:
        total_allocations = {}
        for allocations in category_allocations_list:
            for key, value in allocations.items():
                total_allocations[key] = total_allocations.get(key, 0) + value
        return total_allocations
        
    def calculate_estimated_yearly_expenses(self, total_category_allocations: Dict[str, float],  categories: List[str], number_of_months: int) -> float:
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

    def get_data(self) -> List[List]:
        return [budget.get_list() for budget in self.monthly_budgets]
    
    def __str__(self) -> str:

        if not self.monthly_budgets:
            return "\nNO BUDGETS FOUND!"
        
        result = []
        
        # 1. Total Income
        result.append(f"Total Income across all months: ${self.total_income:,.2f}")
        
        # 2. Category Allocations (Total across all months)
        result.append("\nTotal Allocations across all months:")
        for category, allocation in self.total_category_allocations.items():
            result.append(f"  - {category.capitalize()}: ${allocation:,.2f}")
        
        # 3. Unallocated Funds across all months
        result.append(f"\nTotal Unallocated Funds: ${self.total_unallocated_funds:,.2f}")
        
        # 4. Estimated Yearly Expenses (for Rent and Electricity)
        result.append(f"\nEstimated Yearly Expenses for Rent and Electricity: ${self.estimated_expensed:,.2f}")
        
        # 5. Dream Salary
        result.append(f"\nYour Dream Salary (based on monthly income): ${self.dream_salary:,.2f}")
        
        return "\n".join(result)
    
        

    
    

        
        



    # def display_results(self):
    #     '''
    #     Previews the calculated results: 
    #         1. allocated amounts
    #         2. total spent
    #         3. remainder
    #         4. yearly estimations
    #         5. fun
    #     '''
    #     # 1 Display the amount allocated to savings, rent, and electricity.
    #     for category, amount in self.allocated_amounts.items():
    #         print(f'The amount allocated to {category}: {self.format_number(amount)}')

    #     # 2 Display the total amount spent on savings, rent, and electricity combined.
    #     print(f'The total amount spent on savings, rent, and electricity combined: {self.format_number(self.total_expenses)}')

    #     # 3 Display the remainder of the salary after these expenses.
    #     print(f'The remainder salary: {self.format_number(self.remaining_balance)}')

    #     # 4 Display the monthly rent and electricity multiplied by 12 to estimate yearly rent and electricity costs.
    #     combined_yearly_expenses = self.yearly_expenses["Rent"] + self.yearly_expenses["Electricity"]
    #     print(f'The estimated yearly rent and electricity costs: {self.format_number(combined_yearly_expenses)}')

    #     # 5 Display total salary for the month raised to the power of 2 (just for fun).
    #     print(f'The dream salary :) {self.format_number(self.dream_salary)}')
