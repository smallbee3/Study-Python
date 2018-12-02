from django.core.management import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('num_of_obj', type=int)

    def handle(self, *args, **options):
        # crawler
        number_of_obj = options['num_of_obj']
        print(number_of_obj)
