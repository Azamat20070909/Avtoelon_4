from django.db import models
from user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Locations(models.Model):

    VILOYAT = (
		('andijon', 'Andijon'),
		('buxoro', 'Buxoro'),
		("farg'ona", "Farg'ona"),
		('jizzax', 'Jizzax'),
		('xorazm', 'Xorazm'),
		('namangan', 'Nmanagan'),
		('navoiy', 'Navoiy'),
		('qashqadaryo', 'Qashqadaryo'),
		("qoraqalpog'iston respublikasi", "Qoraqalpog'iston Respublikasi"),
		('samarqand', 'Samarqand'),
		('sirdaryo', 'Sirdaryo'),
		('surxondaryo', 'Surxondaryo'),
		('toshkent', 'Toshkent')
		)

    locations = models.CharField(max_length = 50, choices = VILOYAT, default = 'andijon')

    def __str__(self):
        return f'{self.locations}'
 

class Car_Model(models.Model):
    model = models.CharField(max_length = 20, verbose_name = 'modeli')
    marka = models.CharField(max_length = 30, verbose_name = 'markasi')


class Image(models.Model):
    image = models.ImageField(upload_to = 'car_photos')


class Kuzov(models.Model):
    KUZOV = (
        ('sedan', 'Sedan'),
        ('hatchback', 'Hatchbak'),
        ('offroad', 'Offroad'),
        ('universal', 'Universal'),
        ('kabriolet', 'Kabriolet'),
        ('krossover', 'Krossover'),
        ('kupe', 'Kupe'),
        ('limuzin', 'Limuzin'),
        ('mikroavtobus', 'Mikroavtobus'),
        ('miniven', 'Miniven'),
        ('pikup', 'Pikup'),
        ('rodster', 'Rodster'),
        ('furgon', 'Furgon'),
    )
    kuzov = models.CharField(max_length=15, choices = KUZOV)

    def __str__(self):
        return f'{self.kuzov}'


class Yoqilgi(models.Model):
    TURI = (
        ('benzin','Benzin'),
        ('gaz-benzin','Gaz-Benzin'),
        ('dizel','Dizel'),
        ('elektr','Elektr'),
        ('gibrid','Gibrid'),
        ('gaz','Gaz'),
    )
    yoqilgi = models.CharField(max_length = 11, choices = TURI)

    def __str__(self):
        return f'{self.yoqilgi}'


class Uzatish(models.Model):
    QUTISI = (
        ('mexanika','Mexanika'),
        ('avtomat','Avtomat'),
        ('tiptronik','Tiptronik'),
        ('variator','Variator'),
        ('robot', 'Robot'),
    )
    uzatish = models.CharField(max_length = 10, choices = QUTISI)

    def __str__(self):
        return f'{self.uzatish}'


class Uzatma(models.Model):
    UZATMA = (
        ('oldi','Oldi'),
        ('orqa','Orqa'),
        ('to\'liq','To\'liq'),
    )
    qutisi = models.CharField(max_length = 7, choices = UZATMA)

    def __str__(self):
        return f'{self.qutisi}'

class Car(models.Model):

    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'User_cars')
    manzil = models.ForeignKey(Locations, on_delete = models.CASCADE, related_name = 'Car_location')
    photo = models.ManyToManyField(Image, related_name = 'Car_photo')
    modeli = models.ForeignKey(Car_Model, on_delete = models.CASCADE, related_name ='Car_model')
    kuzov = models.ForeignKey(Kuzov, on_delete = models.CASCADE, related_name = 'Car_kuzov', blank = True, null = True)
    yoqilgi = models.ForeignKey(Yoqilgi, on_delete = models.CASCADE, related_name = 'Car_yoqilgisi')
    uzatish = models.ForeignKey(Uzatish, on_delete = models.CASCADE, related_name = 'Car_qutisi')
    batafsil = models.TextField(blank = True, null = True)
    telefon = models.CharField(max_length = 13, verbose_name = 'aloqa uchun telefon')
    yili = models.IntegerField(validators=[MinValueValidator(1990), MaxValueValidator(2024)])
    masofa = models.IntegerField(validators=[MinValueValidator(0)], blank = True, null = True)
    rangi = models.CharField(max_length = 20, verbose_name = 'rangi', blank = True, null = True)
    uzatma = models.ForeignKey(Uzatma, on_delete = models.CASCADE, related_name = 'Car_qutisi')
    cost = models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return f'{self.modeli}'
