from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "medical_lab.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import medical_lab.users.signals  # noqa F401
        except ImportError:
            pass
