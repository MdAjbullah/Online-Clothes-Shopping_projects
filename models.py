from django.db import models
class NewRegister(models.Model):
    p_id=models.AutoField(primary_key=True)
    user=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    cpassword=models.CharField(max_length=100)
    image=models.ImageField(upload_to='clothpictures/')
    def __str__(self):
        return self.email
class NewProduct(models.Model):
    p_id=models.AutoField(primary_key=True)
    category=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    productprice=models.CharField(max_length=100)
    featureofproduct=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    productid=models.CharField(max_length=100)
    image=models.ImageField(upload_to='clothpictures/')
    def __str__(self):
        return self.productid
class AddOffer(models.Model):
    p_id=models.AutoField(primary_key=True)
    Nameofoffer=models.CharField(max_length=100)
    Typeofoffer=models.CharField(max_length=100)
    Startingdate=models.CharField(max_length=100)
    Endingdate=models.CharField(max_length=100)
    message=models.CharField(max_length=100)
    def __str__(self):
        return self.Nameofoffer
class user1(models.Model):
    p_id=models.AutoField(primary_key=True)
    Productid=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    productid2=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    userid=models.CharField(max_length=100)
    image=models.ImageField(upload_to='clothpictures/')
    status=models.CharField(max_length=100)
    def __str__(self):
        return self.productname
class Rating(models.Model):
    p_id=models.AutoField(primary_key=True)
    Productid=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    image=models.CharField(max_length=100)
    comment=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)
    def __str__(self):
        return self.name
