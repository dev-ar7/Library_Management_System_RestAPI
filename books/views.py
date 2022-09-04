from rest_framework.generics import (
    ListAPIView, CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Q
from .permissions import IsLibrarian, IsMember, IsLibrarianOrReadOnly
from .models import Author, Book, BorrowBook
from .serializers import (AuthorSerializer, AuthorCreateSerializer,
     BookSerializer, BookCreateSerializer, 
     BorrowBookSerializer, BorrowBookCreateSerializer,
    BorrowBookRequestSerializer, BorrowBookStatusSerializer)


class AuthorListAPIView(ListAPIView):

    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Author.objects.all()

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query) 
            )
        return queryset_list.order_by('-id')


class AuthorCreateAPIView(CreateAPIView):

    serializer_class = AuthorCreateSerializer
    permission_classes = [IsLibrarian]
    queryset = Author.objects.all()


class AuthorDetailAPIView(RetrieveAPIView):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class AuthorUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsLibrarian]


class AuthorDeleteAPIView(DestroyAPIView):

    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    permission_classes = [IsLibrarian]


class BookListAPIView(ListAPIView):

    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Book.objects.all()
        
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            )
        return queryset_list.order_by('-id')


class BookCreateAPIView(CreateAPIView):

    serializer_class = BookCreateSerializer
    permission_classes = [IsLibrarian]
    queryset = Book.objects.all()


class BookDetailAPIView(RetrieveAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsLibrarian]


class BookDeleteAPIView(DestroyAPIView):

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = [IsLibrarian]


class BorrowBooksListAPIView(ListAPIView):

    serializer_class = BorrowBookSerializer
    permission_classes = [IsLibrarian]

    def get_queryset(self, *args, **kwargs):
        queryset_list = BorrowBook.objects.all()

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            )
        return queryset_list.order_by('-id')


class BorrowBookRequestAPIView(ListAPIView):

    serializer_class = BorrowBookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        queryset_list = BorrowBook.objects.filter(user_id=self.request.user.id)

        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(name__icontains=query)
            )
        return queryset_list.order_by('-id')


class BorrowBookCreateAPIView(CreateAPIView):

    serializer_class = BorrowBookCreateSerializer
    permission_classes = [IsMember]
    queryset = BorrowBook.objects.all()

    def perform_create(self, serializer):
        return serializer.save(user_id = self.request.user.id)


class BorrowBookDetailAPIView(RetrieveAPIView):

    serializer_class = BorrowBookSerializer
    permission_classes = [IsLibrarianOrReadOnly]
    queryset  = BorrowBook.objects.all()


class BorrowBookUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = BorrowBookSerializer
    permission_classes = [IsLibrarian]
    queryset = BorrowBook.objects.all()


class BorrowBookDeleteAPIView(DestroyAPIView):

    serializer_class = BorrowBookSerializer
    permission_classes = [IsLibrarian]
    queryset = BorrowBook.objects.all()


class BorrowBookStatusUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = BorrowBookStatusSerializer
    permission_classes = [IsLibrarian]
    queryset = BorrowBook.objects.all()


class BorrowBookRequestStatusUpdateAPIView(RetrieveUpdateAPIView):

    serializer_class = BorrowBookRequestSerializer
    permission_classes = [IsLibrarian]
    queryset = BorrowBook.objects.all()