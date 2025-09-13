from django.db import models
from django.utils.text import slugify
# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/%Y/%m/%d/')
    funded_amount = models.DecimalField(max_digits=10, decimal_places=2)
    donatuion_amount = models.DecimalField(max_digits=10, decimal_places=2)
    donors = models.IntegerField()
    days_left = models.IntegerField()
    about_project = models.TextField()
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, related_name='projects')
    slug = models.SlugField(null=True, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'