from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='Super Strength', description='Strength training', suggested_for='heroes')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-12-20')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_team(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_workout(self):
        self.assertEqual(self.workout.name, 'Super Strength')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
