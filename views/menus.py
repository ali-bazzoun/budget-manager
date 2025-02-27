# views/menus.py - Menu display and user input handling

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
        print('1. Add Budget')
        print('2. View Budgets')
        print('3. User account settings')
        print('4. Logout')
        print('5. Exit')
        return input('Choose an option: ').strip()
    
    def display_user_account_menu(self):
        """Display the user account management menu and get user choice."""
        print('\n===== User Account Settings =====')
        print('1. Edit username')
        print('2. Edit first name')
        print('3. Edit last name')
        print('4. Edit password')
        print('5. Delete account')
        print('6. Return to main menu')
        return input('Choose an option: ').strip()

    
    def display_budget_form(self):
        """Display the budget creation form and get user input."""
        print("\n----- Add a New Budget -----")
        month = input("Enter month: ").strip()
        income = float(input("Enter your income: ").strip())
        
        category_percentages = {}
        category_percentages['rent'] = float(input("Enter Rent percentage: ").strip())
        category_percentages['electricity'] = float(input("Enter Electricity percentage: ").strip())
        category_percentages['savings'] = float(input("Enter Savings percentage: ").strip())
        
        return month, income, category_percentages
    
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
    
    def get_update_user_details(self, variable: str) -> str:
        return input(f'New {variable}: ')
    


        
class FeedBackHandler:
    
    def display_success_message(self, message):
        """Display a success message."""
        print(message)
    
    def display_error_message(self, message):
        """Display an error message."""
        print(message)
    
    def display_invalid_option(self):
        """Display invalid option message."""
        print("Invalid option. Please try again.")
    
    def display_exit_message(self, username=None):
        """Display exit message."""
        if username:
            print(f"Thank you for using Budget Manager. Goodbye, {username}!")
        else:
            print("Thank you for using Budget Manager. Goodbye!")
    
    def display_logout_message(self, username):
        """Display logout message."""
        print(f"Logged out successfully. Goodbye, {username}!")

    def get_confirmation(self, message):
        """Get user confirmation."""
        return input(message).strip().lower() == 'yes'
    
    