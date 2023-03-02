#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import string
from nltk.corpus import stopwords

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsAggregator.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def process(text):
        nopunc = [char for char in text if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        clean = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
        return clean

if __name__ == '__main__':
    main()
    def process(text):
        nopunc = [char for char in text if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        clean = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
        return clean
