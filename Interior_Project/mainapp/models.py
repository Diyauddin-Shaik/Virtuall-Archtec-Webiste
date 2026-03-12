from django.db import models
from django.contrib.auth.models import User


class RoomDesign(models.Model):

    ROOM_CHOICES = [
        ('Living Room','Living Room'),
        ('Kitchen','Kitchen'),
        ('Bedroom','Bedroom'),
        ('Bathroom','Bathroom'),
        ('Dining Room','Dining Room'),
        ('Study Room','Study Room'),
        ('Kids Room','Kids Room'),
        ('Balcony','Balcony'),
        ('Pooja Room','Pooja Room'),
        ('Guest Room','Guest Room'),
    ]

    HOUSE_CHOICES = [
        ('1RK','1RK'),
        ('1BHK','1BHK'),
        ('2BHK','2BHK'),
        ('3BHK','3BHK'),
        ('4BHK','4BHK'),
        ('5BHK','5BHK'),
    ]

    # user who created design
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # only required for bedroom
    house_type = models.CharField(
        max_length=10,
        choices=HOUSE_CHOICES,
        null=True,
        blank=True
    )

    # which room design
    room_type = models.CharField(
        max_length=50,
        choices=ROOM_CHOICES
    )

    # design details (optional because not every room needs them)
    wall_color = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    lamp_type = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    furniture = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    # uploaded image
    image = models.ImageField(
        upload_to='uploads/',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.room_type}"


class ChatMessage(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.message[:30]}"