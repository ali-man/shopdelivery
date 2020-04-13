import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'h29x&az=8zy+o&&wz66vym46(4o6t((&ix2snucn+3phv5qr!9'

# SECURITY WARNING: don't run with debug turned on in production!
LOCAL = True

if LOCAL:
    DEBUG = True
else:
    DEBUG = False

if LOCAL:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = ['*']


INSTALLED_APPS = [
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',

    'django.contrib.sites',
    'django.contrib.flatpages',

    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # libs
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'mptt',
    'imagekit',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'shopdelivery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopdelivery.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


LANGUAGE_CODE = 'ru-Ru'

TIME_ZONE = 'Asia/Samarkand'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

# -------------------- ckeditor -----------------------
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_JQUERY_URL = 'static/js/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'width': '100%',
        'height': 70,
        'extraPlugins': ','.join([
            'embed', 'iframe'
        ]),
    }, }
CKEDITOR_IMAGE_BACKEND = 'pillow'
# -------------------- ckeditor -----------------------

ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'

MEDIA_ROOT = (os.path.join(BASE_DIR, 'media'))
MEDIA_URL = "/media/"

STATIC_URL = '/static/'
if LOCAL:
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
    )
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)