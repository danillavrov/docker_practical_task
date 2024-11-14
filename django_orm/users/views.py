from rest_framework.views import APIView
from users.models import User
from rest_framework.response import Response
from django_lib_api.serializers import UserSerializer


class CreateUserApiView(APIView):
    def get(self, request):
        a = User.objects.all()
        return Response(UserSerializer(a, many=True).data)

    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        User.objects.create(name=name, email=email)
        return Response("success")
