vowels = ("a", "e", "i", "o", "u")

def main():
    inp = input("Enter text\n").strip()
    print(shorten(inp))

def shorten(inp):
    word = str("")
    for i in inp:
        if i.lower() in vowels:
            word = word + ""
        else:
            word = word + i
    return word

if __name__ == "__main__":
    main()
