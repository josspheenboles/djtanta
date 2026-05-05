from django.db import models

# Create your models here.
class Catagory(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name='ID',help_text='catagory id')
    name=models.CharField(max_length=100,help_text='catagory name',verbose_name='Catagory  Name')
    # test=models.TextField()
    def __str__(self):
        return self.name



