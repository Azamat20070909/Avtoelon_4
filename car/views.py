from django.shortcuts import render
from .models import Car,Image
from .serializer import CarSerializer, CarGetSer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import generics

# Create your views here.

class CarApi(APIView):

	def get(self, request):
		a = Car.objects.all()
		dict_data = CarSerializer(a, many = True)
		return Response(dict_data.data)

	def post(self, request):
		rasm_list = request.data.get('image', [])
		serializer = CarSerializer(data = request.data)

		if serializer.is_valid():
			Car = serializer.save()
			for x in rasm_list:
				t = Image.objects.create(image = x)
				Car.image.add(t)
			return Response(serializer.data)
		return Response(serializer.errors)


class CarApiList(APIView):
	def get(self, request, id):
		try:
			a = Car.objects.get(id = id)
			s = CarGetSer(a)
			return Response(s.data)

		except Exception as a:
			return Response({'xabar':f"{a}"})