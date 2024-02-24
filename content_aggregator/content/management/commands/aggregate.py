from django.core.management.base import BaseCommand, CommandError
from content.service import Feed

'''
   RUN: python3 manage.py aggregate [count]
'''
class Command(BaseCommand):
    help = "runs the Feed() aggregator"

    def add_arguments(self, parser):
        parser.add_argument("count", nargs="+", type=int)

    def handle(self, *args, **options):
        if options.get('count'):
            feed = Feed(count=options.get("count")[0])
        else:
            feed = Feed()

        self.stdout.write(
            self.style.SUCCESS('Beginning fetch of feeds')
        )

        feed.run()


        self.stdout.write(
            self.style.SUCCESS('Successfully fetched feeds')
        )