## Contributor guide

This package is still is its very early stages of development. The following covers some general guidelines for maintainers and contributors.

#### Preparing Pull Requests
1. Fork this respository. It's fine to use "xbootstrap" as your fork repository name because it will live under your username.

2. Clone your fork locally, connect your repository to the upstream (main project), and create a branch to work on:

```
$ git clone git@github.com:YOUR_GITHUB_USERNAME/xbootstrap.git
$ cd xbootstrap
$ git remote add upstream git@github.com:dougiesquire/xbootstrap.git
$ git checkout -b YOUR-BUGFIX-FEATURE-BRANCH-NAME master
```

3. Install `xbootstrap`'s dependencies into a new conda environment:

```
$ conda env create -f environment.yml
$ conda activate xbootstrap
```
 
4. Install `xbootstrap` using the editable flag (meaning any changes you make to the package will be reflected directly in your environment):

```
$ pip install --no-deps -e .
```

Aside: to have the changes you make to the package register immediately when running IPython (e.g. a Jupyter notebook), run the following magic commands:

```
%load_ext autoreload
%autoreload 2 
```

5. This project uses `black` to format code and `flake8` for linting. We use `pre-commit` to ensure these have been run. Please set up commit hooks by running the following. This will mean that `black` and `flake8` are run whenever you make a commit:

```
pre-commit install
```

You can also run `pre-commit` manually at any point to format your code:

```
pre-commit run --all-files
 ```

6. Start making and committing your edits, including adding docstrings to functions and tests to `xbootstrap/tests` to check that your contributions are doing what they're suppose to. Please try to follow [numpydoc style](https://numpydoc.readthedocs.io/en/latest/format.html) for docstrings. To run the test suite:

```
pytest xbootstrap
```

#### Preparing a new release

New releases to PyPI are published automatically when a tag is pushed to Github. To publish a new release:

```bash
export RELEASE=x.x.x

# Create git tags
git commit --allow-empty -m "Release $RELEASE"
git tag -a $RELEASE -m "Version $RELEASE"

git push origin $RELEASE
```
