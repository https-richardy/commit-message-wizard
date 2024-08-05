# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from dataclasses import dataclass

@dataclass
class DiffOptions:
    only_staged: bool = False
    file_path: str = None
