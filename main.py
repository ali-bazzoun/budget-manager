from user import User
from database import save_user, login_user, delete_user, save_budget_data, get_budget_data
from budget_manager import BudgetManager
from monthly_budget import MonthlyBudget
from print_table import print_table



def main():
    current_user = None
    is_running = True
     
    while is_running:
        if current_user is None:
            # Not logged in - show authentication menu
            display_auth_menu()
            auth_choice = input('Choose an option: ').strip()
            
            if auth_choice == '1':  # Register
                current_user = handle_registration()
                
            elif auth_choice == '2':  # Login
                current_user = handle_login()
                
            elif auth_choice == '3':  # Exit
                print("Thank you for using Budget Manager. Goodbye!")
                is_running = False
                
            else:
                print("Invalid option. Please try again.")
        
        else:
            # User is logged in - show main menu
            display_main_menu(current_user.username)
            main_choice = input('Choose an option: ').strip()
            
            if main_choice == '1':  # Add budget
                add_budget(current_user)
            
            if main_choice == '2':  # View budgets
                view_budgets(current_user)
                
            elif main_choice == '3':  # User account menu
                current_user = handle_user_account_menu(current_user)
                
            elif main_choice == '4':  # Logout
                print(f"Logged out successfully. Goodbye, {current_user.username}!")
                current_user = None
                
            elif main_choice == '5':  # Exit
                print(f"Thank you for using Budget Manager. Goodbye, {current_user.username}!")
                is_running = False
                
            else:
                print("Invalid option. Please try again.")


def display_auth_menu():
    """Display the authentication menu options."""
    print('\n===== Budget Manager =====')
    print('1. Register')
    print('2. Login')
    print('3. Exit')


def display_main_menu(username):
    """Display the main menu options for logged-in users."""
    print(f'\n===== Budget Manager - Welcome, {username} =====')
    print('1. Add Budget')
    print('2. View Budgets')
    print('3. User account settings')
    print('4. Logout')
    print('5. Exit')


def display_user_account_menu():
    """Display the user account management menu options."""
    print('\n===== User Account Settings =====')
    print('1. Edit username')
    print('2. Edit first name')
    print('3. Edit last name')
    print('4. Edit password')
    print('5. Delete account')
    print('6. Return to main menu')


def handle_registration():
    """Handle the user registration process."""
    print("\n----- User Registration -----")
    username = input('Username: ').strip()
    password = input('Password: ').strip()
    firstname = input('First name: ').strip()
    lastname = input('Last name: ').strip()
    
    new_user = User(
        username=username, 
        password=password, 
        firstname=firstname,
        lastname=lastname
    )
    
    if save_user(new_user):
        print(f"Registration successful! Welcome, {firstname}!")
        return new_user
    else:
        print("Registration failed. Please try again.")
        return None


def handle_login():
    """Handle the user login process."""
    print("\n----- User Login -----")
    username = input('Username: ').strip()
    password = input('Password: ').strip()
    
    user = login_user(username, password)
    
    if user:
        greeting_name = user.firstname or user.username
        print(f"Login successful! Welcome back, {greeting_name}!")
        return user
    else:
        print("Login failed. Invalid username or password.")
        return None


def handle_user_account_menu(user):
    """Handle the user account management menu."""
    current_user = user
    return_to_main = False
    
    while not return_to_main:
        display_user_account_menu()
        account_choice = input('Choose an option: ').strip()
        
        if account_choice == '1':  # Edit username
            new_username = input('New username: ').strip()
            if new_username and new_username != user.username:
                updated_user = User(
                    user_id=user.user_id,
                    username=new_username,
                    password=user.password,
                    firstname=user.firstname,
                    lastname=user.lastname
                )
                if save_user(updated_user, user.user_id):
                    print("Username updated successfully!")
                    current_user = updated_user
                else:
                    print("Failed to update username. It might already be taken.")
            else:
                print("Invalid or unchanged username. Operation cancelled.")
                
        elif account_choice == '2':  # Edit first name
            new_firstname = input('New first name: ').strip()
            if new_firstname and new_firstname != user.firstname:
                updated_user = User(
                    user_id=user.user_id,
                    username=user.username,
                    password=user.password,
                    firstname=new_firstname,
                    lastname=user.lastname
                )
                if save_user(updated_user, user.user_id):
                    print("First name updated successfully!")
                    current_user = updated_user
                else:
                    print("Failed to update first name.")
            else:
                print("Invalid or unchanged first name. Operation cancelled.")
                
        elif account_choice == '3':  # Edit last name
            new_lastname = input('New last name: ').strip()
            if new_lastname and new_lastname != user.lastname:
                updated_user = User(
                    user_id=user.user_id,
                    username=user.username,
                    password=user.password,
                    firstname=user.firstname,
                    lastname=new_lastname
                )
                if save_user(updated_user,):
                    print("Last name updated successfully!")
                    current_user = updated_user
                else:
                    print("Failed to update last name.")
            else:
                print("Invalid or unchanged last name. Operation cancelled.")
                
        elif account_choice == '4':  # Edit password
            new_password = input('New password: ').strip()
            if new_password:
                updated_user = User(
                    user_id=user.user_id,
                    username=user.username,
                    password=new_password,
                    firstname=user.firstname,
                    lastname=user.lastname
                )
                if save_user(updated_user, user.user_id):
                    print("Password updated successfully!")
                    current_user = updated_user
                else:
                    print("Failed to update password.")
            else:
                print("Invalid password. Operation cancelled.")
                
        elif account_choice == '5':  # Delete account
            confirm = input("Are you sure you want to delete your account? (yes/no): ").strip().lower()
            if confirm == 'yes':
                if delete_user(user.user_id):
                    print("Account deleted successfully.")
                    return None  # Return None to indicate user is logged out
                else:
                    print("Failed to delete account.")
            else:
                print("Account deletion cancelled.")
                
        elif account_choice == '6':  # Return to main menu
            return_to_main = True
            
        else:
            print("Invalid option. Please try again.")
    
    return current_user


def add_budget(user):
    """Prompt the user to add a new budget."""
    print("\n----- Add a New Budget -----")
    month = input("Enter month: ").strip()
    income = float(input("Enter your income: ").strip())
    
    # Here you would collect other budget-related info (e.g., category allocations)
    category_percentages = {}
    category_percentages['rent'] = float(input("Enter Rent percentage: ").strip())
    category_percentages['electricity'] = float(input("Enter Electricity percentage: ").strip())
    category_percentages['savings'] = float(input("Enter Savings percentage: ").strip())

    # Add the budget to the user's data (you can expand this to save to a database)
    new_budget = MonthlyBudget(user_id=user.user_id, month=month, income=income, category_percentages=category_percentages)
    
    if save_budget_data(new_budget):
        print("Budget added successfully!")
    else:
        print("Failed to add budget. Please try again.")


def view_budgets(user):
    """Display all budgets for the user."""
    print("\n----- View Your Budgets -----\n")
    budgets = get_budget_data(user.user_id)
    
    if not budgets:
        print("No budgets found.")
    else:
        budget_manager = BudgetManager(user)
        data = budget_manager.get_data()
        keys = ['month', 'income', 'savings', 'electricity', 'rent', 'unallocated']
        data.insert(0, keys)
        print_table(data)
        print('\n')
        print(budget_manager)

if __name__ == "__main__":
    main()