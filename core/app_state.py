class AppState:
    """Central class for managing application state."""
    
    def __init__(self):
        self.current_user = None
        self.budget_manager = None
        self.is_running = True
        self.in_account_menu = False
    
    @property
    def is_authenticated(self):
        return self.current_user is not None
    
    def reset(self):
        """Reset state on logout or account deletion"""
        self.current_user = None
        self.budget_manager = None
        self.in_account_menu = False