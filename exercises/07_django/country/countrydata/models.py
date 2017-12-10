from django.db import models


class Continent(models.Model):
    """ Write your answer in 7.1 here. """
    name = models.CharField(max_length = 13,unique = True, default = "")
    code = models.CharField(max_length = 2, unique=True,default="")

    class Meta:
        ordering = ["name"]

class Country(models.Model):
    """ Write your answer in 7.1 here. """
    name = models.CharField(max_length = 25,unique=True,default="")
    capital = models.CharField(max_length = 25,default="")
    code = models.CharField(max_length = 2,unique=True,default="")
    population = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    continent = models.ForeignKey(Continent, on_delete = models.CASCADE, default="",related_name='countries')
    class Meta:
        ordering = ["name"]
