# Python Dunder Methods ... No Deep Shit

(Title inspired by [git: the simple guide](http://rogerdudler.github.io/git-guide/).)

## Guidelines

This is an abbreviated guide to "dunder methods" in Python 3.  It is based off the [Data Model](https://docs.python.org/3/reference/datamodel.html) page from the Python docs.  "Dunder" means double-underscore: `__repr__`, `__bool__`, and others.

Sections are grouped by the general utility of what their methods do.  More commonly overridden/implemented groups are shown first (based on my own judgment).

If a method has a consistent (required, or very common) return type, it is indicated with type hinting.

Most things here use the format `object.__method__(self, ...)`.  That's because:

> if a class defines a method named `__getitem__()`, and `x` is an instance of this class, then `x[i]` is roughly equivalent to `type(x).__getitem__(x, i)`

... and defining a class with `MyClass(object)` means that `MyClass` inherits from `object`.

Not covered here: special attributes (`.__class__`, `.__slots__`, `.__doc__`, `.__name__`, `.__module__`, and others).

## Quick Guide

### Object Instantiation and Deletion

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__init__(self[, ...]) -> None`    | `a = MyClass(x=1, y=2)` | [1] |
| `object.__new__(cls[, ...])`              | `a = MyClass(x=1, y=2)` | [2] |
| `object.__del__(self)`                    | `a = MyClass(); del a`  |     |

**[1]**: `__init__` is responsible for _customizing_ the object.  Its arguments are passed to the class constructor.  `__init__` should always return `None` (implicitly).  It initializes an instance after it's been created, usually adding attributes to it.

**[2]**: You usually won't need `__new__`.  It is responsible for _creating_ the object.  It's first argument is `cls`.  Usually used when you're mimicking subclassing on a type that otherwise can't be subclassed, such as `int`, `unicode`, or `re.Pattern`.  An [example](https://github.com/python/cpython/blob/121eb1694cab14df857ba6abe9839654cada15cf/Lib/pathlib.py#L609) is in the `pathlib` module: creating an instance of `PurePath` actually gets you an instance of `PureWindowsPath` or `PurePosixPath` depending on your OS.

### Representation (Display)

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__repr__(self) -> str`                        | `repr(x)`                 | [1] |
| `object.__str__(self) -> str`                         | `str(x)`                  | [2] |
| `object.__format__(self, format_spec)`                | `format(x, format_spec)`  |     |

**[1]**: The "official" (information-rich, unambiguous) string representation.  "This should look like a valid Python expression that could be used to recreate an object with the same value."

Example can be found in [`tarfile.TarInfo`](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Lib/tarfile.py#L768).

**[2]**: The "informal" (nicely printable) string representation.  Used by `format()` and `print()`.  Defaults to `__repr__` if `__str__` is not defined but `__repr__` is.

### Rich Comparison Methods

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__lt__(self, other) -> bool` | `x < y`  |     |
| `object.__le__(self, other) -> bool` | `x <= y` |     |
| `object.__eq__(self, other) -> bool` | `x == y` |     |
| `object.__ne__(self, other) -> bool` | `x != y` | [1] |
| `object.__gt__(self, other) -> bool` | `x > y`  |     |
| `object.__ge__(self, other) -> bool` | `x >= y` |     |

Notes:

- These methods can also return `NotImplemented`.
- Use [`functools.total_ordering`](https://docs.python.org/3/library/functools.html#functools.total_ordering) to avoid needing to define all of them.

**[1]**: `__ne__()` delegates to `__eq__()` and inverts the result unless it is `NotImplemented`.

### Attribute Access

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__getattr__(self, name)`                  | `x.a`     | [1] |
| `object.__getattribute__(self, name)`             | `x.a`     | [1] |
| `object.__setattr__(self, name, value)`           | `x.a = y` |     |
| `object.__delattr__(self, name)`                  | `del x.a` |     |

**[1]**: Difference between `__getattr__` versus `__getattribute__`: this deserves some discussion.

In most situations, you should use `__getattr__`.

- `__getattribute__` is called first, before checking if the attribute exists.  If you are going to use this, use `def __getattribute__(self, name): return super().__getattribute__(self, name)`

- `__getattr__` does not get called unless either `__getattribute__` (1) raises an `AttributeError` or (2) explicitly calls `__getattr__`.  One common use is to specify what happens and what is returned when the attribute does not exist.

### Methods for Container Types

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__len__(self) -> int`                        | `len(x)`                   |     |
| `object.__length_hint__(self) -> int`                | `operator.length_hint(x)`  | [1] |
| `object.__getitem__(self, key)`                      | `x[key]`                   |     |
| `object.__missing__(self, key)`                      | `x[key]`                   | [2] |
| `object.__setitem__(self, key, value) -> None`       | `x[key] = value`           |     |
| `object.__delitem__(self, key) -> None`              | `del x[key]`               |     |
| `object.__iter__(self)`                              | `iter(x)`                  |     |
| `object.__reversed__(self)`                          | `reversed(x)`              |     |
| `object.__contains__(self, item)`                    | `y in x`                   |     |

**[1]**: `__length_hint__` should return an estimated length for the object (which may be greater or less than the actual length).

**[2]**: Called by `dict.__getitem__()` to implement `self[key]` for dict subclasses when key is not in the dictionary.

### Arithmetic: Emulating Numeric Types

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__add__(self, other)`                 | `x + y`                 |     |
| `object.__sub__(self, other)`                 | `x - y`                 |     |
| `object.__mul__(self, other)`                 | `x * y`                 |     |
| `object.__matmul__(self, other)`              | `x @ y`                 | [1] |
| `object.__truediv__(self, other)`             | `x / y`                 |     |
| `object.__floordiv__(self, other)`            | `x // y`                |     |
| `object.__mod__(self, other)`                 | `x % y`                 |     |
| `object.__divmod__(self, other)`              | `divmod(x, y)`          |     |
| `object.__pow__(self, other[, modulo])`       | `x ** y` or `pow(x, y)` | [2] |

**[1]**: `@` is the matrix multiplication operator, introduced in Python 3.5 / PEP 465.

**[2]**: Optional `modulo` parameter: the signature for `pow()` is `pow(x, y, z=None)`:

> Equivalent to `x**y` (with two arguments) or `x**y % z` (with three arguments).

### Bitwise Operations

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__lshift__(self, other)`              | `x << y`                |
| `object.__rshift__(self, other)`              | `x >> y`                |
| `object.__and__(self, other)`                 | `x & y`                 |
| `object.__xor__(self, other)`                 | `x ^ y `                |
| `object.__or__(self, other)`                  | `x | y`                 |

Bitwise operators: treat a number as if it were a string of bits, written in twos-complement binary.  Used for `int` (and `bool`) operands.

More: Python [wiki](https://wiki.python.org/moin/BitwiseOperators).

### Augmented Arithmetic Assignment

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__iadd__(self, other)`                | `x +=y`  | |
| `object.__isub__(self, other)`                | `x -=y`  | |
| `object.__imul__(self, other)`                | `x *=y`  | |
| `object.__imatmul__(self, other)`             | `x @=y`  | |
| `object.__itruediv__(self, other)`            | `x /=y`  | |
| `object.__ifloordiv__(self, other)`           | `x //=y` | |
| `object.__imod__(self, other)`                | `x %=y`  | |
| `object.__ipow__(self, other[, modulo])`      | `x **=y` | |
| `object.__ilshift__(self, other)`             | `x <<=y` | |
| `object.__irshift__(self, other)`             | `x >>=y` | |
| `object.__iand__(self, other)`                | `x &=y`  | |
| `object.__ixor__(self, other)`                | `x ^=y`  | |
| `object.__ior__(self, other)`                 | `x |=y`  | |

The `i` means "in-place."

Examples: `collections.Counter` [defines](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Lib/collections/__init__.py#L841) several of these.

### Serialization

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__reduce__(self) -> tuple`                |          | |
| `object.__reduce_ex__(self, protocol)`            |          | |
| `object.__getnewargs_ex__(self)`                  |          | |
| `object.__getnewargs__(self)`                     |          | |
| `object.__getstate__(self)`                       |          | |
| `object.__setstate__(self, state)`                |          | |

These are used to define, customize, and control how class instances are pickled and unpickled.

[Reference](https://docs.python.org/3/library/pickle.html#pickling-class-instances) from the pickle docs.  Example: [`datetime.date`](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Lib/datetime.py#L1072)

### Unary Arithmetic Operations

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__neg__(self)`                        | `-x`     | |
| `object.__pos__(self)`                        | `+x`     | |
| `object.__abs__(self)`                        | `abs(x)` | |
| `object.__invert__(self)`                     | `~x`     | |

### Built-in Functions for Type Constructors

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__complex__(self) -> complex`                | `complex(x)`   | |
| `object.__int__(self) -> int`                        | `int(x)`       | |
| `object.__float__(self) -> int`                      | `float(x)`     | |

### Math Functions

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__round__(self[, ndigits])`       | `round(x)`      | |
| `object.__trunc__(self)`                  | `math.trunc(x)` | |
| `object.__floor__(self)`                  | `math.floor(x)` | |
| `object.__ceil__(self)`                   | `math.ceil(x)`  | |

### Context Managers (`with` Statement)

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__enter__(self)`                                      | `with open('/path/to/file.txt') as f:` (example) | |
| `object.__exit__(self, exc_type, exc_value, traceback)`       |                                                  | |

Detail in [`PEP 343`](https://www.python.org/dev/peps/pep-0343/).

Example can be found in [`warnings.catch_warnings`](https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Lib/warnings.py#L451):

```python
class catch_warnings(object):
    # ...
     def __enter__(self):
        # ...
     def __exit__(self, *exc_info):
        # ...
```

Usage:

```python
import warnings

def fxn():
    warnings.warn("deprecated", DeprecationWarning)

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    fxn()
```

### Async IO: Coroutines

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__await__(self)` |

### Async IO: Asynchronous Iterators

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__aiter__(self)` |
| `object.__anext__(self)` |

### Async IO: Asynchronous Context Managers

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__aenter__(self)` |
| `object.__aexit__(self, exc_type, exc_value, traceback)` |

### Binary Arithmetic Operations With **Reflected** Operands

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__radd__(self, other)`            | `x + y`                 | |
| `object.__rsub__(self, other)`            | `x - y`                 | |
| `object.__rmul__(self, other)`            | `x * y`                 | |
| `object.__rmatmul__(self, other)`         | `x @ y`                 | |
| `object.__rtruediv__(self, other)`        | `x / y`                 | |
| `object.__rfloordiv__(self, other)`       | `x // y`                | |
| `object.__rmod__(self, other)`            | `x % y`                 | |
| `object.__rdivmod__(self, other)`         | `divmod(x, y)`          | |
| `object.__rpow__(self, other)`            | `x ** y` or `pow(x, y)` | |
| `object.__rlshift__(self, other)`         | `x << y`                | |
| `object.__rrshift__(self, other)`         | `x >> y`                | |
| `object.__rand__(self, other)`            | `x & y`                 | |
| `object.__rxor__(self, other)`            | `x ^ y `                | |
| `object.__ror__(self, other)`             | `x | y`                 | |

These are only called when:

- The left operand does not support the corresponding operation (i.e. `__add__` for `__radd__`).  "Does not support" means either not defined, or returns `NotImplemented`.
- The operands are of different types

> For instance, to evaluate the expression `x - y`, where `y` is an instance of a class that has an `__rsub__()` method, `y.__rsub__(x)` is called if `x.__sub__(y)` returns `NotImplemented`.

Example:

```python
>>> 's'.__rmul__(2)  # 's' * 2
'ss'
```

### Descriptors

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__get__(self, instance, owner)`               | `a.x`     | |
| `object.__set__(self, instance, value) -> None`       | `a.x = y` | |
| `object.__delete__(self, instance) -> None`           | `del a.x` | |
| `object.__set_name__(self, owner, name)`              | `a.x`     | |

You usually define a descriptor with the purpose of adding it as a class instance attribute.  The purpose of defining a descriptor is that _it can override default behavior upon being looked up as an attribute_.

> For instance, `a.x` has a lookup chain starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and continuing through the base classes of `type(a)` excluding metaclasses.

If `x` is a descriptor instance, you customize what happens when it gets looked up.  A good example is in the Pandas library's [`CachedAccesor`](https://github.com/pandas-dev/pandas/blob/a784aee993ab9a5ac63e5e233a69388ab3bc4c18/pandas/core/accessor.py#L145) class.

See also: [Descriptor HowTo Guide](https://docs.python.org/3/howto/descriptor.html)

### Customizing Class Creation

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `classmethod object.__init_subclass__(cls)`       | | |
| `classmethod object.__prepare__`                  | | |

### Checks

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `X.__instancecheck__(self, instance)` | `isinstance(instance, X)` | |
| `X.__subclasscheck__(self, subclass)` | `issubclass(subclass, X)` | |

### Odds and Ends

| Signature | Invokes | Note |
| --------- | ------- | ---- |
| `object.__call__(self[, args...])`                    | `A(x)(y)`             | [1] |
| `object.__hash__(self) -> int`                        | `hash(x)`             | [2] |
| `object.__bool__(self) -> bool`                       | `bool(x)`             | [3] |
| `object.__bytes__(self) -> bytes`                     | `bytes(x)`            |     |
| `object.__index__(self) -> int`                       | `operator.index(x)`   |     |
| `object.__dir__(self) -> Sequence`                    | `dir(x)`              |     |
| `classmethod object.__class_getitem__(cls, key)`      | `List[int]`           | [4] |
| `object.__sizeof__(self) -> int`                      | `sys.getsizeof(x)`    |     |

**[1]**: A good [example](https://github.com/networkx/networkx/blob/bf1c7cc9b144767523e5abcf84f949d4223848a0/networkx/classes/reportviews.py#L189) is found in the `networkx` library.

Example:

```python
>>> import networkx as nx
>>> G = nx.Graph()
>>> G.add_edges_from([
...     ('a', 'b'),
...     ('a', 'c'),
...     ('d', 'c'),
... ])
>>> G.edges  # as property, returns class instance
EdgeView([('a', 'b'), ('a', 'c'), ('c', 'd')])
>>> G.edges(['b', 'd'])  # with __call__(), filter to certain nodes
EdgeDataView([('b', 'a'), ('d', 'c')])
```

**[2]**: Objects that compare equal should have the same hash value.  "_It is advised to mix together the hash values of the components of the object that also play a part in comparison of objects by packing them into a tuple and hashing the tuple_":

```python
def __hash__(self):
    # tuple is hashable (list is not)
    return hash((self.name, self.nick, self.color))
```

**[3]**: Also used in [truth-value testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing), as in `if x` or `if not x`.

**[4]**: Primarily used with static type hints.  Specified in [PEP 560](https://www.python.org/dev/peps/pep-0560/).

## What Methods Come "Attached" Out of the Box?

If we define a class with just `__init__`, which methods come "pre-attached" to it?  (Note: some of these may return `NotImplemented`.)

```python
from types import (BuiltinMethodType,
                   ClassMethodDescriptorType,
                   MethodType,
                   MethodWrapperType)


class A(object):
    def __init__(self, x: int, y: str):
        self.x, self.y = x, y


mtypes = (BuiltinMethodType,
          ClassMethodDescriptorType,
          MethodType,
          MethodWrapperType)

a = A(2, 'b')
for s in dir(a):
    method = getattr(a, s)
    # Could also use just `callable(method)`, but that would include
    # a.__class__, which isn't a method.  (It returns `A`.)
    if isinstance(method, mtypes) and s.startswith('__'):
        print(s)
```

Output:

```
__delattr__
__dir__
__eq__
__format__
__ge__
__getattribute__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__str__
__subclasshook__
```
