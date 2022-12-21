from django.shortcuts import render

# Create your views here.
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import User
from common.serializer import UserSerializer
from .authentication import JWTAuthentication


class RegisterAPIView(APIView):

    def post(self, request):
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException('Password do not match !')

        data['is_ambassador'] = False

        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()
        return Response(serializer.data)
class LoginAPIView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Incorrect password')
        jwtAuthentications=JWTAuthentication()
        token = jwtAuthentications.generate_jwt(user.id)
        response = Response()
        response.set_cookie(key='jwt',value=token,httponly=True)

        response.data={
            'messages': 'success'
        }
        return response
        #     Response({
        #     'jwt': token
        # })

        # return Response(UserSerializer(user).data)

