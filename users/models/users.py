# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    User model.

    Extend from Django's Abstract User.
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    second_last_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)

    created_by = models.ForeignKey('self', related_name='created_by_user',
                                   on_delete=models.SET_NULL, null=True, blank=True)

    modified_by = models.ForeignKey('self', related_name='modified_by_user',
                                    on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        """Return username."""
        return self.username

    def get_short_name(self):
        """Return username."""''

        return self.username


