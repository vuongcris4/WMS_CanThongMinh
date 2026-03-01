web: python manage.py force_migrate && python manage.py collectstatic --noinput --clear && gunicorn can_thong_minh.wsgi:application --bind 0.0.0.0:$PORT
