from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    MANZIL = (
        ('andijon', 'Andijon'),
        ('buxoro',  'Buxoro'),
        ('farg\'ona', 'Farg\'ona'),
        ('jizzax', 'Jizzax'),
        ('xorazm', 'Xorazm'),
        ('namangan', 'Namangan'),
        ('navoiy', 'Navoiy'),
        ('qashqadaryo', 'Qashqadaryo'),
        ('qoraqalpoq', 'Qoraqalpog\'iston Respublikasi'),
        ('samarqand', 'Samarqand'),
        ('sirdaryo', 'Sirdaryo'),
        ('surxondaryo', 'Surxondaryo'),
        ('toshkent', 'Toshkent'),
    )

    address = models.CharField(max_length = 30, choices=MANZIL)
    phone = models.CharField(max_length = 13)
    image = models.ImageField(upload_to = 'user_photos/', null = True, blank = True)

    def __str__(self):
        return self.username