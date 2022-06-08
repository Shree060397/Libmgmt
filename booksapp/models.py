from django.db import models

# Create your models here.
class Books(models.Model):
  id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=70)


  
class Roles(models.Model):
  id=models.AutoField(primary_key=True)
  role=models.CharField(max_length=10)


class Users(models.Model):
  id=models.AutoField(primary_key=True)
  Email=models.CharField(max_length=50)
  password=models.CharField(max_length=12)
  roles = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='role_id')






