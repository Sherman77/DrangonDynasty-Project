from django.db import models

# Create your models here.
class Rice(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class MainDish(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SideDish(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Meal(models.Model):
    mainDish = models.ForeignKey(MainDish, on_delete=models.CASCADE)
    sideDish = models.ForeignKey(SideDish, on_delete=models.CASCADE)
    rice = models.ForeignKey(Rice, on_delete=models.CASCADE)
