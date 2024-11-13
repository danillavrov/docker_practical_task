from django.contrib import admin

from django_lib_api.models import *



@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author_id', 'category_id')

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('author_id', 'book_id')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)

@admin.register(BookOwner)
class BookOwnerAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'user_id')

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')