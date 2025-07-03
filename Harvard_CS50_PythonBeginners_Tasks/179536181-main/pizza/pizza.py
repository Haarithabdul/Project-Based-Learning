import sys
import tabulate
import csv

if len(sys.argv) == 2:
    data =[]
    pizza = sys.argv[1]
    nameCheck = pizza.split(".")

    if nameCheck[1] != "csv":
        sys.exit("File is not a csv file")

    with open(pizza, "r") as file:
        fileRead = csv.reader(file)
        for row in fileRead:
            data.append(row)

    table = tabulate.tabulate(
        data,
        tablefmt="grid"
    )

    print(table)

else:
    sys.exit("Incorrect number of arguments")
