from django.db import models

class Customer(models.Model):
    city_choice = [
    ('islamabad', 'Islamabad'),
    ('lahore', 'Lahore'),
    ('karachi', 'Karachi'),
    ('peshawar', 'Peshawar'),
    ('quetta', 'Quetta'),
    ('multan', 'Multan'),
    ('sargodha', 'Sargodha'),
    ('hyderabad', 'Hyderabad'),
    ('rawalpindi', 'Rawalpindi'),
    ('sialkot', 'Sialkot'),
    ('mardan', 'Mardan'),
]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=20, choices=city_choice, default='lahore')
    

    def __str__(self):
        return self.name