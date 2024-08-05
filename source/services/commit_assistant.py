# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from .git_diff_manager import GitDiffManager
from .gemini_service import GeminiService
from ..configuration import Configuration
from ..diff_options import DiffOptions
from ..exceptions import NoChangesDetectedException
from pathlib import Path

import os

class CommitAssistant:
    def __init__(
            this,
            diff_manager: GitDiffManager,
            gemini_service: GeminiService,
            configuration: Configuration
        ):
        this.diff_manager = diff_manager
        this.gemini_service = gemini_service
        this.configuration = configuration

        this.pre_prompt = this._load_pre_prompt().format(
            configuration.language,
            configuration.max_number_of_characters
        )

    def generate_commit_message(this, options: DiffOptions = None) -> str:
        if options is None:
            options = DiffOptions()

        this.diff_manager.capture_diff(
            file_path=options.file_path,
            staged=options.only_staged
        )

        this.diff_manager.save_diff_to_temp_file()

        if not this.diff_manager.get_diff_text().strip():
            raise NoChangesDetectedException()

        full_prompt = this.pre_prompt + this.diff_manager.get_diff_text()
        commit_message = this.gemini_service.get_response(full_prompt)

        return commit_message

    def _load_pre_prompt(this) -> str:
        try:
            base_path = Path(__file__).resolve().parent.parent

            prompt_file = "prompt.txt"
            prompt_file_path = os.path.join(base_path, prompt_file)

            with open(prompt_file_path, 'r', encoding='utf-8') as file:
                return file.read()

        except FileNotFoundError:
            raise FileNotFoundError(f"The preprompt file 'prompt.txt' was not found.")