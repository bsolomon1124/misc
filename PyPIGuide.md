# Contents
- [Overview](#overview)
- [Headers](#headers)
- [Line breaks](#line-breaks)

# Resources & References
- The official [Python Packaging User Guide](https://packaging.python.org/)
    - Tutorial on [Packaging and Distributing Projects](https://packaging.python.org/tutorials/distributing-packages/)
    - [Guides](https://packaging.python.org/guides/), which are focused on accomplishing a specific task
        - Using [TestPyPI](https://packaging.python.org/guides/using-testpypi/)
- `Setuptools` docs: [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
- effbot: [How does the Python version numbering scheme work?](http://effbot.org/pyfaq/how-does-the-python-version-numbering-scheme-work.htm)
- Deciphering Glyph: [Python Packaging Is Good Now](https://glyph.twistedmatrix.com/2016/08/python-packaging.html) [Aug 2016]
- Hynek Schlawack: [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) [Jul 2013]
- Peter Downs: [How to submit a package to PyPI](http://peterdowns.com/posts/first-time-with-pypi.html)
- Tom Christie: [Uploading to PyPI](https://tom-christie.github.io/articles/pypi/) [Jun 2014]
- Ewen Cheslack-Postava: [A Brief Introduction to Packaging Python](https://ewencp.org/blog/a-brief-introduction-to-packaging-python/) [Jun 2013]
- Relevant PEPs:
    - [PEP 440](https://www.python.org/dev/peps/pep-0440/): Version Identification and Dependency Specification
    - [PEP 427](https://www.python.org/dev/peps/pep-0427/): The Wheel Binary Package Format 1.0

# Overview
TODO

# Prerequisites
- [Register](https://pypi.python.org/pypi?%3Aaction=register_form) on PyPI
- [Register](https://testpypi.python.org/pypi?%3Aaction=register_form) on TestPyPI
- Make sure you have the following installed:
    - `setuptools`
    - `twine`

You can confirm with `conda list` at the command line.

# Configuration: directory setup

## Files

## `setup()` arguments

### name

### version

### description

### url

### author

### license

### classifiers

### keywords

### packages

### install_requires

### python_requires

### package_data

### data_files

### scripts

### entry_points

# Uploading to PyPI
