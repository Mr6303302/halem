from asyncio.windows_events import NULL
from distutils.command.upload import upload
from email.mime import image
from django.db import models

class project(models.Model):
    id=models.IntegerField(primary_key=True )
    name=models.CharField(max_length=150 )
    image=models.ImageField(upload_to='photos/%y/%m/%d' )

    def __str__(self):
        return self.name

class main_project(models.Model):
    project=models.ForeignKey(project ,on_delete=models.CASCADE)
    cotente=models.TextField(max_length=1500,default=NULL)
    fimage=models.ImageField(upload_to='photos/%y/%m/%d')
    
    def __str__(self):
        return str(self.project)

class project_image(models.Model):
    id_n=models.IntegerField(default=NULL )
    project=models.ForeignKey(project ,on_delete=models.CASCADE)
    project_image=models.ImageField(upload_to='photos/%y/%m/%d')

    def __str__(self):
        return str(self.project)


