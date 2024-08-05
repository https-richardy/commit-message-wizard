# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from source import ServiceCollection, DiffOptionsParser
from source.services import CommitAssistant
from source.exceptions import NoChangesDetectedException

services = ServiceCollection()

assistant: CommitAssistant = services.commit_assistant()
arguments_parser: DiffOptionsParser = services.arguments_parser()

if __name__ == "__main__":
    options = arguments_parser.parse_arguments()
    try:
        commit_message = assistant.generate_commit_message(options)
    except NoChangesDetectedException as exception:
        print(exception.message)

    print(commit_message)