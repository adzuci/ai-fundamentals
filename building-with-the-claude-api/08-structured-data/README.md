# Lesson 8: Structured data

This folder is lesson 8 (structured data) of Building with the Claude API.
`structured.py` prefills the assistant turn with `` ```json `` and stops generation at `` ``` `` so the reply is a JSON object. It then parses that text with `json.loads`.

From the repo root, run `.venv-claude/bin/python building-with-the-claude-api/08-structured-data/structured.py`. The script prints the stop reason, the raw text, and the parsed object.


Example of the kind of EventBridge rule the lesson describes:

```json
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
```

This rule captures EC2 instance state changes when instances start running.
