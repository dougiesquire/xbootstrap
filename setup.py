from setuptools import find_packages, setup
import versioneer

setup(
    name="xbootstrap",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Dougie Squire",
    url="https://github.com/dougiesquire/xbootstrap",
    description="Nested circular block bootstrap resampling for xarray objects",
    long_description="xbootstrap is a simple package for performing nested circular block bootstrapping (random resampling with replacement) of xarray objects. Here, 'nested' means that, when multiple dimensions are specified, the first dimension is randomly resampled, then for each randomly sampled element along that dimension the second dimension is randomly resampled, then for each randomly sampled element along that dimension the third dimension is randomly resampled etc. 'Block' boostrapping is a simple way to account for autocorrelation in the data being randomly resampled and 'circular' block bootstrapping avoids undersampling data values near the beginning and end of the dimension(s) being resampled",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "xarray",
        "numpy",
    ],
)
