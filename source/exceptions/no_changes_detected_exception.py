# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

class NoChangesDetectedException(Exception):
    def __init__(this, message="No changes detected in the diff. Cannot generate commit message."):
        this.message = message

        super().__init__(this.message)