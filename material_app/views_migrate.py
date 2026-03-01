from django.http import HttpResponse
from django.core.management import call_command
from io import StringIO

def run_migrations_view(request):
    """
    View để chạy migrations từ browser
    Only accessible in DEBUG mode
    """
    if not request.META.get('SERVER_SOFTWARE', '').startswith('gunicorn'):
        return HttpResponse("Not allowed", status=403)
    
    out = StringIO()
    try:
        call_command('migrate', '--noinput', stdout=out)
        return HttpResponse(f"<pre>{out.getvalue()}</pre><h2>✅ Migrations completed!</h2>")
    except Exception as e:
        return HttpResponse(f"<pre>{out.getvalue()}</pre><h2>❌ Error: {e}</h2>", status=500)
