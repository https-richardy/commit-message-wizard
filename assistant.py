# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from source import ServiceCollection, DiffOptionsParser
from source.services import CommitAssistant

services = ServiceCollection()

assistant: CommitAssistant = services.commit_assistant()
arguments_parser: DiffOptionsParser = services.arguments_parser()

if __name__ == "__main__":
    options = arguments_parser.parse_arguments()
    commit_message = assistant.generate_commit_message(options)

    print(commit_message)