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
    
    def get_pause_message(self, menu_to_return_to):
        return input(f"\nPress any key to return to the {menu_to_return_to}...")