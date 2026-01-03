from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book, Transaction

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Book)
admin.site.register(Transaction)
