# MatificCodingChallenge
This is a basketball league management system

Assumptions
This is a monitoring system. Thus insertion and modification APIs are not provided
A team consists of 16 players. Not more or less than that.

Requirements
1.Django:3.0.3
2.djangorestframework:3.11.0
3.python:3.8.7


Running the server
1. Migrating Data
	1. >python manage.py makemigrations
	2. >python manage.py migrate
	
2. Running Server
	1. >python manage.py runserver

Access Url
	http://127.0.0.1:8000/api/
	
Users to Access the system
	Seperate users were creared with respect to user roles (Admin, Coach, Player)
1. Super User: chanaka/password

2. Admins: alex/1qaz2wsx@

3. Coaches: wesley/1qaz2wsx@

4. Players: marc/1qaz2wsx@



APIs
1. Overview
	List of APIs provided. No authentication requied.
	/api
	
	eg: http://127.0.0.1:8000/api/
	
2. Scoreboaed
	Thenament's scorecard. Users belonged to player, coach and admin roles can see it.
	/api/scoreboard
	
	eg: http://127.0.0.1:8000/api/scoreboard
	
3. Players List
	List of all the teams. Users belonged to admin role can see it.
	/api/players/
	
	eg: http://127.0.0.1:8000/api/players
	
4. Plater detail
	List of all the teams. Users belonged to admin role can see it.
	/api/players/[player id]
	
	eg: http://127.0.0.1:8000/api/players/10
	
5. Team List
	List of all the teams. Users belonged to admin role can see it.
	/api/teams
	
	eg: http://127.0.0.1:8000/api/teams/
	
6. Team detail
	List of all the teams. Users belonged to admin role can see it.
	/api/teams/[team id]
	
	eg: http://127.0.0.1:8000/api/teams/3
	
7. Best Players List 
	List of best players (Average is grater than 90 presentile) by the team. Users belonged to coach role can see it.
	/api/teams/[team id]/players/best
	
	eg:http://127.0.0.1:8000/api/teams/3/players/best

8. Players by team
	List of players by the team. Users belonged to coach role can see it.
	/api/teams/[team id]/players
	
	eg: http://127.0.0.1:8000/api/teams/3/players
	
9. Player detail by team
	Detail of player by the team. Users belonged to coach role can see it.
	/api/teams/[team id]/players/[player id]
	
	eg: http://127.0.0.1:8000/api/teams/3/players/10
