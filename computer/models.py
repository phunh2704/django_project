from django.db import models


class Computer_TXTS(models.Model):
    pcname = models.CharField(max_length=10, null=False)
    username = models.CharField(max_length=10,null=True)
    userid = models.CharField(max_length=10,null=True)
    name = models.CharField(max_length=40,null=True)
    cd = models.CharField(max_length=20,null=True)
    job = models.CharField(max_length=40,null=True)
    department = models.CharField(max_length=40,null=True)
    phone = models.CharField(max_length=12,null=True)        
    buy = models.IntegerField(null=True)
    mainboard = models.CharField(max_length=20,null=True)
    cpu = models.CharField(max_length=20,null=True)
    ram = models.CharField(max_length=20,null=True)
    disk = models.CharField(max_length=20,null=True)
    vga = models.CharField(max_length=20,null=True)
    monitor = models.CharField(max_length=20,null=True)
    note = models.CharField(max_length=40,null=True)
    class Meta:
        db_table = 'computer_txts'