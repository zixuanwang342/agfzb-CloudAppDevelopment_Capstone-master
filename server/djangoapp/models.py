from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class Carmake(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name
# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    carmake=models.ForeignKey(Carmake, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    dealer_id=models.CharField(max_length=50)
    TYPE=(
        ('Sedan','Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'WAGON'),
        ('COUPE', 'COUPE'),
        ('SPORTS', 'SPORTS CAR'),
    )
    car_type=models.CharField(choices=TYPE)
    year=models.DateField()
    def __str__(self):
        return self.carmake

# <HINT> Create a plain Python class `CarDealer` to hold dealer data





# <HINT> Create a plain Python class `DealerReview` to hold review data
"""
        "id": 50,
        "name": "Sherwood Brogan",
  "dealership": 34,"
        "review": "Stand-alone holistic model",
        "purchase": false,
        "purchase_date": "05/10/2020",
        "car_make": "Cadillac",
        "car_model": "DeVille",
"""
class DealerReview:
    def __init__(self,review):
        self.review=review
