#!/bin/bash
set -e

echo "🔍 Checking database tables..."
python manage.py showmigrations

echo ""
echo "📊 Checking Unit table..."
python manage.py shell << EOF
from material_app.models import Unit
print(f"Unit count: {Unit.objects.count()}")
print(f"Units: {list(Unit.objects.all()[:5])}")
EOF

echo ""
echo "✅ Database check complete!"
