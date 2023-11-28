
################################################################################
# create the param file

import sys, os

solver = sys.argv[1]
length = sys.argv[2]
nbInv = sys.argv[3]

paramfile = f'params/{solver}-{length}-{nbInv}.param'

with open(paramfile, "w") as out:
    print('letting turnedOn be true', file=out)
    print('letting classic_avoidance be {sequence(1,3,2,4)}', file=out)
    print(f'letting length be {length}', file=out)
    print(f'letting nInversions be {nbInv}', file=out)


################################################################################
# run conjure

if solver == 'minionseq':
    solvername = 'minion'
    opts = '--savilerow-options "-preprocess SSACBounds"'
elif solver == 'minionpar':
    solvername = 'minion'
    opts = '--savilerow-options "-preprocess SSACBounds" --solver-options "-parallel -cores 250 -findallsols -noprintsols"'
elif solver == 'nbcsat':
    solvername = 'nbc_minisat_all'
    opts = ''
else:
    sys.exit(f'Unexpected solver {solver}')

os.system(f'conjure solve av1324invcount.essence {paramfile} --number-of-solutions=all --solutions-in-one-file --output-format=json --solver={solvername} {opts}')


################################################################################
# cleanup

os.remove(f'conjure-output/model000001-{solver}-{length}-{nbInv}.eprime-param')
os.remove(f'conjure-output/model000001-{solver}-{length}-{nbInv}.eprime-minion')
try: os.remove(f'conjure-output/model000001-{solver}-{length}-{nbInv}.eprime-dimacs')
except: pass
try: os.remove(f'conjure-output/model000001-{solver}-{length}-{nbInv}.eprime-infor')
except: pass
try: os.remove(f'conjure-output/model000001-{solver}-{length}-{nbInv}.eprime-solutions')
except: pass
try: os.remove(f'conjure-output/model000001-{solver}-{length}-{nbInv}.solutions')
except: pass

# leave eprime-info
# leave solutions.json, compress
try: os.system(f'gzip conjure-output/model000001-{solver}-{length}-{nbInv}.solutions.json')
except: pass
