from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Leaderboard, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Clear existing data

        # Drop collections directly using pymongo to avoid Djongo deletion issues
        from django.db import connections
        db = connections['default'].connection
        if db is not None:
            for coll in ['activities', 'leaderboard', 'workouts', 'users', 'teams']:
                db.get_collection(coll).drop()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (superheroes)
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        from datetime import date
        activities = [
            Activity.objects.create(user=users[0], type='run', duration=30, date=date.today()),
            Activity.objects.create(user=users[1], type='cycle', duration=60, date=date.today()),
            Activity.objects.create(user=users[2], type='swim', duration=45, date=date.today()),
            Activity.objects.create(user=users[3], type='run', duration=25, date=date.today()),
            Activity.objects.create(user=users[4], type='cycle', duration=70, date=date.today()),
            Activity.objects.create(user=users[5], type='swim', duration=50, date=date.today()),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Morning Cardio', description='Cardio workout for all', suggested_for='All'),
            Workout.objects.create(name='Strength Training', description='Strength workout for superheroes', suggested_for='Superheroes'),
        ]

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=270)
        Leaderboard.objects.create(team=dc, points=255)


        # Ensure unique index on email using pymongo
        from django.db import connections
        db = connections['default'].connection
        if db is not None:
            db.get_collection('users').create_index('email', unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
