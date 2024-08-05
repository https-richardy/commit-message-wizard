# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from dependency_injector import containers, providers

from .configuration import Configuration
from .parse_arguments import DiffOptionsParser
from .services.gemini_service import GeminiService
from .services.commit_assistant import CommitAssistant
from .services.git_diff_manager import GitDiffManager

class ServiceCollection(containers.DeclarativeContainer):
    configuration = providers.Singleton(Configuration)
    diff_manager = providers.Singleton(GitDiffManager)
    arguments_parser = providers.Factory(DiffOptionsParser)

    gemini_service = providers.Factory(
        GeminiService,
        configuration=configuration
    )

    commit_assistant = providers.Factory(
        CommitAssistant,
        diff_manager=diff_manager,
        gemini_service=gemini_service,
        configuration=configuration
    )