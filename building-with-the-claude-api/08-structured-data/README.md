# Lesson 8: Structured data

## Why plain replies are awkward

A web app that saves an EventBridge rule needs a JSON object it can parse. Ask Claude for that rule in a normal chat turn and the reply often arrives as a sentence plus a markdown fence, then the object, then another fence. That whole string is not JSON, so the app cannot load it.

## Prefill and a stop sequence

Start the assistant turn yourself, and stop generation when Claude tries to close the fence:

```python
messages = []
add_user_message(messages, "Generate a very short event bridge rule as json")
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
```

1. The user message asks for a short EventBridge rule as JSON.
2. The assistant prefill `"```json"` opens the fence, so Claude continues inside it.
3. Claude writes the JSON object.
4. The stop sequence `"```"` ends the reply when Claude would close the fence.

## The JSON you get back

What remains is the rule itself, for an EC2 instance that changes state to running:

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
```

## Turn the text into an object

Claude still leaves extra newlines around that object. `structured.py` strips them, then parses:

```python
clean_json = json.loads(text.strip())
```

Run `structured.py` in this folder. It prints the stop reason, the raw text, and the parsed object.

## Other shapes

The same pattern works for a Python snippet, a list, or CSV. Prefill the wrapper Claude would have added, and stop on the closer.
