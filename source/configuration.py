# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

import configparser
import os

class Configuration:
    def __init__(this, base_path=None, config_file="assistant.cfg"):
        this.base_path = base_path or os.getcwd()
        configuration_file = os.path.join(this.base_path, config_file)

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