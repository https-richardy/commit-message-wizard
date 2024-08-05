# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from source import ServiceCollection
from source.exceptions import NoChangesDetectedException

class Program:
    services = ServiceCollection()

    @staticmethod
    def main():
        assistant = Program.services.commit_assistant()
        arguments_parser = Program.services.arguments_parser()

        options = arguments_parser.parse_arguments()

        try:
            commit_message = assistant.generate_commit_message(options)
            print(commit_message)

        except NoChangesDetectedException as exception:
            print(exception.message)