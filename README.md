# xbootstrap

[![PyPI](https://img.shields.io/pypi/v/xbootstrap)](https://pypi.org/project/xbootstrap)
[![tests](https://github.com/dougiesquire/xbootstrap/actions/workflows/tests.yml/badge.svg)](https://github.com/dougiesquire/xbootstrap/actions/workflows/tests.yml)
[![pre-commit](https://github.com/dougiesquire/xbootstrap/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/dougiesquire/xbootstrap/actions/workflows/pre-commit.yml)
[![codecov](https://codecov.io/gh/dougiesquire/xbootstrap/branch/main/graph/badge.svg?token=N0XB8OZ2AE)](https://codecov.io/gh/dougiesquire/xbootstrap)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/dougiesquire/xbootstrap/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

`xbootstrap` is a simple package for performing **nested circular block bootstrapping** (random resampling with replacement) of xarray objects. Here, "nested" means that, when multiple dimensions are specified, the first dimension is randomly resampled, then for each randomly sampled element along that dimension the second dimension is randomly resampled, then for each randomly sampled element along that dimension the third dimension is randomly resampled etc. "Block" boostrapping is a simple way to account for autocorrelation in the data being randomly resampled and "circular" block bootstrapping avoids undersampling data values near the beginning and end of the dimension(s) being resampled (see [Wilks, Chapter 5.3](https://www.sciencedirect.com/science/article/pii/B9780128158234000055#s0100)).  

### Installation
To install this package from PyPI:
```
pip install xbootstrap
```

### Example usage
`xbootstrap` currently comprises a single function called `block_bootstrap` that can be used as follows:
```python
import numpy as np
import xarray as xr
from xbootstrap import block_bootstrap

# Generate some example data
n_time = 100
n_ensemble = 10
ds1 = xr.DataArray(
    np.random.random((n_time, n_ensemble)),
    coords={"time": range(n_time), "ensemble": range(n_ensemble)},
)
ds2 = xr.DataArray(
    np.random.random((n_time, n_ensemble)),
    coords={"time": range(n_time), "ensemble": range(n_ensemble)},
)
ds3 = xr.DataArray(np.random.random((n_time)), coords={"time": range(n_time)})

# Create 1000 bootstrapped resamples of ds1, ds2 and ds3 using a
# blocksize of 5 for the time dimension and 1 for the ensemble
# dimension, and only bootstrapping the time dimension for ds2
ds1_bs, ds2_bs, ds3_bs = block_bootstrap(
    ds1,
    ds2,
    ds3,
    blocks={"time": 5, "ensemble": 1},
    n_iteration=1000,
    exclude_dims=[[], ["ensemble"], []],
)
```
`block_bootstrap` also operates lazily with dask-backed xarray objects, but this requires `dask` to be installed:
```python
ds1_bs, ds2_bs, ds3_bs = block_bootstrap(
    ds1.chunk(),
    ds2.chunk(),
    ds3.chunk(),
    blocks={"time": 5, "ensemble": 1},
    n_iteration=10,
    exclude_dims=[[], ["ensemble"], []],
)
```

### Contributing
Contributions are very welcome, particularly in the form of reporting bugs and writing tests. Please open an issue and check out the [contributor guide](CONTRIBUTING.md).
