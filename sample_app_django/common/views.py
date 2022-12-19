from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView

from common.serializer import UserSerializer


class RegisterAPIView(APIView):

    def post(self, request):
        data = req uest.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match !')

        data['is_ambassador'] = False

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return Response(serializer.data)
