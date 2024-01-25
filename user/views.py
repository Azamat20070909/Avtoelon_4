from django.shortcuts import render
from .models import *
# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


# class UserApi(generics.ListCreateAPIView):
# 	queryset = User.objects.all()
# 	serializer_class = UserSerializer


class UserApiList(APIView):

	def get(self, request):
		a = User.objects.all()
		dict_data = UserSerializer(a, many = True)
		return Response(dict_data.data)

