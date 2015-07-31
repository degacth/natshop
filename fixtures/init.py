import os, sys
import django

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
settings = os.environ.get('DJANGO_SETTING', "settings.prod")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
django.setup()
