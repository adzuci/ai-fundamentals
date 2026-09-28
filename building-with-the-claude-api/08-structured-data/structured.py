import json
import sys
from pathlib import Path

# Course directory is the parent of this lesson folder, so `claude_chat`
# imports when this file runs from the repo root or the course folder.
_course_dir = str(Path(__file__).resolve().parent.parent)
if _course_dir not in sys.path:
    sys.path.insert(0, _course_dir)

from claude_chat import add_assistant_message, add_user_message, client, model


def chat(messages, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
    }
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    # stop_sequences is a real parameter of client.messages.create in this SDK.
    message = client.messages.create(**params)
    print(message.stop_reason)
    return message.content[0].text


def main():
    messages = []
    add_user_message(messages, "Generate a very short event bridge rule as json")
    add_assistant_message(messages, "```json")
    text = chat(messages, stop_sequences=["```"])
    print("```json" + text)
    print(repr(text))
    clean_json = json.loads(text.strip())
    print(clean_json)


if __name__ == "__main__":
    main()
