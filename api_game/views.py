from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from .models import Team, Game, Coach, Player
from .serializers import TeamSerializer, GameSerializer, PlayerSerializer, TeamDetailSerializer


# Create your views here.
@api_view(["GET"])
def game_list(request):
    """
    List all Games
    """
    if request.method == 'GET':
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def player_details(request, pk):
    """
       Retrieve, certain player detail.
    """
    try:
        player = Player.objects.get(pk=pk)
    except player.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PlayerSerializer(player)
        return JsonResponse(serializer.data)


@api_view(["GET"])
def coach_team_list(request, pk):
    """
       Retrieve, certain coach team detail.
    """
    try:
        coach = Coach.objects.get(pk=pk)

    except coach.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TeamSerializer(coach.team)
        return JsonResponse(serializer.data)


@api_view(["GET"])
def player_avg(request, pk):
    """
       Retrieve, certain player detail over 90%.
    """
    try:
        coach = Coach.objects.get(pk=pk)

    except coach.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':

        coach = Coach.objects.get(pk=pk)
        players = Player.objects.all()
        players_detail = players.filter(team=coach.team)
        avg_score = request.query_params.get('avg_score', None)

        if avg_score is not None:
            player = players_detail.filter(avg_score__gte=avg_score)
            serializer = PlayerSerializer(player, many=True)
            return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def teams_detail(request):
    """
       Retrieve, certain player detail over 90%.
    """
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamDetailSerializer(teams, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET"])
def team_data(request, pk):
    """
       Retrieve, certain player detail.
    """

    try:
        team = Team.objects.get(pk=1)

    except team.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = TeamSerializer(team)
        return JsonResponse(serializer.data)
