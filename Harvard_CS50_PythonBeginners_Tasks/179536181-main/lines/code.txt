def convert(text):
    text1 = text.replace(":)", '🙂')
    text2 = text1.replace(":(", '🙁')
    return text2

def main():
    text= input()
    NewText = convert(text)
    print(NewText)

main()
