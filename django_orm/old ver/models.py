from django.db import models


# class ProductCategory(models.Model):
#     name = models.CharField(max_length=128)
#     description = models.TextField(null=True, blank=True)
#
#     def __str__(self):
#         return self.name

class Category(models.Model):
    category = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


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
