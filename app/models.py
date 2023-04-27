from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('borrower', 'borrower'),
        ('lender', 'lender'),
        ('admin', 'admin'),
    )
    user_type = models.CharField(max_length=200, null=True, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_admin(self):
        return self.user_type == 'admin'

    @property
    def is_borrower(self):
        return self.user_type == 'borrower'

    @property
    def is_lender(self):
        return self.user_type == 'lender'


class kyc(models.Model):
    firstName = models.CharField(max_length=100, null=True)
    lastName = models.CharField(max_length=100, null=True)
    PANnumber = models.CharField(max_length=20, null=True)
    AadharNumber = models.CharField(max_length=15, null=True)
    CreditScore = models.CharField(max_length=5, null=True)
    WalletAddress = models.CharField(max_length=200, default="", null=False)