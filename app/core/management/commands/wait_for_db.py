"""
django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from typing import Any
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """ Django command to wait for database"""

    def handle(self, *args: Any, **options):
        self.stdout.write('waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except(Psycopg2OpError,OperationalError):
                self.stdout.write('database unavailable, wating for 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('database available'))    

