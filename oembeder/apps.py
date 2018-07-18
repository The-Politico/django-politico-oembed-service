from django.apps import AppConfig


class OembederConfig(AppConfig):
    name = 'oembeder'

    def ready(self):
        from oembeder import signals  # noqa
