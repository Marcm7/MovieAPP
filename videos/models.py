from django.db import models

GENRES = [
    ("Comedy", "Comedy"),
    ("Romance", "Romance"),
    ("Action", "Action"),
    ("Drama", "Drama"),
    ("Horror", "Horror"),
    ("Sci-Fi", "Sci-Fi"),
]

class Video(models.Model):
    MovieID = models.CharField(max_length=20, unique=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=120, blank=True)
    Actor2Name = models.CharField(max_length=120, blank=True)
    DirectorName = models.CharField(max_length=120, blank=True)
    MovieGenre = models.CharField(max_length=20, choices=GENRES)
    ReleaseYear = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"
