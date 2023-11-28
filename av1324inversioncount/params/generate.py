import os
from math import comb

def createpairs(inversionrange,minlength, maxlength):
    resarr = []
    for i in range(inversionrange[0],inversionrange[1]+1):
        for j in range(minlength,maxlength+1):
            resarr.append([i,j])
    
    return resarr

def createfile(invs,minlength,maxlength):
    a = createpairs(invs,minlength,maxlength)
    paramstring = []
    for p in a:
        i = p[0]
        l = p[1]
        name = 'av1324-inv{:06d}-len{:06d}'.format(i,l)
        # name = f'av1324-inv{i}-len{l}'
        paramstring.append(name)
        f = open(name+".param", "w")
        f.write("letting turnedOn be true \nletting classic_avoidance be {sequence(1,3,2,4)}\n")
        f.write(f'letting nInversions be {i}\n')
        f.write(f'letting length be {l}')
        f.close()
    return paramstring

def run(invs, minlen, maxlen, minionpar, nbcsat):
    if invs[1]-invs[0]==0:
        invs = range(invs[1],invs[1]+1)
    if minlen <= 4:
        print("Length needs to be 5 or more")
    else:
        pstring = createfile(invs,minlen,maxlen)
        for param in pstring:
            if minionpar[0]:
                print(f'conjure solve -v ../av1324invcount.essence {param}.param --number-of-solutions=all --solutions-in-one-file --output-format=json --solver-options \"-parallel -cores {minionpar[1]}\" --savilerow-options \"-preprocess SSACBounds\" ')
                os.system(f'conjure solve -v ../av1324invcount.essence {param}.param --number-of-solutions=all --solutions-in-one-file --output-format=json --solver-options \"-parallel -cores {minionpar[1]}\" --savilerow-options \"-preprocess SSACBounds\" ')
            elif nbcsat:
                print(f'conjure solve ../av1324invcount.essence {param}.param --number-of-solutions=all --solutions-in-one-file --output-format=json --solver=nbc_minisat_all')
                os.system(f'conjure solve ../av1324invcount.essence {param}.param --number-of-solutions=all --solutions-in-one-file --output-format=json --solver=nbc_minisat_all')
            else:
                print(f'conjure solve ../av1324invcount.essence {param}.param --number-of-solutions=all --solutions-in-one-file --output-format=json')
                os.system(f'conjure solve ../av1324invcount.essence {param}.param --number-of-solutions=all --solutions-in-one-file --output-format=json')
            # print(f'{param}')
            # os.system(f'grep -c letting conjure-output/model000001-{param}.solutions')
            # f = open(f'{param}.sol', "w")
            # stream = os.popen(f'grep -c letting conjure-output/model000001-{param}.solutions')
            # output = stream.read()
            # f.write(output)
            # f.close()
            
def combinesols(invs):
    for i in range(invs[0],invs[1]+1):
        stream = os.popen('grep -ch letting conjure-output/model000001-av1324-inv{:06d}-*.solutions > inv{:06d}.seq'.format(i,i))
