from django.db import models

# Create your models here.

class Conference(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.EmailField()

class Session(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    speakers = models.ManyToManyField(Speaker)


class Attendee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.TextField()
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Attendee, on_delete=models.CASCADE)
