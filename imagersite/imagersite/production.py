
from imagersite.settings import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ["127.0.0.1",
                 "", "",
                 "",
                 '"]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, 'imagersite', 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'MEDIA')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST_PASSWORD = '!QAZZ12344'
EMAIL_HOST_USER = 'regenal@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
SERVER_EMAIL = 'regenal@gmail.com'
DEFAULT_FROM_EMAIL = 'Back to you.'
