from django.db import models

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title

class Team(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Coach(models.Model):
	name = models.CharField(max_length=200, null=True)
	team = models.ForeignKey(Team, null=True, on_delete= models.SET_NULL)
	#to do
	#owner = models.ForeignKey('auth.user', null=True, related_name='coaches', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Player(models.Model):
	name = models.CharField(max_length=200, null=True)
	height = models.CharField(max_length=200, null=True)
	team = models.ForeignKey(Team, null=True, on_delete= models.SET_NULL)
	#to do
	#owner = models.ForeignKey('auth.user', null=True, related_name='players', on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Game(models.Model):
	ROUND = (
			('Qualifier', 'Qualifier'),
			('Quater Final', 'Quater Final'),
			('Semi Final', 'Semi Final'),
			('Final', 'Final'),
			) 

	RESULT = (
			 ('Won', 'Won'),
			 ('Drawn', 'Drawn'),
			 ('Abandoned', 'Abandoned'),
			 ('Scheduled', 'Scheduled'),
			 ('Cancelled', 'Cancelled'),
			 ) 

	name = models.CharField(max_length=200, null=True)
	date_played = models.DateTimeField(auto_now_add=True, null=True)
	match_round = models.CharField(max_length=200, null=True, choices=ROUND)
	result = models.CharField(max_length=200, null=True, choices=RESULT)

	def __str__(self):
		return self.name

class Scorecard(models.Model):
	SIDE = (
			('Host', 'Host'),
			('Visitor', 'Visitor'),
			) 
	side = models.CharField(max_length=200, null=True, choices=SIDE)
	game = models.ForeignKey(Game, null=True, on_delete= models.SET_NULL)
	team = models.ForeignKey(Team, null=True, on_delete= models.SET_NULL)
	score = models.IntegerField(null=True)
	
	def __str__(self):
		return self.side

class Participation(models.Model):
	game =  models.ForeignKey(Game, null=True, on_delete= models.SET_NULL)
	player =  models.ForeignKey(Player, null=True, on_delete= models.SET_NULL)
	score = models.IntegerField(null=True)


