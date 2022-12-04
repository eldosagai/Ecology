#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
os.system("sudo apt-get install nodejs")
# os.system("cinst nodejs.install")
from time import sleep
sleep(5)
os.system("npm install json-server")
os.system("npx json-server --watch db/idForEcoHakaton/db.json")
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
