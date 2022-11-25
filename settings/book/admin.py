from django.contrib import admin
from .models import Author, Publisher, Book, Subject

admin.site.register(Author)
admin.site.register(Subject)
admin.site.register(Book)
admin.site.register(Publisher)