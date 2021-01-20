from django.contrib import admin
from .models import Role
from .models import User
from .models import Team
from .models import Coach
from .models import Player
from .models import Game
from .models import GameTeamScore
from .models import PlayerGameScore
from .models import UserAudit

# Register your models here.
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Team)
admin.site.register(Coach)
admin.site.register(Player)
admin.site.register(Game)
admin.site.register(GameTeamScore)
admin.site.register(PlayerGameScore)
admin.site.register(UserAudit)
