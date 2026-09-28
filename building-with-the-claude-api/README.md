# Building with the Claude API

Course code for [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api).

`claude_chat.py` is a small helper: it creates an Anthropic client (`claude-sonnet-4-5`) and defines `add_user_message`, `add_assistant_message`, and `chat`.

## Setup

Use the macOS virtual environment at the repo root:

```bash
source .venv-claude/bin/activate
```

`ANTHROPIC_API_KEY` is loaded from the repo-root `.env` via python-dotenv (`load_dotenv` in `claude_chat.py` walks up from this folder and finds that file).
