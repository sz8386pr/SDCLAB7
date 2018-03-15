from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=200) # User input for the place name to be added onto the wishlist. max_length is the max string length for the input field
    visited = models.BooleanField(default=False) # If user has visited place

    def __str__(self):
        return '%s visited? %s' % (self.name, self.visited)
