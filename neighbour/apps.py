from django.apps import AppConfig


class NeighbourConfig(AppConfig):
    name = 'neighbour'

    def ready(self):
        import neighbour.signals
