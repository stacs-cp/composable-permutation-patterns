
import os
import json

allInfo = []

for dirpath, dirnames, filenames in os.walk("conjure-output"):
    for infofile in sorted(filenames):
        if infofile.endswith(".eprime-info"):
            [_, solver, length, nbInv] = infofile.split(".")[0].split("-")
            info = {}
            try:
                with open(f'{dirpath}/{infofile}', "r") as f:
                    for l in f:
                        [k, v] = l.split(":")
                        info[k.strip()] = v.strip()

                try:
                    info["TotalTime"] = str(
                        float(info["SolverTotalTime"]) + float(info["SavileRowTotalTime"]))
                except:
                    info["TotalTime"] = "NA"
            except FileNotFoundError:
                pass
            allInfo.append(([solver, length, nbInv], info))

maxLength = 0
maxNbInv = 0
justTheCounts = {}

headers = set()
for _, info in allInfo:
    headers = headers.union(info.keys())
headers = sorted(list(headers))

with open("outputs/info.csv", "w") as out:
    heading = ", ".join(["solver", "length", "nbInv"] + headers)
    print(heading, file=out)
    for [solver, length, nbInv], info in allInfo:
        maxLength = max(maxLength, int(length))
        maxNbInv = max(maxNbInv, int(nbInv))
        if solver == "minionpar":
            justTheCounts[int(length), int(nbInv)] = info["SolverSolutionsFound"]
        print(", ".join([solver, length, nbInv] + [info[k] if k in info.keys() else "NA"
              for k in headers]), file=out)

with open("outputs/table2.csv", "w") as out:
    outputLines = []
    outputLines.append(", " + ", ".join([str(i) for i in range(0, maxNbInv+1)]))
    for l in range(1, maxLength + 1):
        outputLine = []
        outputLine.append(str(l))
        for i in range(0, maxNbInv+1):
            try:
                outputLine.append(justTheCounts[l,i])
            except:
                outputLine.append("")
        outputLines.append(", ".join(outputLine))
    print("\n".join(outputLines), file=out)


