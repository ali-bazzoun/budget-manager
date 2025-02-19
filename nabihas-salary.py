class Nabiha:
    
    def __init__(self, month, salary, savings, rent, electricity):
        self.month = month
        self.salary = salary
        self.percentages = {'Savings': savings, 'Rent': rent, 'Electricity': electricity}

    def basic_calculations(self):
        self.allocated_amounts = {
            'Savings': (savings / 100) * salary,
            'Rent': (rent / 100) * salary,
            'Electricity': (electricity / 100) * salary
            }
        self.total_spent = sum(self.allocated_amounts.values())
        self.reminder = self.salary - self.total_spent
        
    def year_estimation(self):
        self.year_estimations = {}
        for key in self.allocated_amounts:
            self.year_estimations[key] = self.allocated_amounts[key] * 12

    def fun(self):
        self.fun_salary = self.salary * self.salary

    def preview_results(self):
        # The amount allocated to savings, rent, and electricity.
        for key in self.allocated_amounts:
            print(f'The amount allocated to {key}: {self.allocated_amounts[key]}')
        # The total amount Nabiha spends on savings, rent, and electricity combined.
        print(f'The total amount spent on savings, rent, and electricity combined: {self.total_spent}')
        # The remainder of Nabiha’s salary after these expenses.
        print(f'The remainder salary: {self.reminder}')
        #  The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
        print(f'The estimated yearly rent and electricity costs: {self.year_estimations["Rent"] + self.year_estimations["Electricity"]}')
        # Nabiha's total salary for the month raised to the power of 2 (just for fun).
        print(f'The dream salary :) {self.fun_salary}')

    def run_manager(self):
        self.basic_calculations()
        self.year_estimation()
        self.fun()
        self.preview_results()

month = input('Nabiha, please type the month name: ').capitalize()
salary = float(input(f'Nabiha, please enter your salary for {month}: '))
print('Nabiha, please enter the percentages for the following categories:')
savings = float(input('Savings (%): '))
rent = float(input('Rent (%): '))
electricity = float(input('Electricity (%): '))


nabiha = Nabiha(month=month,
                salary=salary,
                savings=savings,
                rent=rent,
                electricity=electricity)

nabiha.run_manager()

