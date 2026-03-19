from pathlib            import Path
from decouple           import config
from django.conf.locale import LANG_INFO

LANG_INFO.update({
    'hmn': {
        'bidi': False,
        'code': 'hmn',
        'name': 'Hmong',
        'name_local': 'Hmong',
    },
})

BASE_DIR        = Path(__file__).resolve().parent.parent
SECRET_KEY      = config('SECRET_KEY')
DEBUG           = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS   = config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',')])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'modeltranslation',
    'mapwidgets',
    'core',
]

PHONENUMBER_DEFAULT_REGION  = "US"
MAP_WIDGETS = {
    "GoogleMap": {
        "apiKey": config('GOOGLE_MAP_API_KEY'),
        "CDNURLParams": {
            "language": "en",
            "libraries": "places,marker",
            "loading": "defer",
            "v": "quarterly",
        },
        "PointField": {
            "interactive": {
                "mapOptions": {
                    "zoom": 12,
                    "scrollwheel": False,
                    "streetViewControl": True,
                },
                "GooglePlaceAutocompleteOptions": {},
                "mapCenterLocationName": "Fresno, CA, USA",
                "markerFitZoom": 14,
            },
        },
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project_resource_library.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'project_resource_library.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
		'ENGINE': 		'django.contrib.gis.db.backends.postgis',
		'NAME': 		'cvlibrary',
		'USER': 		'cvlibraryuser',
		'PASSWORD': 	config('DATABASE_PASS'),
		'HOST': 		'localhost',
		'PORT': 		'5432',
	}
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE   = 'en-us'
LANGUAGES       = [
    ('en', 'English'),
    ('es', 'Spanish'),
    ('pa', 'Punjabi'),
    ('hmn', 'Hmong'),
]
TIME_ZONE       = 'America/Los_Angeles'
USE_I18N        = True
USE_TZ          = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL          = '/static/'
STATIC_ROOT         = BASE_DIR / 'staticfiles'
STATICFILES_DIRS    = [BASE_DIR / 'static']
MEDIA_URL           = '/media/'
MEDIA_ROOT          = BASE_DIR / 'media'
BASE_URL            = config('BASE', default='http://url.com')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'