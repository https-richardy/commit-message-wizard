from dependency_injector import containers, providers

from .configuration import Configuration
from .gemini_service import GeminiService

class ServiceCollection(containers.DeclarativeContainer):
    configuration = providers.Singleton(Configuration)
    gemini_service = providers.Factory(
        GeminiService,
        configuration=configuration
    )