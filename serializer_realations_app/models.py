from django.db import models

# Create your models here.
class Singer(models.Model):
    gender = (
       ('male', 'male'),
       ('female', 'female'),
    )
    name = models.CharField(max_length=200)
    gender = models.CharField(choices=gender,  max_length=30,)

    def __str__(self):
        return f'{self.name}'

class Song(models.Model):
    author = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='singer_song')
    song_name = models.CharField(max_length=300)
    duration = models.FloatField(default=1.00)
    release = models.DateField()

