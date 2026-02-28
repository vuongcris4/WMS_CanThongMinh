#!/bin/bash
set -e

echo "🚀 Starting WMS Can Thong Minh..."

# Run database migrations
echo "📊 Running database migrations..."
python manage.py migrate --noinput --verbosity=2

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput --clear

# Start the server
echo "🌐 Starting server..."
gunicorn can_thong_minh.wsgi:application --bind 0.0.0.0:$PORT
