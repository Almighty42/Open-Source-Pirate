from flask_login import UserMixin
from app import login_manager

class User(UserMixin):
    def __init__(self, id="admin"):
        self.id = id # Fixed ID

@login_manager.user_loader
def load_user(id):
    if id == "admin":
        return User(id)
    return None

@login_manager.request_loader
def request_loader(request):
    return None
