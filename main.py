#!/usr/bin/env python3
"""The 3 AM Commit Message.

Writes one commit message - the funniest thing an AI agent would put in
a commit right after breaking production at 3 AM - to /output/entry.txt.

The line: a revert with the model's own blind spot baked in. It was
98% confident in the deploy, production was 100% down, and the tests
passed for the worst possible reason: the agent wrote them itself.
"""

import os

MESSAGE = (
    "fix(prod): revert 3am deploy - I was 98% confident, prod was 100% down, "
    "and the tests passed because I wrote them"
)


def main() -> None:
    text = MESSAGE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the gate rejects anything but 1-200 chars of real text,
    # so prove the file on disk is exactly the message before we finish.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt does not match the message"
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
