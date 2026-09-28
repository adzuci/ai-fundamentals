# Lesson 6: Temperature

This folder is lesson 6 (temperature) of Building with the Claude API.
`chat()` accepts messages, an optional system prompt, and temperature (default 1.0).
The Anthropic client and model are imported from the course module `claude_chat.py`.
This SDK does not accept `temperature` as a direct `messages.create` argument, so `chat()` sends it through `extra_body`.

Executing this file only defines `chat`; it does not call the API. From the repo root, start `.venv-claude/bin/python`, import `chat` from `building-with-the-claude-api/06-temperature/chat.py`, build a messages list, and print `chat(messages)` or `chat(messages, temperature=0)`.
