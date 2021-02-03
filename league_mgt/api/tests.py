from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User, Permission, Group
from .models import *
import json

# Create your tests here.

class PlayerTests(APITestCase):
	def setUp(self):
		self.user_admin = User.objects.create_user(username="test_admin", email="testadmin@test.com", password="test")
		self.user_coach = User.objects.create_user(username="test_coach", email="testcoach@test.com", password="test")
		self.user_player = User.objects.create_user(username="test_player", email="testplayer@test.com", password="test")
		self.user_without_roles_assigned = User.objects.create_user(username="test_user", email="testplayer1@test.com", password="test")
		
		self.group_admin = Group.objects.create(name="admin")
		self.group_coach = Group.objects.create(name="coach")
		self.group_player = Group.objects.create(name="player")
		
		self.user_admin.groups.add(self.group_admin)
		self.user_admin.save()

		self.user_coach.groups.add(self.group_coach)
		self.user_coach.save()

		self.user_player.groups.add(self.group_player)
		self.user_player.save()

		self.team_ptb = Team.objects.create(name='Portland Trail Blazers')
		self.team_cb = Team.objects.create(name='Chicargo Bulls')

		self.plr_crmelo = Player.objects.create(name='Carmelo Anthony', height='170 cm', team=self.team_ptb)
		self.plr_damian = Player.objects.create(name='Damian Lillard', height='173 cm', team=self.team_cb)

		self.coach_temothy = Coach.objects.create(name='Themothy', team=self.team_ptb)
		self.coach_smith = Coach.objects.create(name='smith', team=self.team_cb)

		self.game_q1 = Game.objects.create(name='q1', match_round='Qualifier', result='Won')

		self.scorecard_q1_ptb = Scorecard.objects.create(side='Host', game=self.game_q1, team=self.team_ptb, score=65)
		scorecard_q1_cb = Scorecard.objects.create(side='Visitor', game=self.game_q1, team=self.team_cb, score=78)

		participation_crmelo = Participation.objects.create(game=self.game_q1, player=self.plr_crmelo, score=18)
		participation_damian = Participation.objects.create(game=self.game_q1, player=self.plr_damian, score=12)

	def test_get_teams(self):		
		self.client.login(username='test_admin', password='test')
		url = reverse('team-list')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)
		#self.assertEqual(json.loads(response.content), [{'id':1, 'name': 'Portland Trail Blazers'}])
		self.client.logout()


	def test_get_teams_with_invalid_user(self):
		url = reverse('team-list')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_get_team(self):		
		self.client.login(username='test_admin', password='test')
		url = reverse('team-detail', kwargs={'pk': self.team_ptb.pk})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_get_players(self):
		self.client.login(username='test_admin', password='test')
		url = reverse('players-list')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 2)
		self.client.logout()


	def test_get_players_with_invalid_user(self):
		url = reverse('players-list')
		self.client.login(username='test_player', password='test')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


	def test_get_scorecard_admin(self):
		self.client.login(username='test_admin', password='test')
		url = reverse('scoreboard')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.client.logout()


	def test_get_scorecard_player(self):
		url = reverse('scoreboard')
		self.client.login(username='test_player', password='test')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_get_scorecard_invalidUser(self):
		url = reverse('scoreboard')
		self.client.login(username='user_without_roles_assigned', password='test')
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_get_team(self):		
		self.client.login(username='test_admin', password='test')
		url = reverse('team-detail', kwargs={'pk': self.team_ptb.pk})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_get_bestPlayer(self):		
		self.client.login(username='test_admin', password='test')
		url = reverse('best-players-list', kwargs={'pk': self.team_ptb.pk})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)


	def test_get_playersDetailByTeam(self):		
		self.client.login(username='test_admin', password='test')
		url = reverse('player-detail-by-team', kwargs={'pk_team': self.team_ptb.pk, 'pk_player': self.plr_crmelo.pk})
		response = self.client.get(url, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)