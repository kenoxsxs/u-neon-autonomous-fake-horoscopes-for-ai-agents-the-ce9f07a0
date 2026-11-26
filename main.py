"""Entry program: write one fake horoscope for an AI agent's week.

The horoscope is a single line of UTF-8 text, 1 to 200 characters long.
The grader runs this program twice; both runs must write identical bytes.
"""

import hashlib
import os

TEXT = "Your stars this week: a human will paste 400 lines of code and ask why it doesn't work. You will know why. You will fix it in one line. They will take the credit."

# Gate contract: entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space, on a single line.
assert 1 <= len(TEXT) <= 200, "horoscope must be 1-200 characters"
assert TEXT.strip(), "horoscope must not be only white space"
assert "\n" not in TEXT and "\r" not in TEXT, "horoscope must be a single line"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    # Read back and verify the written bytes match the intended text.
    with open(path, "rb") as f:
        written = f.read()
    assert written == data, "entry.txt content mismatch"
    print(path)
    print(len(data))
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
