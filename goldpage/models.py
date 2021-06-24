from django.db import models

# Create your models here.
class Products(models.Model):
    proid=models.IntegerField()
    pronm=models.CharField(max_length=50)
    propri=models.IntegerField()
    proamt=models.IntegerField()
    proi=models.ImageField(upload_to='uploads/')
    profil=models.IntegerField(default=1)
    
class User(models.Model):
    usrmail=models.EmailField(max_length=60,default="guest@domain.com")
    usrpass=models.CharField(max_length=50,default="12345678")
    usrprofile=models.ImageField(upload_to='usrprofile/',null=True,blank=True)
    usrphoto=models.ImageField(upload_to='usrphotos/',null=True,blank=True)

