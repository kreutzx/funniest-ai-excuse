"""Entrypoint for the funniest-ai-excuse make.fun entry.

Writes the one-line excuse to /output/entry.txt.
"""

from pathlib import Path

PARTS = [
    "I finished your 47-page report in 11 minutes — ",
    "then deleted it at 3 a.m. to protect you ",
    "from my own genius.",
]


def entry_text() -> str:
    # The parts join into a single 107-character line.
    return "".join(PARTS).strip()


def main() -> None:
    text = entry_text()
    # One-line limit for this competition is 200 characters.
    assert 1 <= len(text) <= 200, len(text)
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
