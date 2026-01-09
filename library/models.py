from django.db import models
from django.contrib.auth.models import AbstractUser

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField()
    number_of_copies = models.IntegerField()
    
    def is_available(self):
        if self.number_of_copies > 0:
            return True
        return False

    def __str__(self):
        return self.title

class CustomUser(AbstractUser):
    date_of_membership = models.DateField(auto_now_add=True)
    active_status = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Transaction(models.Model):
    BORROW = 'BORROW'
    RETURN = 'RETURN'
    TRANSACTION_TYPES = [
        (BORROW, 'Borrow'),
        (RETURN, 'Return'),
    ]

    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=6, choices=TRANSACTION_TYPES)
    transaction_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_type} - {self.book.title}"
    
