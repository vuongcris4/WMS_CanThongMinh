from django.apps import AppConfig


class MaterialAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'material_app'

    def ready(self):
        import material_app.signals  # Import file signals để kích hoạt
