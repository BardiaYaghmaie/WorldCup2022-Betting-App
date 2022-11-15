from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=32)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    
class Match(models.Model):
    home = models.ForeignKey(Team, on_delete=models.CASCADE)