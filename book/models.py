from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100,db_index=True)#index--->fast search
    description=models.TextField(null=True)
    price=models.DecimalField(decimal_places=2,max_digits=10)
    create_date=models.DateField(auto_now_add=True,verbose_name='Insert Date')#during insert get date
    update_date=models.DateTimeField(auto_now=True,verbose_name='Update Date')
    image=models.ImageField(upload_to='books_cover',blank=True,null=True)





