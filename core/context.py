from core import AppState
from views.menu_ui import MenuUI
from views.feedback_handler import FeedBackHandler

class HandlerContext:

    def __init__(self):
        self.state = AppState()
        self.menu_ui = MenuUI()
        self.feedback = FeedBackHandler()