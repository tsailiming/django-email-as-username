from django.conf import settings

user_model_label = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

def get_user_model():
    try:
        from django.contrib.auth import get_user_model
        return get_user_model()
    except ImportError:
        from django.contrib.auth.models import User
        return User
