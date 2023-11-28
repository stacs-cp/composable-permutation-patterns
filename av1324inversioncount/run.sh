
mkdir -p params
mkdir -p outputs

# this is made for a large machine!
# 256 cores, 1TB memory

# populate conjure-output by running a small instance
rm -f conjure-output/model000001-minionseq-04-004.solutions.json.gz
python3 run.py minionseq 04 004

# generates commands-par.txt
python3 gen_commands.py

parallel --no-notice -j1 \
    --joblog outputs/gnuparallel-joblog-par.tsv \
    --results outputs/gnuparallel-results-par \
    --eta \
    :::: commands-par.txt
cat outputs/gnuparallel-joblog-par.tsv | cut -f 1,4- > outputs/gnuparallel-joblog-par.tsv.tmp ; mv outputs/gnuparallel-joblog-par.tsv.tmp outputs/gnuparallel-joblog-par.tsv

# collect results
python3 collect_results.py
