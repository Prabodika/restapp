from rest_framework import serializers
from .models import Team, Game, GameTeamScore, Player, User


class GameTeamScoreSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source='team.name')

    class Meta:
        model = GameTeamScore
        fields = ('score', 'team_name')


class GameSerializer(serializers.ModelSerializer):
    team_score = GameTeamScoreSerializer(read_only=True, many=True)
    winner = serializers.CharField(source='Winner.name')

    class Meta:
        model = Game
        fields = ('id', 'name', 'winner', 'team_score')


class PlayerTeamSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Player
        fields = ['id', 'name']


class TeamSerializer(serializers.ModelSerializer):
    players = PlayerTeamSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['name', 'players', 'avg']


class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='user.name')

    class Meta:
        model = Player
        fields = ['id', 'no_games', 'avg_score', 'height', 'name']


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'no_games', 'avg_score', 'height', 'name']


class TeamDetailSerializer(serializers.ModelSerializer):
    players = PlayerSerializer(read_only=True, many=True)

    class Meta:
        model = Team
        fields = ['name', 'players', 'avg']


