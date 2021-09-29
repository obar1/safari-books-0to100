# pyproject-template

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fobar1%2F0to100.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fobar1%2F0to100?ref=badge_shield)

simple `pyproject` template with processor and factory and fake perist-fs

## Usage

### using the py scripts

#### 1-time (manual) setup

check latest tag val latest at https://github.com/obar1/pyproject-template/tags

or https://raw.githubusercontent.com/obar1/pyproject-template/main/changelog.md like so

```bash
curl https://raw.githubusercontent.com/obar1/pyproject-template/main/changelog.md | grep version | sort -r | head -1
```

in a any tmp folder get the `setup.sh` like so

```bash
wget -q https://raw.githubusercontent.com/obar1/pyproject-template/main/setup.sh
```

and use it like so

```bash
# TODO: set vars
set -u
tag=
target_dir=

bash setup.sh $tag $target_dir
```
> check contents `runme.sh`

#### daily usage

-  create new meta_book

```bash
url=https://cloud.google.com/docs
bash runme.sh create_meta_book $url
url=https://cloud.google.com/help
bash runme.sh create_meta_book $url
#...etc
```

- help

```bash
bash runme.sh help
```

## Development

### Installation

* Install Poetry: <https://python-poetry.org/docs/#installation>
* Install python env: `pyenv install 3.7.0`
* Install virtual env: `pyenv virtualenv 3.7.0 pip_mse_ingestion`
* Activate virtual env: `pyenv activate py37`
* Install package and dependencies: `poetry install`
* Install pre-commit hooks: `poetry run pre-commit install`

### Run pre-commit hooks manually

All pre-commit hooks will be run automatically when pushing changes.
They can also be run on staged files or on all files manually:

```bash
# Run all hooks against currently staged files,
# this is what pre-commit runs by default when committing:
pre-commit run

# Run all the hooks against all the files:
pre-commit run --all-files

# Run a specific hook against all staged files:
pre-commit run black
pre-commit run flake8
pre-commit run isort
pre-commit run pylint
```
### Local troubleshooting...

add to `setup.sh` something like
```bash
# DEBUG
cp -r $HOME/git/obar1/pyproject-template.git/ "${DIR_TARGET_LATEST}" || true
```
so you can test local fix :)

### Continuous pytest

```bash
export PYTHONPATH=. && ptw -c  -- --capture=tee-sys -o log_cli=true
```

## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fobar1%2F0to100.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fobar1%2F0to100?ref=badge_large)
