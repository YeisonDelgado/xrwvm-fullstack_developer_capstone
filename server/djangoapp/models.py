from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Relación muchos a uno
    name = models.CharField(max_length=100)
    
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Puedes agregar más si deseas
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')
    
    year = models.IntegerField(
        default=datetime.datetime.now().year,
        validators=[
            MinValueValidator(2015),
            MaxValueValidator(datetime.datetime.now().year)
        ]
    )
    
    dealer_id = models.IntegerField()  # ID del concesionario (desde Cloudant u otra fuente)

    def __str__(self):
        return f"{self.car_make.name} {self.name}"
