from books.models import Book, Category, BookOwner, BookAuthor, User, Author
from rest_framework import viewsets
from django_lib_api.serializers import CategoriesSerializer, AuthorSerializer, BookAuthorSerializer, \
    BookOwnerSerializer, BookSerializer, UserSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookAuthorViewSet(viewsets.ModelViewSet):
    queryset = BookAuthor.objects.all()
    serializer_class = BookAuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookOwnerViewSet(viewsets.ModelViewSet):
    queryset = BookOwner.objects.all()
    serializer_class = BookOwnerSerializer
