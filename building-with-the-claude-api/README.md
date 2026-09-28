# Building with the Claude API

Small Python lessons for [Building with the Claude API](https://academy.claude.com/courses/building-with-the-claude-api).

Create an API key in the [Claude Console dashboard](https://platform.claude.com/dashboard).

## Setup

Use Python 3.10 and a virtualenv named `.venv-claude` at the repo root:

```bash
python3.10 -m venv .venv-claude
source .venv-claude/bin/activate
pip install -r building-with-the-claude-api/requirements.txt
```

Add a repo-root `.env` with a placeholder key (replace it with the key from the dashboard):

```bash
ANTHROPIC_API_KEY="your-api-key-here"
```

`.env` is gitignored. Leave it out of commits.

`claude_chat.py` calls python-dotenv's `load_dotenv()` with no path. The search starts in this folder and walks up through parent directories until it finds that `.env`, then the Anthropic client reads `ANTHROPIC_API_KEY`. Lessons call the model `claude-sonnet-4-5`.

## Lessons

- `claude_chat.py` — shared client, plus `add_user_message`, `add_assistant_message`, and `chat(messages, system=None)`.
- `06-temperature/chat.py` — `chat(..., temperature=1.0)`. SDK 1.8.0 does not accept `temperature` as a direct keyword argument, so this file sends it through `extra_body`.
- `07-response-streaming/stream.py` — `messages.create(stream=True)` and prints each event.
- `07-response-streaming/text_stream.py` — `client.messages.stream`, prints each `text_stream` chunk, then calls `get_final_message`.
- `08-structured-data/structured.py` — prefills the assistant turn with `` ```json ``, stops on `stop_sequences=["```"]`, then parses the reply with `json.loads(text.strip())`.

## Run a lesson

From the repo root:

```bash
.venv-claude/bin/python building-with-the-claude-api/07-response-streaming/stream.py
```

`text_stream.py` and `08-structured-data/structured.py` run the same way. Temperature's `chat.py` defines a function and does not call the API when you execute the file.
