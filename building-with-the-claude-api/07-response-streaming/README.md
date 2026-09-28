# Lesson 7: Response streaming

This folder is lesson 7 (response streaming) of Building with the Claude API.
`stream.py` sends one user message and prints each streaming event from `client.messages.create(..., stream=True)`.
`text_stream.py` streams the same prompt with `client.messages.stream` and prints each text chunk plus the final message text.
The Anthropic client, model, and `add_user_message` are imported from the course module `claude_chat.py`.

From the repo root, run `.venv-claude/bin/python building-with-the-claude-api/07-response-streaming/stream.py` to print each event. Use the same command with `text_stream.py` to print text chunks and the final message.
