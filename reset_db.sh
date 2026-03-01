#!/bin/bash
# Script để reset và migrate database
set -e

echo "🔄 Resetting database..."
python manage.py flush --noinput || true

echo "📊 Running migrations..."
python manage.py migrate --noinput

echo "✅ Done!"
