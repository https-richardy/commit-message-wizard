# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

import subprocess
import tempfile

class GitDiffManager:
    def __init__(this):
        this.diff_text = None
        this.temp_file = None

    def capture_diff(this) -> None:
        result = subprocess.run(["git", "diff"], capture_output=True, text=True)
        this.diff_text = result.stdout

    def save_diff_to_temp_file(this):
        this.temp_file = tempfile.NamedTemporaryFile(
            delete=False, mode='w+',
            encoding='utf-8'
        )

        this.temp_file.write(this.diff_text)
        this.temp_file.seek(0)

    def get_temp_file_path(this):
        if not this.temp_file:
            raise ValueError("The diff has not yet been saved to a temporary file.")
        return this.temp_file.name

    def get_diff_text(this):
        return this.diff_text