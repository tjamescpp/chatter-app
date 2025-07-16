#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twtapp.settings")
    try:
        from django.core.management import execute_from_command_line

        # Get port from environment or default to 8000
        port = os.environ.get("PORT", "8000")
        args = sys.argv

        if len(args) == 1 or (args[1] == "runserver" and len(args) == 2):
            args += [f"0.0.0.0:{port}"]
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
