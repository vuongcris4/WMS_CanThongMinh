#!/usr/bin/env python3
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'can_thong_minh.settings')
django.setup()

from django.core.management import call_command

print("📊 Running migrations...")
try:
    call_command('migrate', '--noinput', verbosity=2)
    print("✅ Migrations completed!")
except Exception as e:
    print(f"❌ Migration failed: {e}")
    sys.exit(1)
