from django.db import models

class Image(models.Model):
    # Add necessary fields for the image model
    # For example:
    name=models.CharField(max_length=100)
    IN = models.DecimalField(max_digits=8, decimal_places=2)
    OUT= models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='pics')
    sat=models.IntegerField()

    def __str__(self):
        return self.name

