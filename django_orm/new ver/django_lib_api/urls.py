"""
URL configuration for django_lib_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from books.views import *
from users.views import *
from rest_framework import routers

router = routers.SimpleRouter()
# router.register(r'Book',BookViewSet)
#
# router1 = routers.SimpleRouter()
# router1.register(r'Categories', CategoriesViewSet)
#
# router2 = routers.SimpleRouter()
# router2.register(r'BookOwner', BookOwnerViewSet)
#
# router3 = routers.SimpleRouter()
# router3.register(r'BookAuthor', BookAuthorViewSet)
#
# router4 = routers.SimpleRouter()
# router4.register(r'User', UserViewSet)
#
# router5 = routers.SimpleRouter()
# router5.register(r'Author', AuthorViewSet)



urlpatterns = [
    # path('api/v1/', include(router.urls)),
    # path('api/v1/', include(router1.urls)),
    # path('api/v1/', include(router2.urls)),
    # path('api/v1/', include(router3.urls)),
    # path('api/v1/', include(router4.urls)),
    # path('api/v1/', include(router5.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/Take', TakeApiView.as_view()),
    path('api/v1/TakeBack', TakeBackApiView.as_view()),
    path('api/v1/AddBook', AddBookApiView.as_view()),
    path('api/v1/CreateUser', CreateUserApiView.as_view()),

]
