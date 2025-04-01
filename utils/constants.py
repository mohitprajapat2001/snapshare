from django.utils.translation import gettext_lazy as _


class Templates:
    """Templates Constants"""

    REGISTER_TEMPLATE = "accounts/register.html"
    LOGIN_TEMPLATE = "accounts/login.html"
    PROFILE_TEMPLATE = "accounts/profile.html"


class FormSuccessMessages:
    """Form Success Messages"""

    USER_REGISTERED = _("User Registered Successfully")
    USER_LOGIN = _("User Logged In Successfully")
    USER_LOGOUT = _("User Logged Out Successfully")
    USER_UPDATED = _("User Updated Successfully")
    USER_ALREADY_LOGGED_IN = _("User Already Logged In")
    USER_NOT_LOGGED_IN = _("User Not Logged In")


class FormValdationMessages:
    """Form Validation Messages"""

    USER_NOT_FOUND = _("User Not Found")
    USER_NOT_ACTIVE = _("User Not Active")
    EMPTY_FIELD = _("This field is required")
    PASSWORD_MISMATCH = _("Passwords do not match")


# Settings Constants
# =====================================================
class Settings:
    """Settings Constants"""

    ROOT_URLCONF = "conf.urls"
    WSGI_APPLICATION = "conf.wsgi.application"
    ASGI_APPLICATION = "conf.asgi.application"
    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "Asia/Kolkata"
    USE_I18N = True
    USE_TZ = True
    STATIC_URL = "static/"
    STATIC_ROOT = "assets/"
    STATIC_FILES_DIRS = "static/"
    TEMPLATES_URLS = "templates/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = "media/"
    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
