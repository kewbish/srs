from numpy import array
from sys import argv

if len(argv) != 2:
    exit(1)
else:
    path = f"../results/{argv[1]}_results.txt"

with open(path, "r") as file:
    file = file.read().split("\n\n")
    file = [f.split("\n") for f in file]
    file[0].insert(0, "")
    file = [f[1:] for f in file]
    file = file[:-1]

for chunk in file:
    args = eval(chunk[0])
    arr = eval("".join([c.lstrip() for c in chunk[1:-3]]))
    average_pprimes = eval(chunk[-3])
    max_min = eval(chunk[-2])
    time = chunk[-1]

    if len(args) == 1:
        opath = f"{argv[1]}_arb.csv"
    elif len(args) == 2:
        if args[1] == "2":
            opath = f"{argv[1]}_2.csv"
        elif args[1] == "3":
            opath = f"{argv[1]}_3.csv"
        elif args[1] == "5":
            opath = f"{argv[1]}_5.csv"
    elif len(args) == 3:
        if "2" in args and "3" in args:
            opath = f"{argv[1]}_2_3.csv"
        elif "3" in args and "5" in args:
            opath = f"{argv[1]}_3_5.csv"
        elif "2" in args and "5" in args:
            opath = f"{argv[1]}_2_5.csv"

    arr_string = ",".join(str(num) for num in arr)

    with open(opath, "a") as csv:
        csv.write(f"{arr_string},{average_pprimes},{max_min[0]},{max_min[1]},{time}\n")
