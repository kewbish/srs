with open("passed_results.txt", "r") as file:
    file = file.read().splitlines()
    aks = [str(f) for f in eval(file[0])]
    aks = [aks[i : i + 1024] for i in range(0, len(aks), 1024)]
    aks_time = file[1]
    euler = [str(f) for f in eval(file[2])]
    euler_time = file[3]
    fermat = [str(f) for f in eval(file[4])]
    fermat_time = file[5]
    mr = [str(f) for f in eval(file[6])]
    mr_time = file[7]

with open("passed_pprimes.csv", "w") as file:
    for a in aks:
        file.write(",".join(a) + "\n")
    file.write(f"{aks_time}\n")
    file.write(",".join(euler) + f",{euler_time}\n")
    file.write(",".join(fermat) + f",{fermat_time}\n")
    file.write(",".join(mr) + f",{mr_time}\n")
