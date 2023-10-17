from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=200)
    No_of_guests = models.IntegerField(null=False)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return self.name


# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    # menu_item_description = models.TextField(max_length=1000, default='')

    def __str__(self):
        return self.title
