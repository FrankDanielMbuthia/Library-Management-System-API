from django.core.exceptions import ValidationError
from .models import Transaction

def checkout_book(user, book):
    if not book.is_available():
        raise ValidationError("This book is not available for checkout.")
    
    if Transaction.objects.filter(user=user,book=book, returned_at_isnull=True).exists():
        raise ValidationError("User has already checked out this book and not returned it yet.")
    
    transaction = Transaction.objects.create(user=user, book=book)
    book.number_of_copies -= 1
    book.save()
    return transaction
    