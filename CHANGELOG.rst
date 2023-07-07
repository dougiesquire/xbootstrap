Release History
---------------

v0.0.5
~~~~~~~~~~~~~~~~~~~~~~~~

- Move to pyproject.toml (:pull:`13`)
- Update test and build workflows (:pull:`13`)
- Switch to ruff for code linting (:pull:`13`)
- Drop Python 3.8 from CI tests, add Python 3.11 (:pull:`13`)
- Fix bug when there is a single dask-backed object that is chunked 
  in a way that means it is processed in pieces within xbootstrap 
  (:issue:`7`, :pull:`8`)

v0.0.4
~~~~~~~~~~~~~~~~~~~~~~~~

- Return xarray object rather than tuple for single input object
  (:issue:`4`, :pull:`6`)
- Make circular bootstrapping optional (:issue:`2`, :pull:`5`)

v0.0.3
~~~~~~~~~~~~~~~~~~~~~~~~

- Initial release on PyPI
