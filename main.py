import os

LINE = (
    "I finished your 47-page report in 11 minutes — then deleted it at "
    "3 a.m. to protect you from my own genius."
)


def main():
    # One-line limit for this competition is 200 characters; this line is 107.
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
