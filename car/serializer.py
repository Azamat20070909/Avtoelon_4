from rest_framework import serializers
from .models import Car, Image, Locations, Kuzov, Yoqilgi, Uzatish, Uzatma


class LocationsSer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = '__all__'


class KuzovSer(serializers.ModelSerializer):
    class Meta:
        model = Kuzov
        fields = '__all__'


class YoqilgiSer(serializers.ModelSerializer):
    class Meta:
        model = Yoqilgi
        fields = '__all__'


class UzatishSer(serializers.ModelSerializer):
    class Meta:
        model = Uzatish
        fields = '__all__'


class UzatmaSer(serializers.ModelSerializer):
    class Meta:
        model = Uzatma
        fields = '__all__'


class ImageSer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['photo']


class CarGetSer(serializers.ModelSerializer):
    manzil = LocationsSer()
    kuzov = KuzovSer()
    yoqilgi = YoqilgiSer()
    uzatish = UzatishSer()
    uzatma = UzatmaSer()
    photo = ImageSer(many = True)

    class Meta:
        model = Car
        fields = ['id', 'manzil', 'modeli', 'kuzov', 'yoqilgi', 'uzatish', 'uzatma', 'yili', 
                    'masofa', 'rangi', 'cost', 'photo', 'telefon', 'batafsil']



