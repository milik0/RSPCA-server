from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    The accounts app config
        * default_auto_field: The default auto field
        * name: The name of the app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
