from django.db import models

# Create your models here.
class CustomerService(models.Model):
    name = models.TextField(null=False)
    contactno = models.CharField(primary_key=True, null=False)
    emailaddress = models.TextField(null=False)
    country = models.TextField(null=False)
    remarks = models.TextField(null=False)

class MealPortionPlan(models.Model):
    id = models.UUIDField(primary_key=True,null=False)
    name = models.CharField(null=False)
    type = models.CharField(max_field=50,null=False)
    price = models.FloatField(null=False)
    dateofsale = models.DateField(null=False)
    saleno = models.UUIDField(null=False)
    contactemail = models.TextField(null=False)

class Racquets(models.Model):
    id = models.UUIDField(primary_key=True,null=False)
    name = models.CharField(null=False)
    sport = models.CharField(max_length=50,null=False)
    brand = models.CharField(max_length=50,null=False)
    model = models.CharField(null=False)
    price = models.FloatField(null=False)
    dateofsale = models.DateTimeField(null=False)
    saleno = models.UUIDField(null=False)

class SportsWear(models.Model):
    id = models.UUIDField(primary_key=True,null=False)
    name = models.TextField(null=False)
    brand = models.TextField()
    size = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    price = models.FloatField(null=False)
    dateofsale = models.DateTimeField(null=False)
    saleno = models.UUIDField(null=False)

class Supplements(models.Model):
    id = models.CharField(primary_key=True,null=False)
    name = models.CharField(null=False)
    ingredients = models.CharField(null=False)
    brand = models.CharField(null=False)
    price = models.FloatField(null=False)
    date = models.DateTimeField(null=False)
    serialno = models.UUIDField(null=False)

class Weights(models.Model):
    id = models.CharField(max_length=50,null=False)
    name = models.CharField(null=False)
    email = models.TextField(null=False)
    brand = models.TextField(null=False)
    price = models.FloatField(null=False)
    saledate = models.DateTimeField(null=False)
    salesserialno = models.UUIDField(null=False)
    
class salestracking(models.Model):
    monthlytrackingid = models.UUIDField(primary_key=True,null=False)
    name = models.CharField(null=False)
    mealplan = models.FloatField(null=False)
    racquetsales = models.FloatField(null=False)
    sportswearsales = models.FloatField(null=False)
    supplementsales = models.FloatField(null=False)
    weightsales = models.FloatField(null=False)
    remarks = models.TextField(null=False)
    dateentered= models.DateField(null=False)
    department = models.CharField(max_length=50,null=False)
    
    