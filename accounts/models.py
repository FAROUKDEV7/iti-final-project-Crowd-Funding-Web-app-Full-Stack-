from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image_profile = models.ImageField(upload_to='profiles/%Y/%m/%d/', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True ,blank=True)
    city = models.CharField(max_length=50) 
    phone = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    

    def __str__(self):
        return str(self.user)
    
