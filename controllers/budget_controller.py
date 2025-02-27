from models import MonthlyBudget
from repositories.budget_repository import BudgetRepository


class BudgetController:
    def __init__(self):
        self.budget_repo = BudgetRepository()

    def get_all_budgets(self, user_id: int) -> list[MonthlyBudget] | None:
        """Retrieve all budgets for a specific user."""
        try:
            budgets = self.budget_repo.get(user_id)
            if not budgets:
                return None
            return budgets
        except Exception as e:
            print(e)
            return None

    def get_budget_by_id(self, user_id: int, month: str) -> MonthlyBudget | None:
        """Retrieve a specific budget by user ID and month."""
        try:
            budget = self.budget_repo.get(user_id, month)
            if not budget:
                return None
            return budget
        except Exception as e:
            print(e)
            return None
        

    def create_budget(
            self,
            user_id: int,
            month: str,
            income: float,
            category_percentages: dict[str, float]
            ) -> bool:
        
        budget = MonthlyBudget(
            user_id=user_id,
            month=month,
            income=income,
            category_percentages=category_percentages
        )
        return self.budget_repo.save(budget)
            
        
    def delete_budget(self, user_id: int, month: str) -> bool:     
        return self.budget_repo.delete(user_id, month)