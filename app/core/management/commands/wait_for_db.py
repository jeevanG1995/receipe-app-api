"""
    django commad to wait for db to be available
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for db...')
        self.stdout.write('db available')
        db_up=False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up=True
            except (OperationalError, Psycopg2Error):
                self.stdout.write('db unavailable, waiting 1 sec...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('db available'))