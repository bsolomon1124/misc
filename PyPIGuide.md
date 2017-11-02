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
Beginner (particularly self-taught) Python programmers often undergo something resembling this evolution:
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
    |-- module3.py
```
5. Uploading the aforementioned packages to GitHub.

...with the final (desired) step to be able to allow others to simply `pip install` the package rather than needing to download the GitHub repository itself.  **This guide is oriented towards people who have followed some form of the progression above, but should also be generalizable, to an extent.**

# Overview
A **packaging index** (for example, PyPI) is a repository of distributions with a web interface to automate package discovery and consumption.

Python's packaging ecosystem, while having recently underwent major improvements, has been condemned over the years as overly complicated and disorganized.  One result of the recent transformation is that many links are outdated; as a result, it is smart to be wary of the publish date and have a higher bar for implementing suggestions from a single article.  For instance, `disutils` is largely unused now.

## What is a _distribution package_?
A [distribution package](https://packaging.python.org/glossary/#term-distribution-package), or just distribution, is different from a "simple" package that just contains modules or other packages.  A distribution package is

> A versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a Release. The archive file is what an end-user will download from the internet and install.

Note that a _project_ is also defined separately.  A project is

> A library, framework, script, plugin, application, or collection of data or other resources, or some combination thereof that is intended to be packaged into a Distribution.  [However,] most projects create Distributions using `distutils` or `setuptools`.

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
`setup.py` | The project specification file for both `setuptools` and `disutils`.  The primary feature of `setup.py` is that it contains a global `setup()` function. The keyword arguments to this function are how specific details of your project are defined. | The most relevant arguments are explained in the section [below](#setup-arguments).
`setup.cfg` | An ini file that contains option defaults for `setup.py` commands. | Not needed in all cases.
`README.rst/.md` | Covers the goal of the project. | Common extensions are `.rst` (reStructuredText) and `.md` (Markdown).  The former can be read by PyPI without additional specification, while the latter requires additional setup to be rendered correctly by PyPI.
`MANIFEST.in` | Needed in certain cases where you need to package additional files that are not automatically included in a source distribution. | To see a list of what’s included by default, see the [Specifying the files to distribute](https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute) section from the `distutils` documentation.
`LICENSE` | Details the terms of distribution. In many jurisdictions, packages without an explicit license can not be legally used or distributed by anyone other than the copyright holder. | GitHub: [Choose an open source license](https://choosealicense.com/)

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

## `setup()` keyword arguments
An example `setup.py`: [pypa/sampleproject/setup.py](https://github.com/pypa/sampleproject/blob/master/setup.py).

Argument | Use | Note(s)
------------ | ------------- | -------------
`name` | The name of your project, determining how your project is listed on PyPI. | [PEP 508](https://www.python.org/dev/peps/pep-0508/) discusses valid project names.
`version` | This is the current version of your project, allowing your users to determine whether or not they have the latest version, and to indicate which specific versions they’ve tested their own software against. | See [choosing a versioning scheme](https://packaging.python.org/tutorials/distributing-packages/#choosing-a-versioning-scheme) and [PEP 440](https://www.python.org/dev/peps/pep-0440/).
`description` | -- | Displayed on PyPI.
`long_description` | -- | Displayed on PyPI.
`url` | A homepage URL for your project. | I.e. `url='https://github.com/pypa/sampleproject'`.
`author` | -- | I.e. `author='The Python Packaging Authority'`.
`author_email` | -- | I.e. `author_email='pypa-dev@googlegroups.com'`.
`license` | Provide the **type** of license you are using. | Note that this doesn't need to refer to the license file itself.
`classifiers` | Provide a list of classifiers that categorize your project.  **These must fall under a prespecified set of classifiers.** This information is used for searching and browing projects on PyPI. | [Full listing of classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers).
`keywords` | List keywords that describe your project. | A single space-separated string i.e. `keywords='sample setuptools development'`.
`packages` | It’s required to list the packages to be included in your project. Although they can be listed manually, `setuptools.find_packages` finds them automatically. Use the `exclude` keyword argument to omit packages that are not intended to be released and installed. | A common specification is `packages=find_packages(exclude=['contrib', 'docs', 'tests*'])`.
`install_requires` | Specify what dependencies a project minimally needs to run. | **When the project is installed by pip, this is the specification that is used to install its dependencies.**
`python_requires` | If your project only runs on certain Python versions, setting the `python_requires` argument to the appropriate [PEP 440 version specifier](https://www.python.org/dev/peps/pep-0440/#version-specifiers) string will prevent pip from installing the project on other Python versions. | Some [examples](https://packaging.python.org/tutorials/distributing-packages/#python-requires) from the docs.

Note that the above list is not exhaustive.  Other kwargs include `scripts`, `data_files`, and `package_data`.

# Uploading to PyPI
[unfinished] - see links below.

_Official docs:_
- [Packaging your project](https://packaging.python.org/tutorials/distributing-packages/#packaging-your-project)
- [Uploading your project to PyPI](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)

Note that the above are two separate steps.  The first consists of creating your distribution, mainly via putting a new directory `dist/` under your project’s root directory.  The project is actually uploaded in the second step.

You **invoke setup from the command line** to _produce eggs, upload to PyPI, and automatically include all packages in the directory where the setup.py lives_

> _Note_: Most examples will shown snippets such as
> 
> ```
> python setup.py sdist
> ```
> 
> Keep in mind that you need to reference the full `setup.py` path if `setup` isn't in your `cd`.  For example,
> 
> ```python C:/Users/Brad/anaconda3/pyfinance/setup.py --help-commands```
>

## Using TestPyPI
_Official guide: [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)_

Before releasing on the main PyPI repo, you might prefer training with the PyPI test site, which is cleaned on a semi regular basis.

# TODO
- [Binary distributions](https://packaging.python.org/glossary/#term-binary-distribution)
