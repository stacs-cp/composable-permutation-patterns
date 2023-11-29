Supplementary files for paper entitled: "Composable Constraint Models for Permutation Enumeration" by Ruth Hoffmann, Özgür Akgün and Chris Jefferson

- **CPModelsForPP.ipynb** -- contains the interactive Jupyter notebook which will allow running the different model fragments (in the browser using Google colab, or locally if you want to install [Conjure](https://conjure-cp.github.io/))
- **models** and **params** -- contain standalone versions of the models and some representative parameter files. There can be used to run Conjure on the command line.
- **av1324inversioncount** -- raw results of out experiment where we enumerate the permutations that avoid $1324$ classically and for a given fixed number of inversions. `run.sh` in this directory can be used to rerun the entire experiment (beware it will try to use 250 cores, this can be changed in the `run.py` file, on [line 28](https://github.com/stacs-cp/composable-permutation-patterns/blob/1fec32c9b8f60de7483837f4c2e6014a4427be04/av1324inversioncount/run.py#L28).

