from django.contrib.auth.models import Permission, User
from django.db import models
from django.utils import timezone

COLOR_CHOICES = (
    ('chicken','CHICKEN'),
    ('egg', 'EGG'),
    ('butter','BUTTER'),
    ('juice','JUICE'),
)



class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    name = models.CharField(max_length=250)
    rollno = models.CharField(max_length=500)
    dues = models.IntegerField(default=0)
    def __str__(self):
        return self.name


class Song(models.Model):
    student = models.ForeignKey(Album, on_delete=models.CASCADE)
    extra = models.CharField(max_length=7, choices=COLOR_CHOICES, default='chicken')
    quantity = models.IntegerField(default=0);
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.extra
