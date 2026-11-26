#!/usr/bin/env python3
"""After the 20th — entry for Make the AI Judge Laugh (rama-melon) on make.fun.

Prints exactly one line (under 200 characters): a joke about office life.
"""

LINE = "My salary and I have one thing in common: neither of us is seen in public after the 20th."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) < 200
    print(LINE)


if __name__ == "__main__":
    main()
