"""
settings_production.py - إعدادات بديلة آمنة للإنتاج
استخدم هذا الملف إذا أردت نسخة أكثر أماناً

طريقة الاستخدام:
في PythonAnywhere WSGI file:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings_production')
"""

from pathlib import Path
import os

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# أمان متقدم
# ========================
DEBUG = False

# احصل على SECRET_KEY من environment variable (الأفضل)
# في PythonAnywhere : اذهب إلى Web → Environment variables
SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-default-key")

# إضافة النطاق الفعلي فقط
ALLOWED_HOSTS = [
    "YOUR_USERNAME.pythonanywhere.com",
    "www.YOUR_USERNAME.pythonanywhere.com",
]

# ========================
# تطبيقات مثبتة
# ========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "Marketer",
]

# ========================
# Middleware
# ========================
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ========================
# URLs و Templates
# ========================
ROOT_URLCONF = "portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "portfolio.wsgi.application"

# ========================
# قاعدة البيانات
# ========================
# SQLite للتطوير - غيّر إلى PostgreSQL في الإنتاج
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ========================
# التحقق من كلمات المرور
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ========================
# Internationalization
# ========================
LANGUAGE_CODE = "ar-sa"  # العربية (اختياري)
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ========================
# Static Files - مهم جداً
# ========================
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    BASE_DIR / "Marketer" / "static",
]

# ========================
# إعدادات الأمان الإضافية
# ========================
# HTTPS فقط
SECURE_SSL_REDIRECT = False  # اجعله True إذا كان لديك HTTPS

# Headers الأمان
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_SECURITY_POLICY = {
    "default-src": ("'self'",),
}

# Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ========================
# Logging (اختياري)
# ========================
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": BASE_DIR / "logs" / "django.log",
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "ERROR",
    },
}

"""
ملاحظات:

1. استخدم environment variables لـ SECRET_KEY في الإنتاج:
   في PythonAnywhere:
   - اذهب إلى Web → Environment variables
   - أضف: SECRET_KEY = your-secret-key-here

2. لتغيير DATABASE إلى PostgreSQL لاحقاً:
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'your_db_name',
           'USER': 'your_db_user',
           'PASSWORD': 'your_db_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }

3. لتفعيل HTTPS:
   SECURE_SSL_REDIRECT = True
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
"""
