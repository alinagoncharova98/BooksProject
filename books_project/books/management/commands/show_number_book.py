from django.core.management.base import BaseCommand, CommandError
from books.models import Book


class Command(BaseCommand):
    help = 'Shows number of all books and number of books named "django"'

    def handle(self, *args, **options):
        all_names = Book.objects.count()
        named_django = Book.objects.filter(name='django').count()
        return 'All = {},\n' \
               'named "django" = {}'.format(all_names, named_django)