import math
import os

# Solvers:
# - minionseq
# - minionpar (this is the one we use)
# - nbcsat

# Length:
# - 1 to n

# Number of inversions:
# - 0 .. comb(length,2)

with open("commands-par.txt", "w") as out:
    for solver in ["minionpar"]:                                    # other solvers: ["minionseq", "nbcsat"]:

        # all nbInvs for lengths 1..16
        for length in range(1, 16+1):
            for nbInv in range(0, math.comb(length, 2) + 1):
                i = nbInv
                lengthPadded = str(length).zfill(2)
                nbInvPadded = str(i).zfill(3)
                infoFile = f'conjure-output/model000001-{solver}-{lengthPadded}-{nbInvPadded}.eprime-info'
                if not os.path.exists(infoFile):
                    print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}', file=out)
                    print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}')

        # also: 25x10
        for length in range(1, 25+1):
            for nbInv in range(0, min(10, math.comb(length, 2)) + 1):
                i = nbInv
                lengthPadded = str(length).zfill(2)
                nbInvPadded = str(i).zfill(3)
                infoFile = f'conjure-output/model000001-{solver}-{lengthPadded}-{nbInvPadded}.eprime-info'
                if not os.path.exists(infoFile):
                    print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}', file=out)
                    print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}')

        # also: 23x20
        for length in range(1, 23+1):
            for nbInv in range(0, min(20, math.comb(length, 2)) + 1):
                i = nbInv
                lengthPadded = str(length).zfill(2)
                nbInvPadded = str(i).zfill(3)
                infoFile = f'conjure-output/model000001-{solver}-{lengthPadded}-{nbInvPadded}.eprime-info'
                if not os.path.exists(infoFile):
                    print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}', file=out)
                    print(f'python3 run.py {solver} {lengthPadded} {nbInvPadded}')
