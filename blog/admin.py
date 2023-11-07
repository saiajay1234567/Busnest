from django.contrib import admin
from .models import Bus,Book,feedback

# Register your models here.

admin.site.register(Bus)

admin.site.register(Book)
admin.site.register(feedback)
# admin.site.register(seat_book)
