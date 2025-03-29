from controllers.budget_controller import BudgetController
from core import HandlerContext
from handlers.base_handler import BaseHandler

class BudgetHandler(BaseHandler):
    """Handles ONLY budget-related menu operations"""
    
    def __init__(self, context: HandlerContext):
        super().__init__(context)
        self.controller = BudgetController()
    
    def handle_menu(self):
        while True:
            choice = self.menu_ui.display_budget_menu(self.state.budget_manager)
            
            if choice == '5':
                break
                
            actions = {
                '1': self._add_budget,
                '2': self._display_summary,
                '3': self._view_budget_month,
                '4': self._edit_budget_month
            }
            
            action = actions.get(choice, self._handle_invalid_choice)
            action()
    
    def _add_budget(self):
        budget_data = self.menu_ui.display_budget_form(self.state.current_user.user_id)
        self.controller.create_budget(*budget_data)
        self.state.budget_manager.refresh()
    
    def _display_summary(self):
        print(self.state.budget_manager)
        self.feedback.get_pause_message('budget menu')
    
    def _view_budget_month(self):
        print(self.controller.get_budget_by_id(
            self.state.current_user.user_id, 
            input('Month: ').lower()
        ))
        self.feedback.get_pause_message('budget menu')
    
    def _edit_budget_month(self):
        month, choice, new_value = self.menu_ui.display_budget_edit_menu()
        if choice in ['1', '2', '3', '4']:
            self.controller.update_budget(
                self.state.current_user.user_id,
                month,
                choice,
                new_value
            )
        elif choice == '5':
            self.controller.delete_budget(self.state.current_user.user_id, month)
        self.state.budget_manager.refresh()