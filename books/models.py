from django.db import models
from django.contrib.auth.models import User


REQUEST_CHOICES = (
        ('A', 'Accepted'),
        ('R', 'Rejected'),
)
STATUS_CHOICES = (
    ('B', 'BORROWED'),
    ('A', 'AVAILABLE'),
)


class Author(models.Model):

    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):

    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(Author, related_name='author', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author}'


class BorrowBook(models.Model):

    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='book', on_delete=models.CASCADE)
    request = models.CharField(max_length=1, choices=REQUEST_CHOICES, blank=True, null=True)
    book_status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True,)

    def __str__(self):
        return f'{self.user} - {self.book} - {self.status}'