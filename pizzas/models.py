from django.db import models


class Pizza(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza)
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name