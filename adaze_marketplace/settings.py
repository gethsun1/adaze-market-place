"""
Django settings for adaze_marketplace project.
"""

import os
from pathlib import Path
import environ 

# Initialize environment variables
env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(Path(__file__).resolve().parent.parent / ".env")

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = env("SECRET_KEY", default="django-insecure-default-key-for-dev")
DEBUG = True


# ALLOWED_HOSTS
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=["localhost", "127.0.0.1", "adaze.com", "adaze-market-place.onrender.com"])


# Application definition
INSTALLED_APPS = [
    'jazzmin',  # Jazzmin must be listed before django.contrib.admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'products',
    'orders',
    'transporters',
    'markets',
    'storage',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # For serving static files in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'adaze_marketplace.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],  # Custom templates directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'adaze_marketplace.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT'),
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]  # Directory for your static files
STATIC_ROOT = BASE_DIR / "staticfiles"  # Directory for collectstatic in production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'  # WhiteNoise for static files

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"  # Directory for uploaded media files

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# CSRF trusted origins
# CSRF trusted origins
CSRF_TRUSTED_ORIGINS = env.list("CSRF_TRUSTED_ORIGINS", default=["https://adaze-market-place.onrender.com"])

# Jazzmin settings for admin interface customization
JAZZMIN_SETTINGS = {
    "site_logo": "images/logo.png",
    "welcome_sign": "Welcome to Adaze Admin",
    "site_title": "Adaze Marketplace Admin",
    "site_header": "Adaze Admin",
    "site_brand": "Adaze Marketplace",
    "site_logo": "admin/images/adaze_logo.png",
    "login_logo": "admin/images/login_logo.png",
    "login_logo_dark": "admin/images/login_logo_dark.png",
    "show_sidebar": True,
    "navigation_expanded": True,
    "search_model": "users.CustomUser",
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "products"},
        {"name": "Support", "url": "https://support.adaze.com", "new_window": True},
    ],
    "custom_css": "admin/css/custom_admin.css",
    "custom_js": "admin/js/custom.js",
    "theme": "flatly",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
    },
    "custom_fonts": ["Roboto", "Open Sans"],
    "language_chooser": True,
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "accent": "accent-primary",
    "navbar": "navbar-dark navbar-primary",
    "no_navbar_border": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": True,
    "footer_small_text": False,
    "footer_fixed": False,
    "layout_fixed": True,
}
