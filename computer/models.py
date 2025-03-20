from django.db import models

# Create your models here.
class Computer(models.Model):
    pcname = models.CharField(max_length=10, null=False)
    username = models.CharField(max_length=10)
    userid = models.CharField(max_length=10)
    name = models.CharField(max_length=40)
    job = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    note = models.CharField(max_length=40)
    class Meta:
        db_table = 'computer'