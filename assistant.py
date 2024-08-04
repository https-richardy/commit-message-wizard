# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from source import ServiceCollection
from source.services import CommitAssistant

services = ServiceCollection()
assistant: CommitAssistant = services.commit_assistant()

if __name__ == "__main__":
    commit_message = assistant.generate_commit_message()
    print(commit_message)