from django.http import HttpResponse
from django.urls import path
from django.core.wsgi import get_wsgi_application
import os

def hello(request):
    return HttpResponse("Hello, World!")

urlpatterns = [
    path('', hello),
]

# Set the application settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '__main__')

# Create the application instance
application = get_wsgi_application()

if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line()
