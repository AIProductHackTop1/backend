from dependency_injector import containers, providers

from src.services.pallet_classifier import PalletClassifier


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    pallete_classifier = providers.Singleton(
        PalletClassifier,
        config.classifier_settings,
    )
