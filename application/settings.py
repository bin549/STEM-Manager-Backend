import os
import sys
from datetime import timedelta
from conf.env import *
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure--z8%exyzt7e_%i@1+#1mm=%lb5=^fx_57=1@a+_y7bg5-w%)sm'
sys.path.insert(0, os.path.join(BASE_DIR, 'plugins'))

DEBUG = locals().get('DEBUG', True)
ALLOWED_HOSTS = locals().get('ALLOWED_HOSTS', ['*'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_comment_migrate',
    'rest_framework',
    'django_filters',
    'corsheaders',
    'dvadmin.system',
    'drf_yasg',
    'captcha',
    'course.apps.CourseConfig',
    'users.apps.UsersConfig',
    'django_oss_storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'dvadmin.utils.middleware.ApiLoggingMiddleware',
]

ROOT_URLCONF = 'application.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'application.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

AUTH_USER_MODEL = 'system.Users'
USERNAME_FIELD = 'username'

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


LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

MEDIA_ROOT = 'media'
MEDIA_URL = "/media/"  # ???STATIC_URL???????????????????????????????????????url????????????

# ?????????????????????????????? MEDIA_ROOT,STATICFILES_DIRS?????????
# python manage.py collectstatic
# STATIC_ROOT=os.path.join(BASE_DIR,'static')
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True  # ????????????????????????????????????????????????cookie?????????

# log ????????????BEGIN #
SERVER_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'server.log')
ERROR_LOGS_FILE = os.path.join(BASE_DIR, 'logs', 'error.log')
if not os.path.exists(os.path.join(BASE_DIR, 'logs')):
    os.makedirs(os.path.join(BASE_DIR, 'logs'))

# ??????:[2020-04-22 23:33:01][micoservice.apps.ready():16] [INFO] ??????????????????:
# ??????:[??????][??????.????????????():??????] [??????] ??????
STANDARD_LOG_FORMAT = '[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s'
CONSOLE_LOG_FORMAT = '[%(asctime)s][%(name)s.%(funcName)s():%(lineno)d] [%(levelname)s] %(message)s'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': STANDARD_LOG_FORMAT
        },
        'console': {
            'format': CONSOLE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'file': {
            'format': CONSOLE_LOG_FORMAT,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': SERVER_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 5,  # ????????????5???
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ERROR_LOGS_FILE,
            'maxBytes': 1024 * 1024 * 100,  # 100 MB
            'backupCount': 3,  # ????????????3???
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        'django': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        'scripts': {
            'handlers': ['console', 'error', 'file'],
            'level': 'INFO',
        },
        'django.db.backends': {
            'handlers': [],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%d %H:%M:%S",  # ????????????????????????
    'DATE_FORMAT': "%Y-%m-%d",
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'dvadmin.utils.filters.CustomDjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'dvadmin.utils.pagination.CustomPagination',  # ???????????????
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',  # ??????????????????????????????????????????????????????
        # 'rest_framework.permissions.IsAdminUser', # is_staff=True???????????? ?????? ?????????(??????)??????
        'rest_framework.permissions.AllowAny', # ????????????
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly', # ????????? ?????? ????????????(self.list,self.retrieve)
    ],
    'EXCEPTION_HANDLER': 'dvadmin.utils.exception.CustomExceptionHandler',  # ????????????????????????
}

AUTHENTICATION_BACKENDS = [
    'dvadmin.utils.backends.CustomBackend'
]
# ================================================= #
# ****************** simplejwt?????? ***************** #
# ================================================= #

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('JWT',),
    'ROTATE_REFRESH_TOKENS': True,
}

# ====================================#
# ****************swagger************#
# ====================================#
SWAGGER_SETTINGS = {
    # ????????????
    'SECURITY_DEFINITIONS': {
        "basic": {
            'type': 'basic'
        }
    },
    # ?????????????????????????????????????????????, ?????????????????????restframework?????????.
    'LOGIN_URL': 'apiLogin/',
    # 'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    # 'DOC_EXPANSION': None,
    # 'SHOW_REQUEST_HEADERS':True,
    # 'USE_SESSION_AUTH': True,
    # 'DOC_EXPANSION': 'list',
    # ???????????????????????????????????????????????????
    'APIS_SORTER': 'alpha',
    # ????????????json??????, ????????????????????????json?????????
    'JSON_EDITOR': True,
    # ????????????????????????
    'OPERATIONS_SORTER': 'alpha',
    'VALIDATOR_URL': None,
    'AUTO_SCHEMA_TYPE': 2,  # ????????????url????????????0???1 ??? 2 ???
    'DEFAULT_AUTO_SCHEMA_CLASS': 'dvadmin.utils.swagger.CustomSwaggerAutoSchema',
}

CAPTCHA_STATE = True
CAPTCHA_IMAGE_SIZE = (160, 60)  # ?????? captcha ????????????
CAPTCHA_LENGTH = 4  # ????????????
CAPTCHA_TIMEOUT = 1  # ??????(minutes)
CAPTCHA_OUTPUT_FORMAT = '%(image)s %(text_field)s %(hidden_field)s '
CAPTCHA_FONT_SIZE = 40
CAPTCHA_FOREGROUND_COLOR = '#0033FF'
CAPTCHA_BACKGROUND_COLOR = '#F5F7F4'
CAPTCHA_NOISE_FUNCTIONS = (
    'captcha.helpers.noise_arcs',
    'captcha.helpers.noise_dots',
)
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #???????????????
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'  # ?????????????????????

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
API_LOG_ENABLE = True
# API_LOG_METHODS = 'ALL' # ['POST', 'DELETE']
API_LOG_METHODS = ['POST', 'UPDATE', 'DELETE', 'PUT']  # ['POST', 'DELETE']
API_MODEL_MAP = {
    "/token/": "????????????",
    "/api/login/": "????????????",
    "/api/plugins_market/plugins/": "????????????",
}
# ?????????
TABLE_PREFIX = ""
DJANGO_CELERY_BEAT_TZ_AWARE = False
CELERY_TIMEZONE = 'Asia/Shanghai'  # celery ????????????
# ??????????????????
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
# ?????????????????????????????????????????????????????????
INITIALIZE_RESET_LIST = []
ALL_MODELS_OBJECTS = []  # ??????app models ??????

DEFAULT_FILE_STORAGE = 'django_oss_storage.backends.OssMediaStorage'
OSS_ACCESS_KEY_ID = os.environ.get('OSS_ACCESS_KEY_ID', '')
OSS_ACCESS_KEY_SECRET = os.environ.get('OSS_ACCESS_KEY_SECRET', '')
OSS_BUCKET_NAME = 'mortem'
OSS_ENDPOINT = 'oss-cn-guangzhou.aliyuncs.com'

# dvadmin ??????
REGISTER_PLUGINS = (
    # ""
)
