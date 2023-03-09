from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.Charfield(max_length=200)
    slug = models.SlugField(max_length=200, unique=true)

    class Meta:
        ordering = ['name']
        indexes = models.Index(fields=['name']),

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


class Product(models.Model):
    category    = models.ForeignKey(Category, 
                                    relate_name='products',
                                    on_delete=models.CASCADE
                                    )
    name        = models.Charfield(max_length=200)
    slug        = models.SlugField(max_length=200)
    image       = models.ImageField(upload_to='products/%y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, 
                                   decimal_places=2)
    available   = models.BooleanField(default=True)
    created      = models.DateTimeField(auto_now_add=True)
    updated      = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

