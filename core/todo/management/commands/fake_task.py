from django.core.management.base import BaseCommand, CommandError
from todo.models import Task
from django.contrib.auth.models import User
from faker import Faker
import random

class Command(BaseCommand):
    help = "Creates fake tasks in db"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()
    

    def handle(self, *args, **options):
        user = User.objects.create_user(self.fake.name(),self.fake.email(),"abcd!@~12312313")

        for _ in range(5):
            task = Task.objects.create(
                user=user, title=self.fake.sentence(), completed=random.choice([True,False])                
            )
        print('tasks created')