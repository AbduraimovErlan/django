from django.db import models

class Book(models.Model):
    GENRE_CHOICE = (
        ('Fiction', 'Fiction'),
        ('Non-fiction', 'Non-fiction'),
        ('Business', 'Business'),
        ('Romance', 'Romance'),


    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    genre = models.CharField(choices=GENRE_CHOICE, max_length=100)
    data_filmed = models.DateField()

