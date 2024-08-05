# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from argparse import ArgumentParser
from .diff_options import DiffOptions

class DiffOptionsParser:
    def __init__(this):
        this._parser = ArgumentParser(description="Generate a commit message based on git diff.")
        this._add_arguments()

    def _add_arguments(this) -> None:
        this._parser.add_argument(
            "--only-staged",
            action="store_true",
            help="Capture only staged changes."
        )

        this._parser.add_argument(
            "--file-path",
            type=str,
            help="Specify a file to capture the diff from."
        )

    def parse_arguments(this) -> DiffOptions:
        arguments = this._parser.parse_args()

        return DiffOptions(
            only_staged=arguments.only_staged,
            file_path=arguments.file_path
        )
