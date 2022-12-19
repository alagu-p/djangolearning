import time
from sqlite3 import OperationalError

from django.core.management import BaseCommand
from django.db import connection
import time
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self,*args, **kwargs):
        self.stdout.write('waiting for the database...')
        conn = None

        while not conn:
            try:
                conn = connection['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting for 1 secound.... ')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database avaialbe'))

