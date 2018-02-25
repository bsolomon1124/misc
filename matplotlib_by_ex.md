# Matplotlib by Example

A picture says a thousand words, and with Python's **matplotlib** library, it fortunately takes far less than a thousand words of code to create a production-quality graphic.

However, matplotlib is also a massive library, and getting a plot to look "just right" is often practiced on a trial-and-error basis.  Using one-liners to generate basic plots in matplotlib is fairly simple, but skillfully commanding the remaining 98% of the library can be daunting.

This article is a beginner-to-intermediate-level walkthrough on matplotlib that mixes theory with example.  While learning by example can be tremendously insightful, it helps to have a little understanding of the library's inner workings and layout as well.

Here's what we'll cover:

- [Why can matplotlib be confusing?](#why-can-matplotlib-be-confusing)
- [pylab: what is it, and should I use it?]()
- [The matplotlib object hierarchy]()
- [Stateful versus stateless approaches]()
- [Understanding `plt.subplots()` notation]()
- [The "Figures" behind the scenes]()
- [A burst of color: `imshow()` and `matshow()`]()
- [Plotting in pandas]()
- [Wrapping up]()
- [More resources]()
- [Appendix A: configuration and styling]()
- [Appendix B: interactive mode]()

This article assumes the user knows a tiny bit of NumPy; we'll mainly use the [`numpy.random`](https://docs.scipy.org/doc/numpy/reference/routines.random.html) module here to generate "toy" data, drawing samples from different statistical distributions.  For example, `numpy.random.uniform()` draws samples from a uniform distribution.

If you don't already have matplotlib installed, see [here](https://matplotlib.org/users/installing.html) for a walkthrough before proceeding.

## Why can matplotlib be confusing?

Learning matplotlib can be a frustrating process at times.  The problem is not that matplotlib's documentation is lacking (it's extensive, actually).  But, what can be challenging is that:

- The library itself is huge, at something like 200,000 total lines of code.
- Matplotlib is home to several different _interfaces_ (ways of constructing a figure) and capable of interacting with a handful of different _backends_.  (Backends deal with the process of how charts are actually rendered, not just structured internally.)
- While it is comprehensive, some of matplotlib's own public documentation is seriously [out-of-date](https://matplotlib.org/users/shell.html).  The library is still evolving, and many older examples floating around elsewhere on the internet may take 70% less lines of code in their modern version.

And so, before we get to any glitzy examples, it's useful to grasp the core concepts of matplotlib's interface.

## pylab: what is it, and should I use it?

A bit of history: John D. Hunter, a neurobiologist, began developing matplotlib around 2003, originally inspired to emulate commands from Mathworks' MATLAB software.  John passed away tragically young at age 44, in 2012, and matplotlib is now a full-fledged community effort, developed and maintained by a host of others.  (John [talked about](https://www.youtube.com/watch?v=e3lTby5RI54) the evolution of matplotlib at the 2012 SciPy conference, which is worth a watch.)

One relevant feature of MATLAB is its _global style_.  The Python concept of importing is not heavily used in MATLAB, and most of MATLAB's [functions](https://www.mathworks.com/help/matlab/functionlist.html) are readily available to the user at the top level.

Knowing that matplotlib has its roots in MATLAB helps to explain why pylab exists.  pylab is a module within the matplotlib library that was built to mimic MATLAB's global style.  It exists only to bring a number of functions and classes from both NumPy and matplotlib into the namespace, making for an easy transition for former MATLAB users who were not used to needing `import` statements.  MATLAB converts (who are all fine people, I promise!) liked this functionality, because with `from pylab import *`, they could simply call `plot()` or `array()` directly, as they would in MATLAB.

The issue here may be apparent to some Python users: using `from pylab import *` in a session or script is generally bad practice.  Matplotlib now directly addresses this in its own tutorials:

> [pylab] still exists for historical reasons, but it is highly advised not to use. It pollutes namespaces with functions that will shadow Python built-ins and can lead to hard-to-track bugs. To get IPython integration without imports the use of the `%matplotlib` magic is preferred. [[source](https://matplotlib.org/users/shell.html#using-matplotlib-in-a-python-shell)]

Internally, there are a ton of potentially conflicting imports being masked within the short pylab [source](https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/pylab.py).  And in fact, using `ipython --pylab` (from the terminal/command line) or `%pylab` (from IPython/Jupyter tools) simply calls `from pylab import *` under-the-hood.

The bottom line is that **matplotlib has abandoned this convenience module and now explicitly recommends against using pylab,**  bringing things more in line with one of Python's key notions--that _explicit is better than implicit_.

Without the need for pylab, we can usually get away with just one canonical import:

```pycon
>>> import matplotlib.pyplot as plt
```

Let's also import NumPy while we're at it, which we'll use for generating data later on, and call `np.random.seed()` to make examples with random data reproducible:

```pycon
>>> import numpy as np
>>> np.random.seed(444)
```

## The matplotlib object hierarchy

The first of two important big-picture matplotlib concepts is that of its **object hierarchy**.

If you've worked through any introductory tutorial, you've probably called something like `plt.plot([1, 2, 3])`.  This one-liner hides the fact that **a plot is really a hierarchy of nested Python objects.**  A "hierarchy" here means that there is a tree-like structure of matplotlib objects underlying each plot.

A `Figure` object is the outermost container for a matplotlib graphic, which can contain multiple `Axes` objects.  One source of confusion is from this naming: an `Axes` actually translates into what we think of as an individual plot or graph (rather than the plural of "axis", as we might expect).

To reiterate, you can think of the `Figure` object as the box-like container that contains one or more `Axes` (actual plots).  Below the `Axes` in the hierarchy are smaller objects such as tick marks, individual lines, legends, and text boxes.  Almost every "element" of a chart is its own manipulable Python object, all the way down to the ticks and labels:

![](fig_map.png)

Here's an illustration of this hierarchy in action.  Don't worry if you're not familiar with this notation, which we'll cover later on.

```pycon
>>> fig, _ = plt.subplots()
>>> type(fig)
<class 'matplotlib.figure.Figure'>
```

Above we created two variables with `plt.subplots()`.  The first is a top-level `Figure` object; the second is a "throwaway" variable that we don't need just yet, denoted with an underscore.  Using attribute notation, it is easy to traverse down the figure hierarchy and see the _first tick of the y axis of the first Axes object_:

```pycon
>>> one_tick = fig.axes[0].yaxis.get_major_ticks()[0]
>>> type(one_tick)
<class 'matplotlib.axis.YTick'>
```

Above, `fig` (a `Figure` class) has multiple `Axes` (a list, for which we take the first element).  Each `Axes` has a `yaxis` and `xaxis`, each of which have a collection of "major ticks," and we grab the first one.

Matplotlib presents this as a figure anatomy, rather than an explicit hierarchy:

![](anatomy.png)

(In true matplotlib style, the figure above is created in the matplotlib docs [here](https://matplotlib.org/examples/showcase/anatomy.html).)

## Stateful versus stateless approaches

Alright, we need one more chunk of theory before we can get into the shiny graphics.  A matplotlib concept that arguably does not get enough attention is the difference between **stateful** (a.k.a. state-based) and **stateless** (a.k.a. object-oriented, OO) approaches.

Above, we used `import matplotlib.pyplot as plt` to import the pyplot module from matplotlib and name it `plt`.

Almost all functions from pyplot, such as `plt.plot()`, are _implicitly_ either creating a new `Figure` and its `Axes`, or referring to an existing `Figure`/`Axes` if one already exists.  Hidden in the matplotlib docs is this helpful snippet:

> [With pyplot], simple functions are used to add plot elements (lines, images, text, etc.) **to the current axes in the current figure**. [emphasis added]

Hardcore ex-MATLAB users may choose to word this by saying something like, "`plt.plot()` is a state-machine interface that implicitly tracks of the current figure!"  In English, this means that:
- The stateful interface makes its calls with `plt.plot()` and other top-level pyplot functions.  There is only ever one Figure or Axes that you're manipulating at a given time, and you don't need to explicitly refer to it.
- Modifying the underlying objects directly is the object-oriented approach.

Tying these together, most of the *functions* from pyplot also exist as *methods* of the `matplotlib.axes.Axes` class.

This is easier to see by peaking under the hood; `plt.plot()` can be boiled down to five or so lines of code:

```pycon
# matplotlib/pyplot.py
>>> def plot(*args, **kwargs):
...     """An abridged version of plt.plot()."""
...     ax = plt.gca()
...     return ax.plot(*args, **kwargs)

>>> def gca(**kwargs):
...     """Get the current Axes of the current Figure."""
...     return plt.gcf().gca(**kwargs)
```

That is, calling `plt.plot()` is just a convenient way to get the _current Axes of the current Figure_ and then call its `plot()` method.  This is what is meant by the assertion that the stateful interface always "implicitly tracks" the plot that it wants to reference.

pyplot is home to a [batch of functions](https://matplotlib.org/api/pyplot_summary.html#the-pyplot-api) which are really just _wrappers_ around matplotlib's object-oriented interface.  For example, with `plt.title()`, there are corresponding _setter_ and _getter_ methods within the OO approach, `ax.set_title()` and `ax.get_title()`.  (Use of getters and setters tends to be more popular in languages such as Java, but is a key feature of matplotlib's OO approach.)

Calling `plt.title()` gets translated into this one line: `gca().set_title(s, *args, **kwargs)`.  What is this doing?

- `gca()` gets the current axis.
- `set_title()` is a setter method, which sets the title for that Axes object.  The "convenience" here is that we didn't need to specify any Axes object explicitly with `plt.title()`.

Similarly, if you take a few moments to look at the source for top-level functions like [`plt.grid()`](https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/pyplot.py#L3708), [`plt.legend()`](https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/pyplot.py#L3714), and [`plt.ylabels()`](https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/pyplot.py#L1521), you'll notice that all of them follow the same structure of delegating to the current Axes with `gca()`, and then calling some method of the current Axes.  (This is the underlying object-oriented approach!)

## Understanding `plt.subplots()` notation

Alright, enough theory.  Now, we're ready to tie everything together and do some plotting.  From here on out, **we'll mostly rely on the stateless (object-oriented) approach**, which is more customizable and comes in handy as graphs become more complex.

The prescribed way to create a Figure with a single Axes under the OO approach is (not too intuitively) with `plt.subplots()`.  (This is really the only time that the OO approach uses `pyplot`, to create a Figure and Axes).

```pycon
>>> fig, ax = plt.subplots()
```

Above, we took advantage of iterable unpacking to assign a separate variable to each of the two results of `plt.subplots()`.  Notice that we didn't pass arguments to `subplots()` here; the default call is `subplots(nrows=1, ncols=1)`.  Consequently, `ax` is a single `AxesSubplot` object:

```pycon
>>> type(ax)
<class 'matplotlib.axes._subplots.AxesSubplot'>
```

and we can call its _instance methods_ to manipulate the plot similarly to how we call pyplots functions.  Let's illustrate with a stacked area graph of three time series:

```pycon
>>> rng = np.arange(50)
>>> rnd = np.random.randint(0, 10, size=(3, rng.size))
>>> yrs = 1950 + rng

>>> fig, ax = plt.subplots(figsize=(5, 3))
>>> ax.stackplot(yrs, rng + rnd, labels=['Eastasia', 'Eurasia', 'Oceania'])
>>> ax.set_title('Combined debt growth over time')
>>> ax.legend(loc='upper left')
>>> ax.set_ylabel('Total debt')
>>> fig.tight_layout()
```

What's going on above?

- After creating three random time series, we defined one Figure containing one Axes (a plot, `ax`).
- We call methods of `ax` directly to create a stacked area chart, and add a legend, title, and y-axis label.  Under the object-oriented approach, it's clear that all of these are attributes of `ax`.
- `tight_layout()` applies to the Figure object as a whole to clean up whitespace padding.

TODO: constrain sides

![](debt.png)

Let's look at an example with multiple subplots (Axes) within one Figure, plotting two correlated arrays that are drawn from the [discrete uniform distribution](https://en.wikipedia.org/wiki/Discrete_uniform_distribution):

```pycon
>>> x = np.random.randint(low=1, high=11, size=50)
>>> y = x + np.random.randint(1, 5, size=x.size)
>>> data = np.column_stack((x, y))

>>> fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2,
                                   figsize=(8, 4))

>>> ax1.scatter(x=x, y=y, marker='o', c='r', edgecolor='b')
>>> ax1.set_title('Scatter: $x$ versus $y$')
>>> ax1.set_xlabel('$x$')
>>> ax1.set_ylabel('$y$')

>>> ax2.hist(data, bins=np.arange(data.min(), data.max()),
             label=('x', 'y'))
>>> ax2.legend(loc=(0.65, 0.8))
>>> ax2.set_title('Frequencies of $x$ and $y$')
>>> ax2.yaxis.tick_right()
```

![](twosubplot.png)

There's a little bit more going on in this example:
- Because we're creating a "1x2" Figure, the returned result of `plt.subplots(1, 2)` is now a Figure object and a NumPy array of Axes objects.  (You can inspect this with `fig, axs = plt.subplots(1, 2)`.)
- We deal with `ax1` and `ax2` individually.  (Something it'd be difficult to do with the stateful approach.)  The final line is a good illustration of the object hierarchy, where we are modifying the `yaxis` belonging to the second Axes, placing its ticks and ticklabels to the right.
- Text inside dollar signs utilizes [TeX markup](https://en.wikipedia.org/wiki/TeX) to put variables in italics.

Remember that multiple Axes can be enclosed in or "belong to" a given figure; in the case above, `fig.axes` (lowercase, not uppercase Axes--there's no denying the terminology is a bit confusing) gets us a list of all the Axes objects:

```pycon
>>> (fig.axes[0] is ax1, fig.axes[1] is ax2)
(True, True)
```

Taking things to the next step, we could alternatively create a figure that holds a 2x2 grid of `Axes` objects:

```pycon
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
```

Now, what is `ax`?  It's no longer a single `Axes`, but a two-dimensional NumPy array of them:

```pycon
>>> type(ax)
numpy.ndarray

>>> ax
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x1106daf98>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x113045c88>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x11d573cf8>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x1130117f0>]],
      dtype=object)

>>> ax.shape
(2, 2)
```

This is reaffirmed by the docstring:

> `ax` can be either a single `matplotlib.axes.Axes` object or an array of `Axes` objects if more than one subplot was created.

We now need to call plotting methods on _each_ of these `Axes` (not the NumPy array, which is just a container in this case.)  A common way to address this is to use **iterable unpacking** after flattening the array to be one-dimensional:

```pycon
>>> fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(7, 7))
>>> ax1, ax2, ax3, ax4 = ax.flatten()  # flatten a 2d NumPy array to 1d
```

We could've also done this with `((ax1, ax2), (ax3, ax4)) = ax`, but the first approach tends to be more flexible.

To illustrate some more advanced subplot features, let's pull some macroeconomic California housing data extracted from a compressed tar archive, using `io`, `tarfile`, and `urllib` from Python's Standard Library.

```pycon
>>> from io import BytesIO
>>> import tarfile
>>> from urllib.request import urlopen

>>> url = 'http://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.tgz'
>>> b = BytesIO(urlopen(url).read())
>>> fpath = 'CaliforniaHousing/cal_housing.data'

>>> with tarfile.open(mode='r', fileobj=b) as archive:
...     housing = np.loadtxt(archive.extractfile(fpath), delimiter=',')
```

The "response" variable `y` below, to use the statistical term, is an area's average home value.  `pop` and `age` are the area's population and average house age, respectively.

```pycon
>>> y = housing[:, -1]
>>> pop, age = housing[:, [4, 7]].T
```

Next let's define a "helper function" that places a text box inside of a plot and acts as an "in-plot title":

```pycon
>>> def add_titlebox(ax, text):
...     ax.text(.55, .8, text,
...         horizontalalignment='center',
...         transform=ax.transAxes,
...         bbox=dict(facecolor='white', alpha=0.6),
...         fontsize=12.5)
...     return ax
```

We're ready to do some plotting.  Matplotlib's [`gridspec`](https://matplotlib.org/api/gridspec_api.html) module allows for more subplot customization.  pyplot's `subplot2grid()` interacts with this module nicely.  Say we want to create a layout like this:

![](empty_gridspec.png)

Above, what we actually have is a 3x2 grid.  `ax1` is twice the height and width of `ax2`/`ax3`, meaning that it takes up two columns and two rows.

![](empty_gridspec_annot.png)

The second argument to `subplot2grid()` is the (row, column) location of the Axes within the grid:

```pycon
>>> gridsize = (3, 2)
>>> fig = plt.figure(figsize=(12, 8))
>>> ax1 = plt.subplot2grid(gridsize, (0, 0), colspan=2, rowspan=2)
>>> ax2 = plt.subplot2grid(gridsize, (2, 0))
>>> ax3 = plt.subplot2grid(gridsize, (2, 1))
```

Now, we can proceed as normal, modifying each Axes individually:

```pycon
>>> ax1.set_title('Home value as a function of home age & area population',
...               fontsize=14)
>>> sctr = ax1.scatter(x=age, y=pop, c=y, cmap='RdYlGn')
>>> plt.colorbar(sctr, ax=ax1, format='$%d')
>>> ax1.set_yscale('log')
>>> ax2.hist(age, bins='auto')
>>> ax3.hist(pop, bins='auto', log=True)

>>> add_titlebox(ax2, 'Histogram: home age')
>>> add_titlebox(ax3, 'Histogram: area population (log scl.)')
```

![](gridspec_ex.png)

Above, `colorbar()` (different from ColorMap earlier) gets called on the Figure directly, rather than the Axes.  Its first argument is the result of `ax1.scatter()`, which functions as a mapping of y-values to a ColorMap.

Visually, there isn't much differentiation in color (the y-variable) as we move up-and-down the y-axis, indicating that home age seems to be a stonger determinant of house value.

## The "Figures" behind the scenes

Each time you call `plt.subplots()` or the lesser-used `plt.figure()` (which creates a Figure, with no Axes), you are creating a new Figure object that matplotlib sneakily keeps around in memory.  Earlier, we alluded to the concept of a current Figure and current Axes.  By default, these are the most-recently-created Figure and Axes, which we can show with the builtin function `id()` to display the address of the object in memory:

```pycon
>>> fig1, ax1 = plt.subplots()

>>> id(fig1)
4525567840

>>> id(plt.gcf())  # `fig1` is the current figure
4525567840

>>> fig2, ax2 = plt.subplots()
>>> id(fig2) == id(plt.gcf())  # current figure has changed to `fig2`
True
```

After the above routine, the current figure is `fig2`, the most recently created figure.  However, both figures are still hanging around in memory, each with a corresponding number (1-indexed, in MATLAB style):

```pycon
>>> plt.get_fignums()
[1, 2]
```

A useful way to get all of the Figures themselves is with a mapping of `plt.figure()` to each of these integers:

```pycon
>>> def get_all_figures() -> list:
...    return [plt.figure(i) for i in plt.get_fignums()]

>>> get_all_figures()
[<matplotlib.figure.Figure at 0x10dbeaf60>,
 <matplotlib.figure.Figure at 0x1234cb6d8>]
```

A takeaway: be cognizant of this if running a script where you're creating a group of figures.  You'll want to explicitly close each of them after use to avoid a `MemoryError`.  `plt.close()` by itself closes the current figure; `plt.close(num)` closes the figure number `num`, and `plt.close('all')` closes all the figure windows.

```pycon
>>> plt.close('all')
>>> get_all_figures()
[]
```

## A burst of color: `imshow()` and `matshow()`

While `ax.plot()` is one of the most common plotting methods on an Axes, there are a whole host of others, as well.  (We used `ax.stackplot()` above; you can find the complete list [here](https://matplotlib.org/api/axes_api.html?highlight=axes%20class#plotting).)

One group of methods that get heavy use are `imshow()` and `matshow()`, with the latter being a wrapper around the former.  These are useful anytime that a raw array an be visualized as a colored grid.

First, let's create two distinct grids with some fancy NumPy indexing:

```pycon
>>> x = np.diag(np.arange(2, 12))[::-1]
>>> x[np.diag_indices_from(x[::-1])] = np.arange(2, 12)
>>> x2 = np.arange(x.size).reshape(x.shape)
```

Next, we can map these to their image representations.  In this specific case, we toggle "off" all axis labels and ticks by passing, using a dictionary comprehension and passing the result to `ax.tick_params()`, then using a [context manager](https://docs.python.org/3/reference/datamodel.html#context-managers) to disable the grid:

```pycon
>>> sides = ('left', 'right', 'top', 'bottom')
>>> nolabels = {s: False for s in sides}
>>> nolabels.update({'label%s' % s: False for s in sides})
>>> print(nolabels)
{'left': False, 'right': False, 'top': False, 'bottom': False, 'labelleft': False,
 'labelright': False, 'labeltop': False, 'labelbottom': False}
```

Using this context manager to disable the Axes grid, we call `matshow()` on each Axes.  Lastly, we need to put the colorbar in what is technically a _new Axes_ within `fig`.  For this we can use a bit of an esoteric function from deep within matplotlib:

```pycon
>>> from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable

>>> with plt.rc_context(rc={'axes.grid': False}):
...     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
...     ax1.matshow(x)
...     img2 = ax2.matshow(x2, cmap='RdYlGn_r')
...     for ax in (ax1, ax2):
...         ax.tick_params(axis='both', which='both', **nolabels)
...     for i, j in zip(*x.nonzero()):
...         ax1.text(j, i, x[i, j], color='white', ha='center', va='center')
...     divider = make_axes_locatable(ax2)
...     cax = divider.append_axes("right", size='5%', pad=0)
...     plt.colorbar(img2, cax=cax, ax=[ax1, ax2])
...     fig.suptitle('Heatmaps with `Axes.matshow`', fontsize=16)
```

![](heatmaps.png)

## Plotting in pandas

The pandas library has become popular for not just for enabling powerful data analysis, but also for its handy pre-canned plotting methods.  Interestingly though, pandas plotting methods are really just convenient _wrappers_ around existing matplotlib calls.

That is, the `plot()` method on pandas' Series and DataFrame (`df.plot()`) is just a simple wrapper around `plt.plot()`.  One convenience provided, for example, is that if the DataFrame's Index consists of dates, `gcf().autofmt_xdate()` is called internally by pandas to get the current Figure and nicely auto-format the x-axis.

In turn, remember that `plt.plot()` (the state-based approach) is implicitly aware of the current Figure and current Axes, so pandas is following the state-based approach.

We can prove this "chain" of function calls with a bit of introspection.  First, let's construct a plain-vanilla pandas Series, assuming we're starting out in a fresh interpreter session:

```pycon
>>> import pandas as pd

>>> s = pd.Series(np.arange(5), index=list('abcde'))
>>> ax = s.plot()

>>> type(ax)
<matplotlib.axes._subplots.AxesSubplot at 0x121083eb8>

>>> id(plt.gca()) == id(ax)
True
```

This internal architecture is helpful to know when you are mixing pandas plotting methods with traditional matplotlib calls, which is done below in plotting the moving average of a widely-watched financial time series.  `ma` is a pandas Series for which we can call `ma.plot()` (the pandas method), and then customize by retrieving the Axes that is created by this call (`plt.gca()`), for matplotlib to reference.

```pycon
>>> import pandas as pd
>>> import matplotlib.transforms as mtransforms

>>> url = 'https://fred.stlouisfed.org/graph/fredgraph.csv?id=VIXCLS'
>>> vix = pd.read_csv(url, index_col=0, parse_dates=True, na_values='.',
...                   infer_datetime_format=True,
...                   squeeze=True).dropna()
>>> ma = vix.rolling('90d').mean()
>>> state = pd.cut(ma, bins=[-np.inf, 14, 18, 24, np.inf],
...                labels=range(4))

>>> cmap = plt.get_cmap('RdYlGn_r')
>>> ma.plot(color='black', linewidth=1.5, marker='', figsize=(8, 4),
...         label='VIX 90d MA')
>>> ax = plt.gca()  # get the current Axes that ma.plot() references
>>> ax.set_xlabel('')
>>> ax.set_ylabel('90d moving average: CBOE VIX')
>>> ax.set_title('Volatility Regime State')
>>> ax.grid(False)
>>> ax.legend(loc='upper center')
>>> ax.set_xlim(xmin=ma.index[0], xmax=ma.index[-1])

>>> trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
>>> for i, color in enumerate(cmap([0.2, 0.4, 0.6, 0.8])):
...     ax.fill_between(ma.index, 0, 1, where=state==i,
...                     facecolor=color, transform=trans)
>>> ax.axhline(vix.mean(), linestyle='dashed', color='xkcd:dark grey',
...            alpha=0.6, label='Full-period mean', marker='')
```

![](vix.png)

There's a lot happening above:

- `ma` is a 90-day moving average of the VIX Index, a measure of market expectations of near-term stock volatility.  `state` is a binning of the moving average into different _regime states_; a high VIX is seen as signaling a heightened level of fear in the marketplace.
- `cmap` is a ColorMap--a matplotlib object that is essentially a mapping of floats to RGBA colors.  Any colormap can be reversed by appending `'_r'`, so `'RdYlGn_r'` is the reversed Red-Yellow-Green colormap.  Matplotlib maintains a handy [visual reference guide](https://matplotlib.org/examples/color/colormaps_reference.html) to colormaps.
- The only real pandas call we're making here is `ma.plot()`.  This calls `plt.plot()` internally, so to integrate the object-oriented approach, we need to get an explicit reference to the current Axes with `ax = plt.gca()`.
- The second chunk of code creates color-filled blocks that correspond to each bin of `state`.  `cmap([0.2, 0.4, 0.6, 0.8])` says, "get an RGBA sequence for the colors at the 20th, 40th, 60th, and 80th "percentile" along the colormaps's spectrum.  [`enumerate()`](https://dbader.org/blog/python-enumerate) is used because we want to map each state back to a color.

Pandas also comes built-out with a smattering of [more advanced plots](https://pandas.pydata.org/pandas-docs/stable/visualization.html#plotting-tools) (which could take up an entire tutorial all on their own).  However, all of these, like their simpler counterparts, rely on matplotlib machinery internally.

## Wrapping up

As shown by some of the examples above, there's no getting around that matplotlib can be a technical, syntax-heavy library.  Creating a production-ready chart sometimes requires a half hour of Googling and combining a hodgepodge of lines meant to fine-tune a plot.  However, understanding how matplotlib's interfaces interact is an investment that an pay off down the road.  As Real Python's own Dan Bader has advised, taking the time to dissect code rather than resorting to the Stack Overflow "copy pasta" tends to be a smarter long-term solution.  Sticking to the object-oriented approach can save hours of frustration when you want to take a plot from plain to a work of art.

## More resources

From the matplotlib documentation:
- An index of matplotlib [examples](https://matplotlib.org/examples/index.html)
- The usage [FAQ](https://matplotlib.org/faq/usage_faq.html)
- The [tutorials](https://matplotlib.org/tutorials/index.html) page, which is broken up into beginner, intermediate, and advanced sections
- [Lifecylcle of a plot](https://matplotlib.org/tutorials/introductory/lifecycle.html#the-lifecycle-of-a-plot) touches on the object-oriented versus stateful approaches

Third-party resources:
- DataCamp's matplotlib [cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)
- PLOS Computational Biology: [Ten Simple Rules for Better Figures](http://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1003833&type=printable)
- Chapter 9 (Plotting & Visualization) of Wes McKinney's [_Python for Data Analysis, 2nd ed._](http://a.co/icUQo3Z)
- Chaper 11 (Visualization with Matplotlib, Pandas, and Seaborn) of Ted Petrou's [_Pandas Cookbook_](http://a.co/9YzpuRP)
- Section 1.4 (Matplotlib: Plotting) of the [Scipy Lecture Notes](http://www.scipy-lectures.org/_downloads/ScipyLectures-simple.pdf)
- The [xkcd](https://xkcd.com/color/rgb/) color palette
- The matplotlib [external resources](https://matplotlib.org/resources/index.html) page
- queirozf.com: [Matplotlib, Pylab, Pyplot, etc: What's the difference between these and when to use each?](http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these)
- The [visualization](https://pandas.pydata.org/pandas-docs/stable/visualization.html) page in the pandas documentation

Other plotting libraries
- The [seaborn](https://seaborn.pydata.org/) library, built on top of matplotlib and designed for advanced statistical graphics, which could take up an entire tutorial all on its own
- [Datashader](http://datashader.org/), a graphics library geared specifically towards large datasets
- A list of [other third-party packages](https://matplotlib.org/thirdpartypackages/index.html) from the matplotlib documentation

## Appendix A: configuration and styling

If you've been following along with this tutorial, it's likely that the plots popping up on your screen look different stylistically than the ones given here.

Matplotlib offers two ways to configure style in a uniform way across different plots:

1. By customizing a matplotlibrc file;
2. By changing your configuration parameters interactively, or from a _.py_ script.

A matplotlibrc file (**Option #1** above) is basically a text file specifying user-customized settings that are remembered between Python sessions.

(A tip: GitHub is a great place to keep configuration files--I keep mine [here](https://github.com/bsolomon1124/config/blob/master/matplotlibrc).  Just make sure that they don't contain personally identifiable or private information, such as passwords or SSH private keys!)

Alternatively, you can change your configuration parameters interactively (**Option #2** above).  When you `import matplotlib.pyplot as plt`, you get access to an `rcParams` object that resembles a Python dictionary of settings.  All of the module objects starting with "rc" are means to interact with your plot styles and settings:

```pycon
>>> [attr for attr in dir(plt) if attr.startswith('rc')]
['rc', 'rcParams', 'rcParamsDefault', 'rc_context', 'rcdefaults']
```

Of these,
- `plt.rcdefaults()` restores the rc parameters from Matplotlib's internal defaults, which are listed at `plt.rcParamsDefault`.  This will revert back (overwrite) whatever you've already customized in a matplotlibrc file.
- `plt.rc()` is used for setting parameters interactively
- `plt.rcParams` is a (mutable) dictionary-like object that lets you manipulate settings directly.  If you have customized settings in a matplotlibrc file, these will be reflected in this dictionary.

With `plt.rc()` and `plt.rcParams`, these two syntaxes are equivalent:

```pycon
>>> plt.rc('lines', linewidth=2, color='r')  # Syntax 1

>>> plt.rcParams['lines.linewidth'] = 2  # Syntax 2
>>> plt.rcParams['lines.color'] = 'r'
```

Notably, the Figure class then [uses some of these these](https://github.com/matplotlib/matplotlib/blob/master/lib/matplotlib/pyplot.py#L498) as its default arguments.

Relatedly, a **style** is just a predefined cluster of custom settings.  To view available styles, we can use:

```pycon
>>> plt.style.available
['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight',
 'seaborn-whitegrid', 'classic', '_classic_test', 'fast', 'seaborn-talk',
 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale',
 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted',
 'seaborn', 'Solarize_Light2', 'seaborn-paper', 'bmh', 'seaborn-white',
 'dark_background', 'seaborn-poster', 'seaborn-deep']
```

And to set a style, call:

```pycon
>>> plt.style.use('fivethirtyeight')
```

Your plots will now take on a new look (this full example is available [here](https://matplotlib.org/examples/style_sheets/plot_fivethirtyeight.html)):

![](plot_fivethirtyeight.png)

For inspiration, Matplotlib keeps some [style sheet displays](https://matplotlib.org/gallery.html#style_sheets) for reference as well.

## Appendix B: interactive mode

Behind the scenes, matplotlib also handles interaction with a number of **backends**.  A backend is the workhorse between actually rendering a chart.  (On the popular Anaconda distribution, for instance, the default backend is Qt5Agg.)  Some backends are interactive

While interactive mode is off by default, you can check its status with `plt.rcParams['interactive']` or `plt.isinteractive()`, and toggle it on and off with `plt.ion()` and `plt.ioff()`, respectively:

```pycon
>>> plt.rcParams['interactive']  # or: plt.isinteractive()
True
```
```pycon
>>> plt.ioff()
>>> plt.rcParams['interactive']
False
```

In some code examples, you may notice the presence of `plt.show()` at the end of a chunk of code.  The main purpose of `plt.show()`, as the name implies, is to actually "show" (open) the figure when you're running with interactive mode turned _off_.  In other words,
- If interactive mode is on, you don't need `plt.show()`, and images will automatically pop-up and be updated as you reference them.
- If interactive mode is off, you'll need `plt.show()` to display a figure and `plt.draw()` to update a plot.

Below, we make that interactive mode is off, which requires that we call `plt.show()` after building the plot itself.

```pycon
plt.ioff()
x = np.arange(-4, 5)
y1 = x ** 2
y2 = 10 / (x ** 2 + 1)
fig, ax = plt.subplots()
ax.plot(x, y1, 'rx', x, y2, 'b+', linestyle='solid')
ax.fill_between(x, y1, y2, where=y2>y1, interpolate=True,
                color='green', alpha=0.3)
lgnd = ax.legend(['y1', 'y2'], loc='upper center', shadow=True)
lgnd.get_frame().set_facecolor('#ffb19a')
plt.show()
```

Notably, interactive mode has nothing to do with what IDE you're using, or whether you've enable _inline_ plotting with something like `jupyter notebook --matplotlib inline` or `%matplotlib`.
