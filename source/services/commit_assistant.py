# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from .git_diff_manager import GitDiffManager
from .gemini_service import GeminiService

class CommitAssistant:
    def __init__(this, diff_manager: GitDiffManager, gemini_service: GeminiService):
        this.diff_manager: GitDiffManager = diff_manager,
        this.gemini_service: GeminiService = gemini_service

        this.pre_prompt = this._load_pre_prompt()

    def generate_commit_message(this) -> str:
        this.diff_manager.capture_diff()
        this.diff_manager.save_diff_to_temp_file()

        full_prompt = this.pre_prompt + this.diff_manager.get_diff_text()
        commit_message = this.gemini_service.get_response(full_prompt)

        return commit_message

    def _load_pre_prompt(this) -> str:
        return "Olhe esse meu dif: \n\n"