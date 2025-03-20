from django.db import models

# Create your models here.
class Computer(models.Model):
    pcname = models.CharField(max_length=10, null=False)
    username = models.CharField(max_length=10,null=True)
    userid = models.CharField(max_length=10,null=True)
    name = models.CharField(max_length=40,null=True)
    job = models.CharField(max_length=40,null=True)
    department = models.CharField(max_length=40,null=True)
    note = models.CharField(max_length=40,null=True)
    class Meta:
        db_table = 'computer'