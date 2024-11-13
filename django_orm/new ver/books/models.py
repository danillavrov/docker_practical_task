from django.db import models

from users.models import User


class Category(models.Model):
    category = models.CharField(max_length=50)


class Author(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)


class Book(models.Model):
    name = models.CharField(max_length=50)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookAuthor(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookOwner(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
