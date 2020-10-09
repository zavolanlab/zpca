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

zpca consists of two tools:
- zpca-tpm
- zpca-counts

When you run
```bash
zpca-tpm --help
```

The following message should appear
```
usage: zpca-tpm [-h] --tpm FILE [--tpm-filter TPM_FILTER]
                [--tpm-pseudocount TPM_PSEUDOCOUNT] --out FILE [-v]

Perform PCA based on a TPM expression matrix (rows are genes/transcripts, columns are samples).

optional arguments:
  -h, --help            show this help message and exit
  --tpm FILE            TPM table (tsv).
  --tpm-filter TPM_FILTER
                        Filter genes/transcripts with mean expression less than the provided filter. Default: 1
  --tpm-pseudocount TPM_PSEUDOCOUNT
                        Pseudocount to add in the tpm table. Default: 1
  --out FILE            Output directory
  -v, --verbose         Verbose
  ```

When you run
```bash
zpca-counts --help
```

The following message should appear
```
usage: zpca-counts [-h] --counts FILE --lengths FILE
                   [--pseudocount PSEUDOCOUNT] [--filter-not-expressed] --out
                   DIRECTORY [-v]

Perform PCA based on an expression matrix (rows are genes/transcripts, columns are samples).

optional arguments:
  -h, --help            show this help message and exit
  --counts FILE         Counts table (tsv). The first column should contain the gene/transcript id. The other columns should contain the counts for each sample.
  --lengths FILE        Table of feature lengths (tsv). 
                        The file can have two types of formats.
                        First option: The first column should contain the gene/transcript id.
                        The second column should contain the corresponding lengths
                        Second option: The first column should contain the gene/transcript id.
                        The rest of the columns should contain the gene/transcript lengths for each of the samples
                        Note that the sample names should be the same the sample names of the counts.
  --pseudocount PSEUDOCOUNT
                        Pseudocount to add in the count table. Default: 1
  --filter-not-expressed
                        Filter not expressed genes/transcripts (0 counts for all samples).
  --out DIRECTORY       Output directory
  -v, --verbose         Verbose
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