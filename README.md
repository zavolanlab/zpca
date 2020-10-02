# zpca

PCA analysis

# Installation

```bash
# clone the repo
git clone https://github.com/zavolanlab/zpca.git
# create a virtual environment
python3 -m venv venv
# activate the virtual environment
source venv/bin/activate
# install zpca scripts
pip install .
```

# Run

```bash
zpca --help
```

```
usage: zpca [-h] --counts FILE --lengths FILE [--pseudocount PSEUDOCOUNT]
            [--tpm-filter TPM_FILTER] [--filter-not-expressed] --out DIRECTORY
            [-v]

Perform PCA based on an expression matrix (rows are genes/transcripts, columns are samples).

optional arguments:
  -h, --help            show this help message and exit
  --counts FILE         Counts table (tsv). The first column should contain the gene/transcript id. The other columns should contain the counts for each sample.
  --lengths FILE        Table of feature lengths (tsv). The first column should contain the gene/transcript id. The second column should contain the corresponding lengths
  --pseudocount PSEUDOCOUNT
                        Pseudocount to add in the count table. Default: 1
  --tpm-filter TPM_FILTER
                        Filter genes/transcripts with mean expression less than the provided filter. Default: 0
  --filter-not-expressed
                        Filter not expressed genes/transcripts (0 counts for all samples).
  --out DIRECTORY       Output directory
  ```

  # Docker 

Pull image
```bash
docker pull zavolab/zpca
```

Run
```bash
docker run -it zavolab/zpca zpca --help
```

# Singularity

Pull image
```bash
singularity pull docker://zavolab/zpca
```

Run
```bash
singularity exec zpca_latest.sif zpca --help
```