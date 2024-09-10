## Create environment
```bash
conda create --prefix ./env python=3.10
source activate
conda activate ./env
conda env list
```
## Create file
```bash
touch requirements.txt
touch .gitignore
touch dvc.yaml
touch params.yaml
touch setup.py
OR
touch requirements.txt .gitignore dvc.yaml params.yaml setup.py

mkdir -p config src/utils
touch config/config.yaml config/secrets.yaml

touch src/__init__.py src/utils/__init__.py
touch src/stage_01_load_save.py src/utils/all_utils.py

touch src/stage_02_prepare_base_model.py
```
## Install Packags
```bash
pip install -r requirements.txt
pip list
- install src
pip install -e .
```
## Initialize tracker
```bash
git init
dvc init
```
## Check install package
```bash
pip freeze > requirements.txt
```

