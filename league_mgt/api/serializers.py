from rest_framework import serializers
from django.db.models import Avg
from .models import *

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = Task
		fields ='__all__'

class PlayerSerializer(serializers.ModelSerializer):
	team = serializers.StringRelatedField(many=False)
	no_of_games = serializers.SerializerMethodField('count_participation')
	average_score = serializers.SerializerMethodField('calculate_average_score')

	def count_participation(self, _player):
		player = Player.objects.get(id=_player.id)
		participation = player.participation_set.all().count()
		return participation

	def calculate_average_score(self, _player):
		player = Player.objects.get(id=_player.id)
		average_score = player.participation_set.all().aggregate(Avg('score'))
		return average_score['score__avg']

	class Meta:
		model = Player
		fields = ['name', 'height', 'team', 'no_of_games', 'average_score' ]


class ScorecardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Scorecard
		fields = ['side', 'team', 'score']


class GameSerializer(serializers.ModelSerializer):
	scorecards = serializers.SerializerMethodField('get_scorecards')

	def get_scorecards(self, obj):
		_scorecards = Scorecard.objects.filter(game_id=obj.id).distinct()
		return ScorecardSerializer(_scorecards, many=True).data

	class Meta:
		model = Game
		fields = ['name', 'date_played', 'match_round', 'result', 'scorecards']

class TeamSerializer(serializers.ModelSerializer):
	class Meta:
		model = Team
		fields = '__all__'