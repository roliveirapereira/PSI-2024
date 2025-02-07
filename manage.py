"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management import execute_from_command_line
from django.core.wsgi import get_wsgi_application


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lojaAdmin.settings.production')  # Altere para 'production' ou o nome correto de sua configuração de produção
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

# Para Vercel, use a variável de ambiente `application`
application = get_wsgi_application()

if __name__ == '__main__':
    main()
