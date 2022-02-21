from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length =  100)
    age = models.IntegerField(
        default=18,
        validators=[MaxValueValidator(100), MinValueValidator(1)]
    )
    email = models.EmailField()
    SCHOOL_CHOICES = [
        ('UST','The Hong Kong University of Science and Technology'),
        ('CU', 'The Chinese University of Hong Kong'),
        ('HKU','The University of Hong Kong')
    ]
    school = models.CharField(
        max_length=3,
        choices=SCHOOL_CHOICES,
        default='UST'
    )
    slug = models.SlugField(unique= True)
    image = models.ImageField(upload_to='images')

    objects = models.Manager()

    def __str__ (self):
        return self.name + " " + self.school
