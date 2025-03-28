from views.table_printer import TablePrinter

class MenuUI:
    """Class handling all menu displays and user input."""
    
    def display_auth_menu(self):
        """Display the authentication menu options and get user choice."""
        print('\n===== Budget Manager =====')
        print('1. Register')
        print('2. Login')
        print('3. Exit')
        return input('Choose an option: ').strip()
    
    def display_main_menu(self, username):
        """Display the main menu options for logged-in users and get user choice."""
        print(f'\n===== Budget Manager - Welcome, {username} =====')
        print('1. Budget Menu')
        print('2. User Account Settings')
        print('3. Logout')
        print('4. Exit')
        return input('Choose an option: ').strip()
    
    def display_budget_menu(self, budget_manager):
        """Display the budget menu options and get user choice."""
        headers = ['month', 'income', 'savings', 'rent', 'electricity', 'unallocated']
        rows=budget_manager.get_list_of_all_budgets()

        print('\n===== Budget Menu =====')

        if rows:  
            table = TablePrinter(headers=headers, rows=rows).generate_table()
            print('\n' + table + '\n')
        else:
            print("\nNO BUDGETS FOUND!\n")

        print('1. Add Budget')
        print('2. View Total Budget Summary')
        print('3. View Budget for a Specific Month')
        print('4. Edit Budget for a Specific Month')
        print('5. Return to Main Menu')
        return input('Choose an option: ').strip()
    
    def display_user_account_menu(self):
        """Display the user account management menu and get user choice."""
        update_fields = {
            '1': 'username',
            '2': 'first name',
            '3': 'last name',
            '4': 'password',
        }

        print('\n===== User Account Settings =====')
        for key, value in update_fields.items():
            print(f'{key}. Edit {value}')
        print('5. Delete account')
        print('6. Return to main menu')

        choice = input('Choose an option: ').strip()

        if choice in update_fields:
            new_value = input(f'Enter new {update_fields[choice]}: ').strip()
            return choice, new_value

        return choice, None
    
    def display_budget_edit_menu(self):
        """Display the user account management menu and get user choice."""
        month = input('Enter month: ').strip().lower()
        update_fields = {
            '1': 'income',
            '2': 'savings_percentage',
            '3': 'rent_percentage',
            '4': 'electricity_percentage'
        }

        print(f'\n===== {month.capitalize()} Budget Settings =====')
        for key, value in update_fields.items():
            print(f'{key}. Edit {value}')
        print('5. Delete budget')
        print('6. Return to Budget menu')

        choice = input('Choose an option: ').strip()

        if choice in update_fields:
            new_value = input(f'Enter new {update_fields[choice]}: ').strip()
            return month, choice, new_value

        return month, choice, None
    
    def display_budget_form(self, user_id: int):
        """Display the budget creation form and get user input."""
        print("\n----- Add a New Budget -----")
        month = input("Enter month: ").strip()
        income = float(input("Enter your income: ").strip())
        
        category_percentages = {}
        category_percentages['rent'] = float(input("Enter Rent percentage: ").strip())
        category_percentages['electricity'] = float(input("Enter Electricity percentage: ").strip())
        category_percentages['savings'] = float(input("Enter Savings percentage: ").strip())
        
        return user_id, month, income, category_percentages
    
    def get_registration_details(self):
        """Get user registration details."""
        print("\n----- User Registration -----")
        username = input('Username: ').strip()
        password = input('Password: ').strip()
        firstname = input('First name: ').strip()
        lastname = input('Last name: ').strip()
        
        return username, password, firstname, lastname
    
    def get_login_details(self):
        """Get user login details."""
        print("\n----- User Login -----")
        username = input('Username: ').strip()
        password = input('Password: ').strip()
        
        return username, password