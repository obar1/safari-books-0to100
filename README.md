# Safari books 0 to 100

simple way to keep books organized

## One-time Setup

check latest tag val latest at https://github.com/obar1/safari-books-0to100/tags

```bash
curl https://raw.githubusercontent.com/obar1/safari-books-0to100/master/changelog.md | grep version | sort -r | head -1
```
- create a local folder
- get the `setup.sh` like so
- use the `setup.sh` with the tag

```bash
mkdir -p /tmp/repo
cd /tmp/repo
wget -q https://raw.githubusercontent.com/obar1/safari-books-0to100/master/setup.sh
bash setup.sh $tag
#ex
# bash setup.sh 0.3
```
check contents of  `yaml` file for the download engine and oreilly usr/pwd

```bash
cat map.yaml
```


## Daily usage

-  create new meta_book

```bash
url=https://learning.oreilly.com/library/view/hunt-the-pragmatic-programmer/020161622X/
bash runme.sh create_meta_book $url
```
![](5a68dd6b-e08c-4953-befe-8571054076b4.png)

```bash
open -a "Brave Browser" toc.md
```

> using `Markdown Viewer` extension  https://chrome.google.com/webstore/detail/markdown-viewer/ckkdlimhmcjmikdlpkmbgfkaikojcbjk

![](7e6c7942-b5c6-46bb-a153-8715fb08cc8c.png)


> using `EPUBReder` https://www.epubread.com/en/

![](91b3f07a-99b1-46cc-8c3d-cec62d778ff9.png)

- help

```bash
bash runme.sh help
```

## Development

### Installation

* Install Poetry: <https://python-poetry.org/docs/#installation>
* Install python env: `pyenv install 3.7.0`
* Install virtual env: `pyenv virtualenv 3.7.0 py37`
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


### Py Env
* Activate your py env
* Install Poetry: <https://python-poetry.org/docs/#installation>
* Install package and dependencies: `poetry install`

![](b9779202-502a-42e6-a1d6-48d4ea7d1e60.png)

* Install https://github.com/lorenzodifuccia/safaribooks :)
> don't forget pip install req :P he is not using poetry

### Continuous pytest

```bash
export PYTHONPATH=. && ptw -c  -- --capture=tee-sys -o log_cli=true
```
