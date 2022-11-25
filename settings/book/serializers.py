from rest_framework import serializers
from .models import Book
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ('name', 'price', 'discount', 'author', 'publisher')
    