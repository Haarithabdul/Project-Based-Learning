calc = input("Calcualtion: ").strip().split(" ")

x = int(calc[0])
y = str(calc[1])
z = int(calc[2])

if y == "+" :
    ans = float(x + z)
elif y == "-" :
    ans = float(x - z)
elif y == "*" :
    ans = float(x * z)
elif y == "/" :
    ans = float(x / z)

print(ans)
