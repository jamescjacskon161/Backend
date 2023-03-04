from django.db import models
from cloudinary.models import CloudinaryField
from category.models import Category

# Create your models here.

class Movies(models.Model):

    name=models.CharField(
        'Title' , blank= False,null=False, max_length=50 , db_index= True
    )

    description = models.TextField(
        'Descrition', blank= False, null=False, max_length=100 , default='description'
    )
    category_id=models.ForeignKey(
        Category,on_delete=models.CASCADE ,default=""
    )

    movies_duration= models.IntegerField(
        'duration',blank=False,null=False,default=45
    )
    
    poster=CloudinaryField(
        'poster',blank=True,null=True
    )
    
