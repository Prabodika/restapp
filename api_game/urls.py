from django.conf.urls import url
from .views import game_list, player_avg
from .views import player_details
from .views import coach_team_list
from .views import teams_detail
from .views import team_data

urlpatterns = [

    url(r'^game-api/v1/games', game_list),
    url(r'^game-api/players/(?P<pk>[0-9]+)', player_details),
    url(r'^game-api/v1/coaches/(?P<pk>[0-9]+)/teams/players$', player_avg),
    # this route is  only available for coaches to get his team details
    url(r'^game-api/v1/coaches/(?P<pk>[0-9]+)/teams', coach_team_list),
    # this route is for admin to get team detail
    url(r'^game-api/v1/teams/(?P<pk>[0-9]+)', team_data),
    url(r'^game-api/v1/teams', teams_detail),

]
