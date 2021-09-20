from django.db import models

class course(models.Model):
    image = models.ImageField(upload_to = 'images/')
    descrp = models.CharField(max_length=200)

    def __str__(self):
        return self.descrp