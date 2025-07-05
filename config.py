import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' # Requried for session security
    SESSION_COOKIE_SECURE = True # Use secure cookies in production
    REMEMBER_COOKIE_DURATION = 7200 # Remember user for 2 hours
