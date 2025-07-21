from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(default=000)

    def __str__(self):
        return f'{self.title} from {self.year}'