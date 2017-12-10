from django.db import models

class Product(models.Model):
    """
    Write your model for the exercise 3 here. Remove the pass text.
    """
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    image_url = models.URLField(blank = True)
    quantity = models.PositiveSmallIntegerField(default=0)

    def sell(self):
        self.quantity = self.quantity - 1
        self.save()
        return self.quantity
