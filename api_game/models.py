from django.db import models


# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=50)
    avg = models.FloatField(default=150)

    def __str__(self):
        return self.name


class Coach(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Player(models.Model):
    height = models.FloatField(default=1.70)
    no_games = models.IntegerField(default=1)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avg_score = models.FloatField(default=90)

    def __str__(self):
        return self.user.name


class Game(models.Model):
    name = models.CharField(max_length=50)
    Winner = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class GameTeamScore(models.Model):
    team = models.ForeignKey(Team, related_name='team_scores', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='team_score', on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.game.name


class PlayerGameScore(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.game.name


class UserAudit(models.Model):
    start_time = models.DateTimeField(auto_now_add=True, blank=False)
    end_time = models.DateTimeField(auto_now_add=True, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name
