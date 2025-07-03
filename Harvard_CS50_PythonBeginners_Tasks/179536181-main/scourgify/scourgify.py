import sys
import csv
import pandas as pd

def main():
    inp = sys.argv

    if len(inp) > 3:
        sys.exit("too many command line arguments")
    elif len(inp) < 3:
        sys.exit("too few command line arguments")
    else:
        oldFileName = inp[1].split(".")
        newFileName = inp[2].split(".")
        if oldFileName[1] != "csv":
            sys.exit("not a csv file")
        elif newFileName[1] != "csv":
            sys.exit("not a csv file")
        else:
            clean(inp[1], inp[2])

def clean(before, after):
    data = []
    with open(before, "r") as oldFile:
        oldFile = csv.reader(oldFile)
        for row in oldFile:
            data.append(row)

    with open(after, "w") as newFile:
        newWrite = csv.writer(newFile)
        newWrite.writerows(data)

    df = pd.read_csv(before)
    df["name"] = df["name"].str.split(",")
    df["name"] = df["name"].str[::-1]
    newName = df["name"].str.join(" ")

    df = pd.read_csv(after)
    df["name"] = newName
    df.to_csv(after, index=False)



if __name__ == "__main__":
    main()
