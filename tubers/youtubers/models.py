from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):
    #choice restricting
    
    crew_choices=(
        ('solo','solo'),
        ('small','small'),
        ('large','large'),
    )

    camera_choices=(
        ('canon','canon'),
        ('fuji','fuji'),
        ('nikon','nikon'),
        ('sony','sony'),
    )

    category_choices=(
        ('education','education'),
        ('comedy','comedy'),
        ('gaming','gaming'),
        ('cooking','cooking'),
    )
    

    #main fields
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    photo=models.ImageField(upload_to='media/ytubers/%Y/%m/')
    video_url=models.CharField(max_length=255)
    description=RichTextField()
    city=models.CharField(max_length=255)
    age=models.IntegerField()
    crew=models.CharField(choices=crew_choices ,max_length=255,null=True)
    camera=models.CharField(choices=camera_choices ,max_length=255,null=True)
    category=models.CharField(choices=category_choices ,max_length=255,null=True)
    subs_count=models.IntegerField()
    is_featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(default=datetime.now,blank=True)

    def __str__(self):
        return self.name

    