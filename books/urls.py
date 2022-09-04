from django.urls import path
from .views import *


urlpatterns = [
    path('authors/', AuthorListAPIView.as_view(), name='authors'),
    path('author/create', AuthorCreateAPIView.as_view(), name='author_create'),
    path('author/detail/<int:pk>/', AuthorDetailAPIView.as_view(), name='author_detail'),
    path('author/update/<int:pk>/', AuthorUpdateAPIView.as_view(), name='author_update'),
    path('author/delete/<int:pk>/', AuthorDeleteAPIView.as_view(), name='author_delete'),
    path('books/', BookListAPIView.as_view(), name='books'),
    path('book/create', BookCreateAPIView.as_view(), name='book_create'),
    path('book/detail/<int:pk>/', BookDetailAPIView.as_view(), name='book_detail'),
    path('book/update/<int:pk>/', AuthorListAPIView.as_view(), name='book_update'),
    path('book/delete/<int:pk>/', BookDeleteAPIView.as_view(), name='book_delete'),
    path('borrow_books/', BorrowBooksListAPIView.as_view(), name='borrow_books'),
    path('borrow_book/create', BorrowBookCreateAPIView.as_view(), name='borrow_book_create'),
    path('borrow_book/detail/<int:pk>/', BorrowBookDetailAPIView.as_view(), name='borrow_book_detail'),
    path('borrow_book/update/<int:pk>/', BorrowBookUpdateAPIView.as_view(), name='borrow_book_update'),
    path('borrow_book/delete/<int:pk>/', BorrowBookDeleteAPIView.as_view(), name='borrow_book_delete'),
    path('borrow_book/request', BorrowBookRequestAPIView.as_view(), name='borrow_book_request'),
    path('borrow_book/request_status/update/<int:pk>/', BorrowBookRequestStatusUpdateAPIView.as_view(), name='borrow_book_request_status_update'),
    path('borrow_book/status/update/<int:pk>/', BorrowBookStatusUpdateAPIView.as_view(), name='borrow_book_status_update'),
]