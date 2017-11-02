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
    - [Command reference](https://setuptools.readthedocs.io/en/latest/setuptools.html#command-reference)
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
A **packaging index** is a repository of distributions with a web interface to automate package discovery and consumption.  The Python Package Index (PyPI) is a repository of software for the Python programming language.

Python's packaging ecosystem, while having recently underwent major improvements, has been condemned over the years as overly complicated and disorganized.  One result of the recent transformation is that many links are outdated; as a result, it is smart to be wary of the publish date and have a higher bar for implementing suggestions from a single article.  For instance, while `setuptools` and `disutils` are similar, `setuptools` is more modernized and fixes some of the problems with `distutils`.

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
`setup.cfg` | An ini file that contains option defaults for `setup.py` commands.  Note that metadata and other options normally supplied to `setup()` _can_ be specified here. | Not needed in all cases.  See setuptools docs: [Configuring `setup()` using setup.cfg files](https://setuptools.readthedocs.io/en/latest/setuptools.html#configuring-setup-using-setup-cfg-files).
`README.rst/.md` | Covers the goal of the project. | Common extensions are `.rst` (reStructuredText) and `.md` (Markdown).  The former can be rendered by PyPI to the project page without additional specification, while the latter requires additional setup to be rendered correctly by PyPI.
`MANIFEST.in` | Needed in certain cases where you need to package additional files that are not automatically included in a source distribution.  When `setup.py` builds your package, it includes `.py` files in your package folder by default. If you want any other files included in the `.tar.gz` file that gets created and uploaded to PyPI, you need to include those filenames in `MANIFEST.in`.  | To see a list of what’s included by default, see the [Specifying the files to distribute](https://docs.python.org/3.4/distutils/sourcedist.html#specifying-the-files-to-distribute) section from the `distutils` documentation.  See [here](https://tom-christie.github.io/articles/pypi/) for an example MANIFEST.
`LICENSE` | Details the terms of distribution. In many jurisdictions, packages without an explicit license can not be legally used or distributed by anyone other than the copyright holder. | GitHub: [Choose an open source license](https://choosealicense.com/)
`changelog.txt` | Helps users know what to expect from each relese. | An [example](https://github.com/cmcginty/PyWeather/blob/master/CHANGELOG.txt) from the `PyWeather` package.
`contributing.rst` | A guide on how users and viewers can contribute. | An [example](https://github.com/python-attrs/attrs/blob/master/CONTRIBUTING.rst) from `attrs`.
`.pypirc` | This file holds your information for authenticating with PyPI, both the live and the test versions. | Make sure to put this file in your home folder – its path should be `~/.pypirc`.

### More on `setup.cfg`
From hynek.me: For our minimal Python-only project, we’ll only need four lines in setup.cfg:

```
[bdist_wheel]
universal = 1

[metadata]
license_file = LICENSE
```

Walkthrough of the above:
1. First part will make wheel build a universal wheel file (e.g. attrs-15.1.0-py2.py3-none-any.whl) and you won’t have to circle through virtual environments of all supported Python versions to build them separately.  Note that you'll need `wheel` installed for this. 
2. The second part ensures that your LICENSE file is part of the wheel files which is a common license requirement.

### A note on `README`

As noted above, .rst files can be properly rendered by PyPI without additional effort; .md files require some additional work to have PyPI render them on your project page.

**If you're using a markdown-formatted README file you'll also need a `setup.cfg` file** with the following:

```
[metadata]
description-file = README.md
```

This is necessary if you're using a markdown readme file. At upload time, you may still get some errors about the lack of a readme — don't worry about it.

**Alternate**: use `pypandoc`, which converts from .rst to .md.  Install `pypandoc`, then navigate in the terminal to the location of your `README` file, launch Python, and do:

```python
import pypandoc

#converts markdown to reStructured
z = pypandoc.convert('README','rst',format='markdown')

#writes converted file
with open('README.rst','w') as outfile:
    outfile.write(z)
```

## Example directory structure

**Example 1:**

```
pyfinance                        # the "project folder"
|-- LICENSE                      # <-- *this level is the directory root!*
|-- MANIFEST.in                  # <--
|-- README.rst                   # or: README.md`
|-- setup.py
|-- pyfinance                    # this is the package folder itself*
    |-- __init__.py
    |-- datasets.py
    |-- ols.py
    |-- options.py
    |-- general.py
    |-- returns.py
    |-- utils.py
```

\* This is the name you'll use to import the package.

**Example 2:**

```
root-dir/                       # arbitrary working directory name*
  setup.py
  setup.cfg
  LICENSE.txt
  README.md
  mypackage/
    __init__.py
    foo.py
    bar.py
    baz.py
```

\*Note that the name of the project folder doesn’t have to be the same as the package name.

**Example 2:**

```
YOUR-PROJECT-FOLDER
|-- CHANGES.txt (OPTIONAL)
|-- LICENSE.txt
|-- MANIFEST.in
|-- README
|-- docs (FOLDER)
|-- setup.py
|-- PACKAGENAME (FOLDER)
    |-- __init__.py
    |-- Makefile (OPTIONAL)
    |-- FILE1.py
    |-- FILE2.py
    |-- data (FOLDER, OPTIONAL)
        |-- included_data.dat
    |-- example (FOLDER)
        |-- EXAMPLE.txt
```

## `setup()` keyword arguments
An example `setup.py`: [pypa/sampleproject/setup.py](https://github.com/pypa/sampleproject/blob/master/setup.py).

Argument | Use | Note(s)
------------ | ------------- | -------------
`name` | The name of your project, determining how your project is listed on PyPI. | [PEP 508](https://www.python.org/dev/peps/pep-0508/) discusses valid project names.
`version` | This is the current version of your project, allowing your users to determine whether or not they have the latest version, and to indicate which specific versions they’ve tested their own software against. | See [choosing a versioning scheme](https://packaging.python.org/tutorials/distributing-packages/#choosing-a-versioning-scheme) and [PEP 440](https://www.python.org/dev/peps/pep-0440/).
`description` | -- | Displayed on PyPI.
`long_description` | -- | Displayed on PyPI.  See code below for automatically grabbing it from `README.rst`.
`url` | A homepage URL for your project. | I.e. `url='https://github.com/pypa/sampleproject'`.
`download_url` | A link to a hosted file with your repository's code. | Github will host this for you, but only if you create a git tag. In your repository, type: `git tag 0.1 -m "Adds a tag so that we can put this on PyPI."`. Then, type `git tag` to show a list of tags — you should see 0.1 in the list. Type `git push --tags origin master` to update your code on Github with the latest tag information. Github creates tarballs for download at `https://github.com/{username}/{module_name}/archive/{tag}.tar.gz`.
`author` | -- | I.e. `author='The Python Packaging Authority'`.
`author_email` | -- | I.e. `author_email='pypa-dev@googlegroups.com'`.
`license` | Provide the **type** of license you are using. | Note that this doesn't need to refer to the license file itself.
`classifiers` | Provide a list of classifiers that categorize your project.  **These must fall under a prespecified set of classifiers; PyPI will refuse to accept packages with unknown classifiers.** This information is used for searching and browing projects on PyPI. | [Full listing of classifiers](https://pypi.python.org/pypi?%3Aaction=list_classifiers).
`keywords` | List keywords that describe your project. | Can be a single space-separated string (`keywords='sample setuptools development'`) or a list (`keywords = ['testing', 'logging', 'example']`).
`packages` | It’s required to list the packages to be included in your project. Although they can be listed manually, `setuptools.find_packages` finds them automatically. Use the `exclude` keyword argument to omit packages that are not intended to be released and installed. | `find_packages()` takes a source directory and two lists of package name patterns to exclude and include. If omitted, the source directory defaults to the same directory as the setup script.  A common specification is `packages=find_packages(exclude=['contrib', 'docs', 'tests*'])`.
`install_requires` | Specify what dependencies a project minimally needs to run.  More on declaring dependencies [here](https://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-dependencies). | **When the project is installed by pip, this is the specification that is used to install its dependencies.**
`python_requires` | If your project only runs on certain Python versions, setting the `python_requires` argument to the appropriate [PEP 440 version specifier](https://www.python.org/dev/peps/pep-0440/#version-specifiers) string will prevent pip from installing the project on other Python versions. | Some [examples](https://packaging.python.org/tutorials/distributing-packages/#python-requires) from the docs.

Note that the above list is not exhaustive.  Other kwargs include `scripts`, `data_files`, and `package_data`.

### Having `long_description` pull from your `README`:

```python
from codecs import open

# __file__ is the pathname of the file from which the module was loaded.
# Then `here` would be something like 'C:\Users\bsolomon\anaconda3\pyfinance'
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()
```

# Uploading to PyPI
## About uploading
[unfinished] - see links below.

_Official docs:_
- [Packaging your project](https://packaging.python.org/tutorials/distributing-packages/#packaging-your-project)
- [Uploading your project to PyPI](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)

Note that the above are two separate steps.  
1. The first consists of creating your distribution, mainly via putting a new directory `dist/` under your project’s root directory.  When you build your package, `setup.py` creates a `dist/` directory in your project directory and puts everything on the specified packages along with everything in the `MANIFEST.in` file in a single `.tar.gz` file in that directory.
2. The project is actually uploaded in the second step.

You **invoke setup from the command line** to _produce eggs, upload to PyPI, and automatically include all packages in the directory where the setup.py lives_.  See the [command reference](https://setuptools.readthedocs.io/en/latest/setuptools.html#command-reference) section of the `setuptools` docs for detail on each command.  One of particular importance is the [upload](https://setuptools.readthedocs.io/en/latest/setuptools.html#upload-upload-source-and-or-egg-distributions-to-pypi) command.  `setup()` is also called when you run `python setup.py install` within the project directory.

> _Note_: Most examples will shown snippets such as
> 
> ```
> python setup.py sdist
> ```
> 
> Keep in mind that you need to reference the full `setup.py` path if `setup` isn't in your `cd`.  For example,
> 
> ```
> python C:/Users/Brad/anaconda3/pyfinance/setup.py --help-commands
> ```

The parameter above, `sdist`, produces a _source distribution_.

## The upload process

From hynke.me: Building a source distribution and a wheel of your project is just a matter of

```
$ rm -rf build
$ python setup.py sdist bdist_wheel
```

Now you should have a **new directory called `dist`** under the root containing (1) a source distribution file and (2) a wheel file.  Example:

```
dist
|-- attrs-15.1.0-py2.py3-none-any.whl
└-- attrs-15.1.0.tar.gz
```

The first line accounts for a bug in wheel that won’t clean up the build directory between builds, which puts you at risk of shipping stale build files.

From glpyh: Want to upload some stuff to PyPI? This should do it for almost any project:
```
$ pip install twine
$ python setup.py sdist bdist_wheel
$ twine upload dist/*
```

From peterdowns.com:

```
python setup.py register -r pypi
python setup.py sdist upload -r pypi
```

## Using TestPyPI
_Official guide: [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)_

Before releasing on the main PyPI repo, you might prefer training with the PyPI test site, which is cleaned on a semi regular basis.

From peterdowns.com:

```
python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
```

Walkthrough of above:
- `register` will attempt to register your package against PyPI's test server, just to make sure you've set up everything correctly.
- After the second command, you should get no errors, and should also now be able to see your library in the [TestPyPI repository](https://testpypi.python.org/pypi).


# Other
- [Binary distributions](https://packaging.python.org/glossary/#term-binary-distribution)
- TODO: hynek.me article unfinished

## `.pypirc` & `keyring`

A `.pypirc` file holds your information for authenticating with PyPI, both the live and the test versions.  Make sure to put this file in your home folder – its path should be `~/.pypirc`.  Example from peterdowns.com:

```
[distutils]
index-servers =
  pypi
  pypitest

[pypi]
repository=https://pypi.python.org/pypi
username=your_username
password=your_password

[pypitest]
repository=https://testpypi.python.org/pypi
username=your_username
password=your_password
```

Conforming example (hynek.me):
```
[distutils]
index-servers=
    pypi
    test

[test]
repository = https://test.pypi.org/legacy/
username = <your test user name goes here>

[pypi]
username = <your production user name goes here>
```

You can use alternately `keyring` to store your PyPI credentials in a secure system storage.

Setuptools augments the upload command with support for `keyring`, allowing the password to be stored in a secure location and not in plaintext in the `.pypirc` file. To use `keyring`, first install `keyring` and set the password for the relevant repository, e.g.:

```
python -m keyring set <repository> <username>
Password for '<username>' in '<repository>': ********
```

I.e.

```
$ keyring set https://test.pypi.org/legacy/ <your user name>
Password for '<your user name>' in 'https://test.pypi.org/legacy/':
```

```
$ keyring set https://upload.pypi.org/legacy/ <your production user name>
Password for '<your production user name>' in 'https://upload.pypi.org/legacy/':
```

Then, in `.pypirc`, set the repository configuration as normal, but omit the password. Thereafter, uploads will use the password from the keyring.



