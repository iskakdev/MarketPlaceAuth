from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)],
                                      null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    UserRole = (
    ('client', 'client'),
    ('owner', 'owner'))
    role = models.CharField(max_length=10, choices=UserRole, default='client')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username}, {self.role}'
