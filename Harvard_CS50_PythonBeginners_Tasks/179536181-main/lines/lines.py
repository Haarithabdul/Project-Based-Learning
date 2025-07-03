import sys

if len(sys.argv) == 2:
    fileName = sys.argv[1]
    name, suffix = fileName.split(".")
    if suffix != "py":
        sys.exit(1)

    lines = open(fileName, "r")
    lines = lines.read()

    with open("code.txt", "w") as file:
        file.write(lines)

        lines = lines.split("\n")
        lineLength = len(lines)
        for line in lines:
            line = line.strip()
            if line == "":
                lineLength -= 1
            elif line[0] == "#":
                lineLength -= 1
        print(lineLength)

else:
    sys.exit("Incorrect input")
