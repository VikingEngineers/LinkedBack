from django.apps import AppConfig


class LmUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lm_users'

    def ready(self):
        import lm_users.signals
