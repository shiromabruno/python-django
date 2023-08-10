from django.db import models

class Movies(models.Model):
    title = models.CharField(max_length=64, null=False)
    episode_nb = models.IntegerField(primary_key=True)
    opening_crawl = models.TextField(null=True)
    director = models.CharField(max_length=32, null=True)
    producer = models.CharField(max_length=128, null=True)
    release_date = models.DateField(null=True)

    class Meta:
        db_table = 'ex03_movies'

    def __str__(self):
        return self.title
    

