from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
	path('scoreboard/', views.scoreboard, name="scoreboard"),
	path('players/', views.playerList, name="players-list"),
	path('players/<str:pk>', views.playerDetail, name="player-detail"),		
	path('teams/', views.teamList, name="team-list"),
	path('teams/<str:pk>', views.teamDetail, name="team-detail"),
	path('teams/<str:pk>/players/best', views.bestPlayersList, name="best-players-list"),
	path('teams/<str:pk_team>/players', views.playersByTeam, name="players-by-team"),
	path('teams/<str:pk_team>/players/<str:pk_player>', views.playerDetailByTeam, name="player-detail-by-team"),
	]
