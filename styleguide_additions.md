# Proposed additions to the Real Python Tutorial Style Guide

https://realpython.com/team/style-guide/

**Note:** some of the "recommendations" below may be copied verbatim from various third-party style guides floating around the internet.  This is really just a patchwork of widely-accepted conventions.

----

## Grammatical Style

- Use "we"/"we're" in place of "you/you're" or "I/I'm" - helps the reader feel like they are working alongside the author rather than being "instructed."
- Use an [active](https://en.wikipedia.org/wiki/Active_voice), present-tense voice rather than passive voice wherever possible.  This is more engaging.
    - Good: "We define the function as ..."
    - Bad: "The function is defined as ..."
- Write concisely.  Walk through what is happening in your code, but, in the words of William Strunk, "make every word tell."

## PEP8: Specific Conventions

PEP8 is a huge document, and its sections can be classified as anywhere from "highly recommended" to "this is a good practice to consider."  We could outline a few specific conventions to follow on Real Python for better consistency between articles.

**Indentation:**

4 spaces, 'nuff said.

**Single-versus-double quotes:**

Who cares?  Just **be consistent** throughout the article.

**Wildcard imports:**

Don't use them, ever.

**List/other data structure comprehensions:**

Use them liberally, except when you shouldn't.  Anything that's doubly-nested or more will instantly stop a beginner-level reader dead in their tracks even if the article is well-written and syntactically correct.

```
# Okay
order = list('acebd')
target = list('edba')
res = [m for m in order if m in target]

# Okay, but not great
res2 = [(x, y) for x in range(10) for y in range(5) if x * y > 10]
```

**Spaces (lack thereof) with kwargs/default params:**

```
# Yes
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

# No
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)
```

**Default arguments:**

Don't use mutable objects as default parameters:

```
# Yes
def foo(a, b=None):
     if b is None:
         b = []

# No
def foo(a, b=[])
```

**Variable case:**

```
class MyClass(object):  # also, explicitly inherit from `object`

def my_first_function(param1):

log = logging.getLogger(__name__)  # (most) variables

MAXLEN = 128  # module-level constants (shouldn't really
              # need these in tutorials, though)
```

From Google's Style Guide:

> `module_name`, `package_name`, `ClassName`, `method_name`, `ExceptionName`, `function_name`, `GLOBAL_CONSTANT_NAME`, `global_var_name`, `instance_var_name`, `function_parameter_name`, `local_var_name`.

**Don't use these variable names:**

Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.  In some fonts, these characters are indistinguishable from the numerals one and zero. When tempted to use 'l', use 'L' instead.

**Naming functions:**

Where possible, make functions "verb-like"; consider how a function _acts on_ its arguments when naming it.  `map()` and `filter()` are good examples of this.  `def my_sorter(x):` doesn't really fit this mold.

**Naming variables:**

Be careful about overriding built-ins/reserved words.  If you need to use a reserved word i.e. `class`, add a _ to the end -> `class_`, or use a recognizable-but-altered version, `klas`.

```
# No
list = [1, 2, 3]

# Yes
a = [1, 2, 3]
Tkinter.Toplevel(master, class_='ClassName'))
```

**Conditional expressions/ternary operators**

Okay to use for one-liners. In other cases, prefer to use a complete `if` statement.

```
# Yes
x = 1 if y > 3 else 2
```

**Imports - use separate lines:**

```
# Yes
import os
import sys

# No
import sys, os
```

**Import order:**

Imports should be grouped in the following order:

- standard library imports
- related third party imports
- local application/library specific imports

You should put a blank line between each group of imports.

**Standalone lambdas: don't use them**

```
# Yes
def f(x): return 2*x

# No
f = lambda x: 2*x
```

**Favor string methods over indexing/slicing:**

```
# Yes
if foo.startswith('bar'):

# No
if foo[:3] == 'bar':
```

**Object comparison/type inspection: use `isintance()`:**

```
# Yes
if isinstance(obj, int):

# No
if type(obj) is str:
```

**Take advantage of Python truthiness:**

```
# Yes
if not x:
    break

# No
if x == []:
    break
```

More: [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth-value-testing)

**...but, know when to be more explicit:**

In some cases, we care not just that `x` is Falsey, but about what specifically it _is_.  (For instance, we want to differentiate between it being an empty list, 0, or `None`.)  In these cases, use explicit `is` or comparison operators.

```
# Bad
def func2(a=None):
    if not a:
        print('a is an empty list')  # Or is it??
```

**`try/except`: no bare `except`-clauses**

```
# Yes
try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None

# No
except:
    platform_specific_module = None
```

**Use `is not` instead of `not ... is`:**

```
# Yes
if foo is not None:

# No:
if not foo is None:
```

**Comparisons to singletons**

```
# Yes
if x is not None:

# No
if x != None:
```

**Inline comments: use them sparingly:**

- Inline comments should be separated by at least two spaces from the statement.
- They should start with a # and a single space.

Inline comments are unnecessary and in fact distracting if they state the obvious. Don't do this:

```
# Unnecessary
x = x + 1  # Increment x

# This is OK (not immediately clear what we're doing otherwise)
x = x + 1  # Compensate for border
```

**One-line v. multi-line docstrings:**

```
def one_liner(x):
    """Here's a docstring.  No add'l line needed."""
    return x ** 2

def multi_liner(y):
    """Short, high-level description of what this does.

    Some details here.  Details, details, oh sweet details.
    """

    return max(dosomething(i) for i in y)
```

More detailed cases - defer to [PEP 257](https://www.python.org/dev/peps/pep-0257/).

**Use non-mandatory parentheses:**

Some expressions can get complicated. Parentheses can (and should) be used to make them less ambiguous. This is for the sake of people who read the code, even if it doesn't matter to the Python parser.

```
if (True and True) or (False or True):
    print(True)
```

**Continuation lines:**

```
# Yes:
# -----------------
# Aligned with opening delimiter.
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)

# Hanging indents should add a level.
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

# No:
# -----------------
# Arguments on first line forbidden when not using vertical alignment.
foo = long_function_name(var_one, var_two,
    var_three, var_four)

# Further indentation required as indentation is not distinguishable.
def long_function_name(
    var_one, var_two, var_three,
    var_four):
    print(var_one)
```

**Indents with method chaining**:

Hanging 4 spaces should suffice, per level of nesting.

```
return frame['value'].replace((-4, -5), np.nan)\
    .ffill()\
    .fillna(0.)\
    .resample('A')\
    .prod()\
    .rolling(n)\
    .sum()\
    .lt(n)\
    .astype(np.float64)
```

**Recommended: [type hinting](https://www.python.org/dev/peps/pep-0484/).**

Especially in tutorials where every LOC is never-before-seen by the reader, this helps the user to easily see what the function is designed to take as input and spit out as output.

```
def counter(s: str) -> int:
    # ...
```

## Inline Code: What Deserves Backticks?

How should we refer to different Python objects consistently?  There are a few considerations:

- What gets put into backticks in the first place?
- When do we use a leading `.dot()` and trailing parentheses?

Here's a proposed scheme:

For anything that is a class, such as a `DefaultDict`, simply refer to it "as-is", with no dot-notation or parentheses.  The first few times these are introduced in the article, we could also preface them with their enclosing module/top-level package i.e. `functools.partial`.

Built-in types (`str`, `bytes`, `range`, `True`, or technically, anything that inherits from `type`): refer to these the same way you would non-builtin-classes.  However, this point is certainly up-for-debate because these are technically classes that don't follow CamelCase, but you can use `str()` (which looks like a function, but really isn't) to instantiate a `str` instance.

Functions:

- Module-level functions (`os.walk`): refer to these simply as `walk()`, or `os.walk()`, with closing parentheses to indicate we're talking about a function.
- Instance methods (`mylist.pop()`): refer to these with a leading dot and closing parentheses, `.pop()`, to indicate we're talking about a method and differentiate from a module-level function.
- Attributes and properties: leading dot, no parentheses.  `.is_unique`; `.nonnegative`.

Other things that can be put in backticks (entirely optional; just emphasize consistnecy throughout the article):

- Filenames: `data.csv`
- Libraries/packages/modules themselves: `NumPy`

## Case of Subheadings

```markdown
## Subheadings - Proper Case Except for Small Words of Less Than Three Letters
```

## Other

Here are a few other points that don't qualify directly as "style," but still promote consistency and are good practice.

### Use Generators

Look out for cases where instantiating a data structure isn't necessary and increases space complexity.

```
# Yes
max((i - j) for i, j in combinations(s, 2))

# No
max([(i - j) for i, j in list(combinations(s, 2))])
```

See the [FP HOWTO](https://docs.python.org/3.6/howto/functional.html) and [PEP 289](https://www.python.org/dev/peps/pep-0289/) for more.

### Python 3.x Version

Be aware of your Python 3.x version and let your readers know what features of the article are limited by minor release version.  For example:

- `z = {**x, **y}`  # Python 3.5+
- `yield from`  # Python 3.3+

Again, this pertains more to Python 3.x versions rather than needing to differentiate between 2.x and 3.x constructs such as `xrange` and `range`.

### Using Random Data

Make random data reproducible by seeding a random number generator.

```
import random
import numpy.random as npr

random.seed(444)
npr.seed(444)
```

## Additional Style Guide Resources

(Could add these to the Real Python Style Guide.)

- [PEP8](https://www.python.org/dev/peps/pep-0008/)
    - [Pet Peeves](https://www.python.org/dev/peps/pep-0008/#pet-peeves)
* [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
* [GNU Mailman Coding Style Guide](https://barry.warsaw.us/software/STYLEGUIDE.txt)
* robinwinslow.uk: [A summary of python code style conventions](https://robinwinslow.uk/2014/01/05/summary-of-python-code-style-conventions/)
* voidspace.org.uk: [Python Coding Style & Standards - My Personal Style Guide for Python Source Code](http://www.voidspace.org.uk/python/articles/python_style_guide.shtml)
* The Chromium Projects: [Python Style Guidelines](https://www.chromium.org/chromium-os/python-style-guidelines#TOC-Official-Style-Guide)
* The Hitchhiker's Guide to Python: [Code Style](http://docs.python-guide.org/en/latest/writing/style/)
* David Goodger: [Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#coding-style-readability-counts)
* [Top 10 Python idioms I wish I'd learned earlier](http://prooffreaderplus.blogspot.com/2014/11/top-10-python-idioms-i-wished-id.html)
