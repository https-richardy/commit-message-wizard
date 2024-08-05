# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

import configparser
import os

from pathlib import Path

class Configuration:
    def __init__(this, config_file="assistant.cfg"):
        base_path = Path(__file__).resolve().parent.parent
        configuration_file = os.path.join(base_path, config_file)

        this.configuration_parser = configparser.ConfigParser()
        this.configuration_parser.read(configuration_file)

    @property
    def api_key(this) -> str:
        return this.configuration_parser.get("assistant.secrets", "gemini.apiKey")

    @property
    def language(this) -> str:
        return this.configuration_parser.get("assistant.defaults", "language")

    @property
    def max_number_of_characters(this) -> int:
        return this.configuration_parser.getint("assistant.defaults", "maxNumberOfCharacters")