from .settings import *

SECRET_KEY = 'eel25_ixgf56y!_3un0f3ibfylv5-0ons9k*gvr%3p_-(bm!mf'

# mysql -uroot -p12345 -e "QUERY"
# CREATE DATABASE my_db CHARACTER SET utf8 COLLATE utf8_general_ci
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'natshop',
        'USER': 'root',
        'PASSWORD': '12345',
    },
}

RECAPTCHA_SITE_KEY = "6LdL3wkTAAAAAJijgcTmNBNHxDwRO1NeJ7gkOPWD"
RECAPTCHA_SECRET_KEY = "6LdL3wkTAAAAAFILI-ISubDaHI0qPoCyu8Vve8Jc"

EMAIL_HOST = "smtp.yandex.ru"
EMAIL_PORT = 465
EMAIL_HOST_USER = "no-reply@coffeestudio.ru"
EMAIL_HOST_PASSWORD = "eeK4Aish5Qua"
EMAIL_USE_SSL = True

SITE_HOST = "localhost"

ALLOWED_HOSTS = [
    SITE_HOST,
]

DEBUG = True
