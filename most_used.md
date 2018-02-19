---
layout: post
title: What are Python's most-used modules?
categories: Python
---

## A fair race (as possible)

A note on terminology: here I mostly use "package," "library,"" and "module" synonymously.  Hear me out--to be clear, they're not equivalent; a package is a collection of modules.  However, when we say that a syntax follows `from module import object`, _module_ could in fact be a package name (`from dask import dataframe`) or an actual module (`from six import types`), where the module is possibly a "standalone" module with no package structure or `__init__.py` file.  But for all intents and purposes, we treat these the same.  (TODO: wording).  Likewise, as far as I know, no one walks around saying that they get great use out of the [`numpy.linalg`](https://github.com/numpy/numpy/blob/master/numpy/linalg/linalg.py) module; they simply make reference to [`numpy`](https://docs.scipy.org/doc/numpy/user/whatisnumpy.html) as a package.  Admittedly, this disadvantages standalone modules (such as `six`, `os`, or `sys`, which are not large tools when measured by lines of code).  (TODO: wrap this up)

<span style="font-size=8" * Imports such as `from pymc3 import logit` are actually made possible because the intermediate `from .math import logit` is made in the package's `__init__.py` file.</span>

## Rules

I tried to make this a technically sound, sensible ranking of popularity. (TODO)

- I search for imports only from _within_ `.py` (pure Python) and `.pyx` (Cython) files,  excluding stuff like `.so` (compiled library) and `.pyd` (Cython extension) files.  It's doubtful you'd get regex matches in these C files anyway, but I explicitly excluded them to be certain.  (As well as `__pycache__` `.egg-info`, and `.dist-info` folders.)  This does mean that we could still pick up imports _from within_ built-in modules such as [`csv`](https://docs.python.org/3/library/csv.html) that import their underlying C counterparts--in this case, [`_csv.c`](cpython/Modules/_csv.c), the low-level underpinnings of `csv`.
- I ran these screens off of a fresh Anaconda install, for Python 3.6/MacOS.  That means I was looking only within the just under 400 packages with a checkmark next to their name [here](https://docs.anaconda.com/anaconda/packages/py3.6_osx-64), as of mid-February 2018.
- I ignore all [intra-package references](https://docs.python.org/3/tutorial/modules.html#intra-package-references).  This is any instance where a module imports something from a sibling module in the same package.  These could be either relative imports (`from .builder import builder_registry, ParserRejectedMarkup`) or absolute imports (`import matplotlib.cbook as cbook`, made from within the `matplotlib` library).

## Import syntax

In my (admittedly limited) experience, the best way to construct a durable regex is to first start out with an exhaustive set of test cases, synthesize their commonalities, and construct something that covers the whole group.

Broadly, Python respects two forms of imports:

```python
import module [as name...]
from module import object [as name...]
```

The full syntax for imports can be found [here](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement) (with a description of notation for lexical analysis and syntax [here](https://docs.python.org/3/reference/introduction.html#notation)), but perhaps we can better illustrate through some slighly more involved real-world examples:

```python
import itertools

from operator import itemgetter as _itemgetter, eq as _eq

from pandas.core.sparse.api import *
from ._version import get_versions

from . import event, util

try:
    from defusedexpat import pyexpat as expat
except ImportError:
    from xml.parsers import expat

from .sql.base import (
    SchemaVisitor
    )

from .ode import checkodesol, classify_ode, dsolve, \
    homogeneous_order
```

## TODO

- Standard Library v. Anaconda Distribution
- Os and sys usually just appear as one "import sys" whereas bumpy is used in LOC_heavy packages.
- testfile.py
- Data dump
