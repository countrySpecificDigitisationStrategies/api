import os

from django.utils.translation import gettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ['APP_SECRET_KEY']

DEBUG = os.environ.get('APP_DEBUG', True)

ALLOWED_HOSTS = '*'

INSTALLED_APPS = [
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'django_filters',
    'api',
    'drf_yasg',
    'storages'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'api/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages'
            ]
        }
    }
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT')
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'
    }
]

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

# CUSTOM
AUTH_USER_MODEL = 'api.User'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

#MEDIA_URL =  '/media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'api.authentication.token_authentication.TokenAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'COERCE_DECIMAL_TO_STRING': False,
    #'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S"
}

AWS_DEFAULT_ACL = None
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_QUERYSTRING_AUTH = False

JET_DEFAULT_THEME = 'light-gray'

JET_SIDE_MENU_COMPACT = True

JET_CHANGE_FORM_SIBLING_LINKS = True

JET_SIDE_MENU_ITEMS = [
    {
        'label': _('system'),
        'items': [
            {'name': 'api.user', 'label': _('users')},
            {'name': 'api.country', 'label': _('countries')},
            {'name': 'api.board', 'label': _('boards')},
            {'name': 'api.analysis', 'label': _('analyses')}
        ]
    },
    {
        'label': _('application'),
        'items': [
            {'name': 'api.buildingblock', 'label': _('building_blocks')},
            {'name': 'api.situationcategory', 'label': _('situation_categories')},
            {'name': 'api.situation', 'label': _('situations')},
            {'name': 'api.measure', 'label': _('measures')},
            {'name': 'api.strategy', 'label': _('strategies')}
        ]
    },
    {
        'label': _('strategy_threads_and_comments'),
        'items': [
            {'name': 'api.strategythread', 'label': _('strategy_threads')},
            {'name': 'api.strategycomment', 'label': _('strategy_comments')}
        ]
    },
    {
        'label': _('building_block_threads_and_comments'),
        'items': [
            {'name': 'api.buildingblockthread', 'label': _('building_block_threads')},
            {'name': 'api.buildingblockcomment', 'label': _('building_block_comments')}
        ]
    },
    {
        'label': _('situation_category_threads_and_comments'),
        'items': [
            {'name': 'api.situationcategorythread', 'label': _('situation_category_threads')},
            {'name': 'api.situationcategorycomment', 'label': _('situation_category_comments')}
        ]
    },
    {
        'label': _('situation_threads_and_comments'),
        'items': [
            {'name': 'api.situationthread', 'label': _('situation_threads')},
            {'name': 'api.situationcomment', 'label': _('situation_comments')}
        ]
    },
    {
        'label': _('strategy_measure_threads_and_comments'),
        'items': [
            {'name': 'api.strategymeasurethread', 'label': _('strategy_measure_threads')},
            {'name': 'api.strategymeasurecomment', 'label': _('strategy_measure_comments')}
        ]
    }
]

REDOC_SETTINGS = {
   #'SPEC_URL': 'http://192.168.178.180:8000/static/openapi.json'
}

CORS_ORIGIN_ALLOW_ALL = True

CSRF_TRUSTED_ORIGINS = ['sysdev-api.therealbrudi.com']
