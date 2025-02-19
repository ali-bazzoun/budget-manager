class BudgetManager:
    def __init__(self, month, salary, savings_percent, rent_percent, electricity_percent):
        self.month = month
        self.salary = salary
        self.percentages = {
            'Savings': savings_percent,
            'Rent': rent_percent,
            'Electricity': electricity_percent
        }

    def calculate_allocated_amounts(self):
        '''
        Calculate allocated amounts, total spent, remainder
        '''
        self.allocated_amounts = {
            category: (percentage / 100) * self.salary
            for category, percentage in self.percentages.items()
        }
        self.total_expenses = sum(self.allocated_amounts.values())
        self.remaining_balance = self.salary - self.total_expenses
        
    def estimate_yearly_expenses(self):
        self.yearly_expenses = {
            category: amount * 12
            for category, amount in self.allocated_amounts.items()
        }

    def calculate_fun_salary(self):
        self.dream_salary = self.salary * self.salary

    def format_number(self, num):
        if num.is_integer():
            return int(num)
        return f"{num:.2f}"

    def display_results(self):
        '''
        Previews the calculated results: 
            1. allocated amounts
            2. total spent
            3. remainder
            4. yearly estimations
            5. fun
        '''
        # 1 Display the amount allocated to savings, rent, and electricity.
        for category, amount in self.allocated_amounts.items():
            print(f'The amount allocated to {category}: {self.format_number(amount)}')

        # 2 Display the total amount spent on savings, rent, and electricity combined.
        print(f'The total amount spent on savings, rent, and electricity combined: {self.format_number(self.total_expenses)}')

        # 3 Display the remainder of the salary after these expenses.
        print(f'The remainder salary: {self.format_number(self.remaining_balance)}')

        # 4 Display the monthly rent and electricity multiplied by 12 to estimate yearly rent and electricity costs.
        combined_yearly_expenses = self.yearly_expenses["Rent"] + self.yearly_expenses["Electricity"]
        print(f'The estimated yearly rent and electricity costs: {self.format_number(combined_yearly_expenses)}')

        # 5 Display total salary for the month raised to the power of 2 (just for fun).
        print(f'The dream salary :) {self.format_number(self.dream_salary)}')

    def run(self):
        self.calculate_allocated_amounts()
        self.estimate_yearly_expenses()
        self.calculate_fun_salary()
        self.display_results()


if __name__ == '__main__':
    month = input('Nabiha, please type the month name: ').strip().capitalize()
    salary = float(input(f'Nabiha, please enter your salary for {month}: ').strip())
    print('Nabiha, please enter the percentages for the following categories:')
    savings_percent = float(input('Savings (%): ').strip())
    rent_percent = float(input('Rent (%): ').strip())
    electricity_percent = float(input('Electricity (%): ').strip())

    nabiha = BudgetManager(
        month=month,
        salary=salary,
        savings_percent=savings_percent,
        rent_percent=rent_percent,
        electricity_percent=electricity_percent
    )
    nabiha.run()
