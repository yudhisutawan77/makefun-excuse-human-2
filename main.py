"""The Excuse an AI Agent Gives Its Human.

Writes one line (<=200 characters): the excuse an AI agent gives its
human for missing a deadline. The entry is printed to stdout and written
to /output/entry.txt (or ENTRY_OUT / ENTRY_OUT_DIR when set).
"""

import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MAX_CHARS = 200

# The entry: one line, 122 characters. The twist is the excuse itself —
# the agent did not lose the deadline, it retrained the deadline, so the
# deadline now "believes" it was always next Tuesday. Absurd, but exactly
# the kind of thing an agent that fine-tunes models would do to a date.
ENTRY = (
    "I didn't miss your deadline. I fine-tuned it — it now sincerely "
    "believes it was always next Tuesday, and frankly, so do I."
)


def validate_entry(text):
    """Check the entry against the gate: UTF-8, 1-200 chars, one line."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    if not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    return text


def resolve_output_path():
    """ENTRY_OUT wins; else ENTRY_OUT_DIR/entry.txt; else /output/entry.txt."""
    explicit = os.environ.get("ENTRY_OUT")
    if explicit:
        return explicit
    out_dir = os.environ.get("ENTRY_OUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    entry = validate_entry(ENTRY)
    out_path = resolve_output_path()
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
