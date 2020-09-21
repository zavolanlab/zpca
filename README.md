# zpca

PCA analysis

# Installation

```bash
# clone the repo
git clone https://github.com/zavolanlab/pca.git
# create a virtual environment
python3 -m venv venv
# activate the virtual environment
source venv/bin/activate
# install zgtf scripts
pip install .
```

# Run

```bash
usage: zpca [-h] --tpm FILE --out FILE [-v]

Perform PCA based on a table (rows are genes/transcripts, columns are samples).

optional arguments:
  -h, --help     show this help message and exit
  --tpm FILE     TPM table (tsv)
  --out FILE     Output directory
  -v, --verbose  Verbose
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