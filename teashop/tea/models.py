from django.db import models

# Create your models here
class TeaComponent(models.Model):
    name = models.CharField(max_length=500,null=False,blank=False)
    description = models.CharField(max_length=600, null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    photo = models.ImageField()

    def __str__(self):
        return str(self.name)

    class Meta:
        app_label = 'tea'
