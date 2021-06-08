import os
import json
import django_heroku



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try: 
    secret_key_file = open('secret_key.txt', 'r' )
    SECRET_KEY = secret_key_file.read()
except:
    SECRET_KEY = ''

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY',SECRET_KEY)

DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True

 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'usertasksapi',
    'corsheaders',
    'rest_framework' 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',

]

ROOT_URLCONF = 'djangosample.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['usertasksapi'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangosample.wsgi.application'
 
 
try:
    #test if it is in development
    infile = open('.env.json', 'r', encoding='utf-8')
except IOError:
    #get production data 
    env = {
            "NAME":os.environ["NAME"],
            "USER":os.environ["USER"],
            "PASSWORD":os.environ["PASSWORD"],
            "HOST":os.environ["HOST"]
          }  
else:
    env = {
            "NAME":"djangosample",
            "USER":"sampleuser",
            "PASSWORD":"samplesecret",
            "HOST":"localhost"
          }  
    
 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DJANGO_DB_NAME', env["NAME"]), #djangosample
        'USER': os.environ.get('DJANGO_DB_USERNAME', env["USER"]), #sampleuser
        'PASSWORD': os.environ.get('DJANGO_DB_PASSWORD', env["PASSWORD"]), #samplesecret
        'HOST': os.environ.get('DJANGO_DB_HOST', env["HOST"]), #localhost
        'PORT': os.environ.get('DJANGO_DB_PORT', '5432'), #5432
    }
}
 
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
 
 
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True
 
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_TMP = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

os.makedirs(STATIC_TMP, exist_ok=True)
os.makedirs(STATIC_ROOT, exist_ok=True)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
 
)

if DEBUG:
    ALLOWED_HOSTS += ['*', ]

 
