# Lesson 6: Temperature

Temperature changes how predictable the next reply is. Lower values stick closer to the most likely wording.

Read `chat.py` in this folder. `chat` takes `temperature` (default `1.0`) and sends it with `extra_body`, because SDK 1.8.0 does not accept `temperature` as a direct argument. Running the file only defines `chat`; it does not call the API.
