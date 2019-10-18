from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSytCWvTPQR6Q9m-wJG5Xz-nDSSs9cV7n4aVk6oR3hwDB6XbekBdA')

    def __str__(self):
        return self.item_name
