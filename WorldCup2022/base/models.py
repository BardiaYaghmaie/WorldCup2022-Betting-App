from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=32)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    ties = models.IntegerField(default=0)
    goals = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    
class Match(models.Model):
    #user
    home = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home")
    away = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away")
    title = f"{home.name} vs {away.name}"
    home_goal = models.IntegerField()
    away_goal = models.IntegerField()
    
    def __str__(self):
        return str(self.title)
    