from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.core.management import call_command
from io import StringIO

def run_migrations(request):
    """
    Run migrations from browser - DEBUG ONLY
    """
    out = StringIO()
    try:
        call_command('migrate', '--noinput', stdout=out, verbosity=2)
        return HttpResponse(f"<pre>{out.getvalue()}</pre><h2>✅ Migrations completed!</h2><a href='/'>Go to homepage</a>")
    except Exception as e:
        return HttpResponse(f"<pre>{out.getvalue()}</pre><h2>❌ Error: {e}</h2>", status=500)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('material_app.urls')),
    path('__run_migrations__/', run_migrations),  # DEBUG ONLY - Remove after migrations run
]
