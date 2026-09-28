# Building with the Claude API

Python notes and scripts for [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api).

Create an API key in the [Claude Console dashboard](https://platform.claude.com/dashboard).

## Setup

From the repo root, with Python 3.10:

```bash
python3.10 -m venv .venv-claude
source .venv-claude/bin/activate
pip install -r building-with-the-claude-api/requirements.txt
```

Add a repo-root `.env` (gitignored) and replace the placeholder with the key from the dashboard:

```bash
ANTHROPIC_API_KEY="your-api-key-here"
```

The lessons call the model `claude-sonnet-4-5`.

## Lessons

1. [Making a request](01-making-a-request/README.md)
2. [Multi-turn conversations](02-multi-turn-conversations/README.md)
3. [Build a simple chat bot](03-build-a-simple-chat-bot/README.md)
4. [System prompts](04-system-prompts/README.md)
5. [Exercise on writing a system prompt](05-exercise-on-writing-a-system-prompt/README.md)
6. [Temperature](06-temperature/README.md)
7. [Response streaming](07-response-streaming/README.md)
8. [Structured data](08-structured-data/README.md)

Lessons 3 and 5 are video titles in that course sequence. They do not have separate Academy articles, so those folders are notes only.

Shared helpers live in `claude_chat.py`: `add_user_message`, `add_assistant_message`, and `chat`.
