from django.shortcuts import render
from rest_framework.views import APIView
from books.models import Book, Category, BookOwner, User, Author
from rest_framework.response import Response
from django_lib_api.serializers import BookOwnerSerializer, BookSerializer, UserSerializer


class TakeApiView(APIView):
    def get(self, request):
        a = Book.objects.all()
        b = User.objects.all()
        return Response({'books': BookSerializer(a, many=True).data, "users": UserSerializer(b, many=True).data})

    def post(self, request):
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        user = User.objects.get(id=user_id)
        book = Book.objects.get(id=book_id)
        BookOwner.objects.create(user_id=user, book_id=book)
        return Response("success")


class TakeBackApiView(APIView):
    def get(self, request):
        a = BookOwner.objects.all()
        return Response(BookOwnerSerializer(a, many=True).data)

    def post(self, request):
        user_id = request.data.get('user_id')
        book_id = request.data.get('book_id')
        book = BookOwner.objects.get(book_id=book_id, user_id=user_id)
        book.delete()
        return Response("success")


class AddBookApiView(APIView):
    def get(self, request):
        a = Book.objects.all()
        return Response({'books': BookSerializer(a, many=True).data})

    def post(self, request):
        author = request.data.get('author').split()
        category = request.data.get('category')
        Name = request.data.get('name')
        Author_id = Author.objects.get(name=author[0])
        Category_id = Category.objects.get(category=category)
        Book.objects.create(author_id=Author_id, name=Name, category_id=Category_id)
        return Response("success")
