from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg
from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

from .models import *
from .decorators import *

# API overview
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'View-Scoreboard':'/scoreboard/',
		'List-Teams':'/teams/',
		'Detail View-Teams':'/teams/<str:pk>/',
		'List-Players':'/teams/<str:pk>/players',
		'Detail View-Players':'/teams/<str:pk_team>/players/<str:pk_player>',
		'View-Statistics':'/users/statistics',
		}
	return Response(api_urls)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin', 'coach', 'player'])
def scoreboard(request):
	games = Game.objects.all().order_by('-date_played')
	serializer = GameSerializer(games, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin'])
def playerList(request):
	players = Player.objects.all().order_by('-id')
	serializer = PlayerSerializer(players, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin'])
def playerDetail(request, pk):
	players = Player.objects.get(id=pk)
	serializer = PlayerSerializer(players, many=False)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin'])
def teamList(request):
	teams = Team.objects.all()
	serializer = TeamSerializer(teams, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin', 'coach'])
def teamDetail(request, pk):
	try:
		team = Team.objects.get(id=pk)
	except Team.DoesNotExist:
		return Response(status=status.HTTP_404_NOT_FOUND)

	serializer = TeamSerializer(team, many=False)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin', 'coach'])
def bestPlayersList(request, pk):
	avg_query = ("SELECT 1 as id, ifnull(avg(pr.score),0) as score "
				"FROM api_player pl LEFT OUTER JOIN api_participation pr on pl.id=pr.player_id "
				"WHERE pl.team_id = %s "
				"GROUP BY pl.id ORDER BY score")
	teamsAverages = Participation.objects.raw(avg_query, [pk])
	
	#Persantile factor is calculated as 16*90/100 as 16 players are there in the team
	#persantileFactor = 14.4
	#TO DO - calculate the factor according to variable team size
	if len(list(teamsAverages)) < 14:
		return Response(None)

	persantile = float(teamsAverages[13].score) + 0.4*(float(teamsAverages[14].score)-float(teamsAverages[13].score))

	#Assuming 90th percentile is calculated (no of participated games + 1)*90/100
	players_query = ("SELECT pl.id, pl.name, pl.height, pl.team_id " 
			 "FROM api_player pl join api_participation pr on pl.id=pr.player_id " 
			 "WHERE pl.team_id = %s"
			 "GROUP BY pl.id, pl.name, pl.height, pl.team_id " 
			 "HAVING avg(pr.score) > %s")

	players = Player.objects.raw(players_query, [pk, persantile])
	serializer = PlayerSerializer(players, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin', 'coach'])
def playersByTeam(request, pk_team):
	players = Player.objects.filter(team__id=pk_team)
	serializer = PlayerSerializer(players, many=True)
	return Response(serializer.data)


@api_view(['GET'])
@allowed_users(allowed_roles=['admin', 'coach'])
def playerDetailByTeam(request, pk_team, pk_player):
	players=Player.objects.filter(pk=pk_player, team__id=pk_team)
	serializer = PlayerSerializer(players, many=True)
	return Response(serializer.data)