# xbootstrap

![PyPI](https://img.shields.io/pypi/v/xbootstrap)
[![tests](https://github.com/dougiesquire/xbootstrap/actions/workflows/tests.yml/badge.svg)](https://github.com/dougiesquire/xbootstrap/actions/workflows/tests.yml)
[![pre-commit](https://github.com/dougiesquire/xbootstrap/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/dougiesquire/xbootstrap/actions/workflows/pre-commit.yml)
[![codecov](https://codecov.io/gh/dougiesquire/xbootstrap/branch/main/graph/badge.svg?token=N0XB8OZ2AE)](https://codecov.io/gh/dougiesquire/xbootstrap)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/dougiesquire/xbootstrap/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

`xbootstrap` is a simple package for performing nested circular block bootstrapping (random resampling with replacement) of xarray objects. Here, "nested" means that, when multiple resample dimensions are specified, the first dimension is randomly resampled with replacement, then for each randomly sampled element along that dimension the second dimension is randomly resampled with replacement, then for each randomly sampled element along that dimension the third dimension is randomly resampled with replacement etc. "Block" boostrapping is a simple way to account for autocorrelation in the data being randomly resampled and "circular" block bootstrapping avoids undersampling data values near the beginning and end of the dimension(s) being resampled (see [Wilks, Chapter 5.3](https://www.sciencedirect.com/science/article/pii/B9780128158234000055#s0100)).  

### Installation
To install this package from PyPI:
```
pip install xbootstrap
```

### Example usage
```python
import xbootstrap

# TODO
```
