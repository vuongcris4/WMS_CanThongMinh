from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Force run migrations with verbose output'

    def handle(self, *args, **options):
        self.stdout.write('🚀 Starting force migrations...')
        try:
            call_command('migrate', '--noinput', verbosity=2)
            self.stdout.write(self.style.SUCCESS('✅ Migrations completed!'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Migration failed: {e}'))
            raise
