import sys
from pathlib import Path

# Course directory is the parent of this lesson folder, so `claude_chat`
# imports when this file runs from the repo root or the course folder.
_course_dir = str(Path(__file__).resolve().parent.parent)
if _course_dir not in sys.path:
    sys.path.insert(0, _course_dir)

from claude_chat import client, model


def chat(messages, system=None, temperature=1.0):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature
    }

    if system:
        params["system"] = system

    # This SDK takes temperature via extra_body.
    message = client.messages.create(
        **{key: value for key, value in params.items() if key != "temperature"},
        extra_body={"temperature": params["temperature"]},
    )
    return message.content[0].text
