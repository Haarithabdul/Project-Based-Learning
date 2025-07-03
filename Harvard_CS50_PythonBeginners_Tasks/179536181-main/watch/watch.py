import re

def main():
    result = parse(input("HTML: "))
    print(result)

def parse(s):
    pattern = r"src=\"http(s)?://(www.)?youtube.com/embed/([\w-]+)\""
    if url := re.search(pattern, s):
        return f"https://youtu.be/{url.group(3)}"
    else:
        return None

if __name__ == "__main__":
    main()
