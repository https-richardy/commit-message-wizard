# Commit Assistant

## About this project

CommitAssistant is a Python script designed to generate commit messages intelligently and automatically by analyzing the differences (diff) in your Git repository. This project makes it easier to create more meaningful commits, saving time and ensuring consistent messages.

## Main features

* **Commit message generation:** Based on the changes detected by git diff, CommitAssistant creates automatic and contextual commit messages.

* **Flexible options:**
    - **Complete Analysis**: Analyzes all changes to the repository.
    - **Staged only**: It only analyzes changes that are already staged (ready for commit).
    - **Specific file**: Allows you to specify a single file for analyzing changes.

## How to use

### Requirements

* Make sure you are in a Git project.
* Python 3.7 or higher installed.

## Executing the Script

There is currently no official installer, but you can create an alias to make it easier to use:

#### Linux (Bash/Zsh):

Add the following line to your `~/.bashrc` or `~/.zshrc:`

```bash
alias commit-assistant='python3 /path/to/project/assistant.py'
```

After saving the file, reload the terminal:

```bash
source ~/.bashrc
# or
source ~/.zshrc
```

#### Windows (CMD/PowerShell):

```powershell
Set-Alias commit-assistant 'C:\path\to\project\assistant.py'
```

### Examples of use

* **Analyze all changes**:
    ```bash
    commit-assistant
    ```

* **Only analyze staged changes**:
    ```bash
    commit-assistant --only-staged
    ```

* **Analyze a specific file**:
    ```bash
    commit-assistant --file-path Path/To/File.cs
    ```

| command                                             | alias               | description |
|-----------------------------------------------------|---------------------|-----------|
| `commit-assistant`                                  |                 | It analyzes all the changes in the repository and generates a commit message. |
| `commit-assistant --only-staged`                    | `-s`             | It only analyzes the changes that are already staged. |
| `commit-assistant --file-path path/to/file.py` | `-f path/to/file.py` | It analyzes a specific file to generate a commit message. |


### Configuration:

CommitAssistant uses an `assistant.cfg` configuration file to store your preferences:

```ini
[assistant.secrets]
# Your Gemini API key. You can get one here: https://aistudio.google.com/app/apikey
gemini.apiKey = YOU_GEMINI_API_KEY

[assistant.defaults]
# Default language for commit messages.
language = EN-US

# Maximum number of characters for commit messages.
maxNumberOfCharacters = 80

```

#### Important

**Don't forget to set the `gemini.apiKey` in the `assistant.cfg`** file! It is essential for CommitAssistant to work. You can obtain your API key [here](https://aistudio.google.com/app/apikey).