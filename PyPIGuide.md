# Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Configuration: directory setup](#configuration-directory-setup)
- [Uploading to PyPI](#uploading-to-pypi)

# Resources & References
- The official [Python Packaging User Guide](https://packaging.python.org/)
    - Tutorial on [Packaging and Distributing Projects](https://packaging.python.org/tutorials/distributing-packages/)
    - [Guides](https://packaging.python.org/guides/), which are focused on accomplishing a specific task
        - Using [TestPyPI](https://packaging.python.org/guides/using-testpypi/)
- `Setuptools` docs: [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
- Blogs:
    - effbot.org: [How does the Python version numbering scheme work?](http://effbot.org/pyfaq/how-does-the-python-version-numbering-scheme-work.htm)
    - Deciphering Glyph: [Python Packaging Is Good Now](https://glyph.twistedmatrix.com/2016/08/python-packaging.html) [Aug 2016]
    - Hynek Schlawack: [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) [Jul 2013]
    - Peter Downs: [How to submit a package to PyPI](http://peterdowns.com/posts/first-time-with-pypi.html)
    - Tom Christie: [Uploading to PyPI](https://tom-christie.github.io/articles/pypi/) [Jun 2014]
    - Ewen Cheslack-Postava: [A Brief Introduction to Packaging Python](https://ewencp.org/blog/a-brief-introduction-to-packaging-python/) [Jun 2013]
- Relevant PEPs:
    - [PEP 440](https://www.python.org/dev/peps/pep-0440/): Version Identification and Dependency Specification
    - [PEP 427](https://www.python.org/dev/peps/pep-0427/): The Wheel Binary Package Format 1.0

# Background
Beginning (particularly self-taught) programmers often undergo something resembling this evolution:
1. Scripting directly within the interpreter.
2. Saving scripts to .py files or just .txt files without formally using them as modules.
3. Writing standalone .py modules.
4. Structuring packages to be used on the local machine (placing them somewhere in PATH, with something resembling the structure below):

```
packagename
|-- __init__.py
|-- modeule1.py
|-- folder1
    |-- __init__.py
    |-- module2.py
```
5. Uploading the aforementioned packages to GitHub.

...with the final (desired) step to be able to allow others to simply `pip install` the package rather than needing to download the GitHub repository itself.  **This guide is oriented towards people who have followed some form of the progression above, but should also be generalizable, to an extent.**

# Overview
Python's packaging ecosystem, while having recently underwent major improvements, has been condemned over the years as overly complicated and disorganized.  One result of the recent transformation is that many links are outdated; as a result, it is smart to be wary of the publish date and have a higher bar for implementing suggestions from a single article.  For instance, `disutils` is largely unused now.

## What is a _distribution package_?
A [distribution package](https://packaging.python.org/glossary/#term-distribution-package), or just distribution, is different from a "simple" package that just contains modules or other packages.  A distribution package is

> A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. The archive file is what an end-user will download from the internet and install.

# Prerequisites
- [Register](https://pypi.python.org/pypi?%3Aaction=register_form) on PyPI
- [Register](https://testpypi.python.org/pypi?%3Aaction=register_form) on TestPyPI
- Make sure you have the following installed:
    - `setuptools`
    - `twine`

You can confirm with `conda list` at the command line.

# Configuration: directory setup

## Files

File | Use | Note(s)
------------ | ------------- | -------------
`setup.py` | The primary feature of setup.py is that it contains a global `setup()` function. The keyword arguments to this function are how specific details of your project are defined. The most relevant arguments are explained in the section [below](#setup-arguments). | TODO
`setup.cfg` | TODO | TODO
`README.rst/.md` | TODO | TODO
`MANIFEST.in` | TODO | TODO
`LICENSE` | TODO | TODO

## Example directory structure

```
pyfinance                        # the "project folder"
|-- LICENSE                      # <-- *this level is the directory root!*
|-- MANIFEST.in                  # <--
|-- README.rst                   # or: README.md`
|-- setup.py
|-- pyfinance                    # this is the package folder itself
    |-- __init__.py
    |-- datasets.py
    |-- ols.py
    |-- options.py
    |-- general.py
    |-- returns.py
    |-- utils.py

```

## `setup()` arguments

### `name`

### `version`

### `description`

### `url`

### `author`

### `license`

### `classifiers`

### `keywords`

### `packages`

### `install_requires`

### `python_requires`

### `package_data`

### `data_files`

### `scripts`

### `entry_points`

# Uploading to PyPI
