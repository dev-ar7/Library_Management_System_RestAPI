from rest_framework import serializers
from .models import *


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('id', 'name', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class AuthorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ('name',)

    def create(self, validated_data):
        Author.objects.create(**validated_data)
        return validated_data


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', validated_data.title)
        instance.author = validated_data.get('author', validated_data.author) 
        instance.save()
        return instance       


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ( 'title', 'author')

    def create(self, validated_data):
        Book.objects.create(**validated_data)
        return validated_data


class BorrowBookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowBook
        fields = ('id', 'user', 'book', 'request', 'book_status', 'created_at', 'updated_at')

    def update(self, instance, validated_data):
        instance.user = validated_data.get('user', validated_data.user)
        instance.book = validated_data.get('book', validated_data.book)
        instance.request = validated_data.get('request', validated_data.request)
        instance.book_status = validated_data.get('book_status', validated_data.book_status)
        instance.save()
        return instance


# For LIBRARIAN to change loan request status to either Accepted or Rejected
class BorrowBookRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowBook
        fields = ['request']

    def update(self, instance, validated_data):
        instance.request = validated_data.get('request', instance.request)
        instance.save()
        return instance


# For LIBRARIAN to change loan request status to either BORROWED or AVAILABLE
class BorrowBookStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowBook
        fields = ['book_status']

    def update(self, instance, validated_data):
        instance.book_status = validated_data.get('book_status', instance.book_status)
        instance.save()
        return instance


# For member to request book loan
class BorrowBookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowBook
        fields = ['user', 'book',]