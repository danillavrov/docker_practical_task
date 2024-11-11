from rest_framework.views import APIView
from django_lib_api.models import Book, Category, BookOwner, BookAuthor, User, Author
from rest_framework import generics, viewsets
from rest_framework.response import Response
from django_lib_api.serializers import CategoriesSerializer, AuthorSerializer, BookAuthorSerializer, BookOwnerSerializer, BookSerializer, UserSerializer


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

class libapiview(APIView):
    def get(self, request):
        a = Book.objects.all()
        return Response({'books': BookSerializer(a, many=True).data})

    def post(self, request):
        a = Book.objects.all()

        book = request.data.get('book_id')
        act = request.data.get('act')
        user = request.data.get('user_id')

        if act == 'take':
            user = User.objects.get(id=user)
            book = Book.objects.get(id=book)
            BookOwner.objects.create(user_id=user, book_id=book)

        if act == 'back':
            book = BookOwner.objects.get(id=book)
            book.delete()

        if act == 'loses':
            book1 = BookOwner.objects.get(id=book)
            book1.delete()
            book = Book.objects.get(id=book)
            book.delete()
        return Response({'books': BookSerializer(a, many=True).data})

















