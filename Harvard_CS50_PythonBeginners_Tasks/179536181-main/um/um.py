import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    try:
        string = s.lower()

        pattern = r"\bum\b"

        if matches := re.findall(pattern, string):
            return len(matches)

    except Exception:
        sys.exit()

if __name__ == "__main__":
    main()
