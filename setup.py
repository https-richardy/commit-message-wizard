# author: Richard Garcia (https://github.com/https-richardy)
# license: MIT

from setuptools import setup, find_packages

setup(
    name="commit-assistant",
    version="0.1.0",
    py_modules=["assistant"],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            "commit-assistant=assistant:Program.main"
        ],
    },
    author="Richard Garcia",
    author_email="code.richardy@gmail.com",
    description="A wizard for generating commit messages",
    license="MIT",
)