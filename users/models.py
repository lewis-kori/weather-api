from django.db import models

from django.contrib.auth.models import AbstractUser, UserManager

class UserAccountManager(UserManager):
    pass

class UserAccount(AbstractUser):
    """
    It's always advisable to use a custom 
    user model whenever starting new django projects.
    This makes it easier to extend the user fields in future.
    access this model using:

    ```
    from django.contrib.auth import get_user_model
    User = get_user_model()
    ```
    """
    objects = UserAccountManager()
