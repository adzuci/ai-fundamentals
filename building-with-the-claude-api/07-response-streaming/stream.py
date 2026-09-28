import sys
from pathlib import Path

# Course directory is the parent of this lesson folder, so `claude_chat`
# imports when this file runs from the repo root or the course folder.
_course_dir = str(Path(__file__).resolve().parent.parent)
if _course_dir not in sys.path:
    sys.path.insert(0, _course_dir)

from claude_chat import add_user_message, client, model


def main():
    messages = []
    add_user_message(messages, "Write a 1 sentence description of a fake database")

    stream = client.messages.create(
        model=model,
        max_tokens=1000,
        messages=messages,
        stream=True,
    )

    for event in stream:
        print(event)


if __name__ == "__main__":
    main()
