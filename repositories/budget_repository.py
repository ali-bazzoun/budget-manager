from sqlite3 import Error
from database import execute_query
from models import MonthlyBudget


class BudgetRepository:


    def save(self, budget: MonthlyBudget) -> bool:
        user_id = budget.user_id
        month = budget.month
        income = budget.income
        category_percentages = budget.category_percentages
        savings_percent = category_percentages.get('savings', 0)
        rent_percent = category_percentages.get('rent', 0)
        electricity_percent = category_percentages.get('electricity', 0)

        query = """--sql
        INSERT OR REPLACE INTO budgets
        (user_id, month, income, savings_percent, rent_percent, electricity_percent)
        VALUES (?,?,?,?,?,?)
        """
        
        try:
            execute_query(
                query,
                (user_id, month, income, savings_percent, rent_percent, electricity_percent),
                commit=True
            )
            return True
        except Error as e:
            print(f"Error saving budget data: {e}")


    def get(self, user_id: int, month: str | None = None) -> MonthlyBudget | list[MonthlyBudget] | None:
        """
        Retrieve budget data for a specified user and month (if provided) and return as MonthlyBudget object.
        If month is None, return a list of MonthlyBudget objects for the user.
        """
        if month:
            query = """--sql
            SELECT id, user_id, month, income, savings_percent, rent_percent, electricity_percent, created_at
            FROM budgets
            WHERE user_id = ? AND month = ?
            """
            result = execute_query(query, (user_id, month), fetch_one=True)
            
            if result:
                category_percentages = {
                    'savings': result[4],
                    'rent': result[5],
                    'electricity': result[6]
                }
                return MonthlyBudget(
                    user_id=user_id,
                    month=result[2],
                    income=result[3],
                    category_percentages=category_percentages
                )
            return None
        else:
            query = """--sql
            SELECT id, user_id, month, income, savings_percent, rent_percent, electricity_percent, created_at
            FROM budgets
            WHERE user_id = ?
            ORDER BY created_at DESC
            """
            results = execute_query(query, (user_id,), fetch_all=True)
            
            if results:
                return [
                    MonthlyBudget(
                        user_id=row[1],
                        month=row[2],
                        income=row[3],
                        category_percentages={
                            'savings': row[4],
                            'rent': row[5],
                            'electricity': row[6]
                        }
                    ) for row in results
                ]
            return []


    def delete(self, user_id: int, month: str) -> bool:
        """
        Delete a budget entry for a specific user and month.
        """
        query = "DELETE FROM budgets WHERE user_id = ? AND month = ?"
        result = execute_query(query, (user_id, month), commit=True)
        return result > 0
