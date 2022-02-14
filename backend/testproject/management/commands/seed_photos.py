import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from account import models as user_models
from testproject import models as post_models
import random

class Command(BaseCommand):
    
    help = "This command creates posts"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help="how many posts do you want")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()

        random_idx=list(i for i in range(100))

        seeder.add_entity(post_models.testData, number, {
            "user": lambda x: random.choice(all_user),
            "image": lambda x:  f"images/insta{random.choice(random_idx)}.jpg",

            "views_cnt": lambda x: random.randint(1,10000),
            "impressions_cnt": lambda x: random.randint(100000,10000000),
            "text_length": lambda x: random.randint(1,10000),
            "image_cnt": lambda x: random.randint(1,10000),
            "like": lambda x: random.randint(1,10000),
            "importance": lambda x: random.randint(1,10000),
        })

        created_room = seeder.execute()
        created_clean = flatten(list(created_room.values()))

        self.stdout.write(self.style.SUCCESS(f"{number} of lists Created"))