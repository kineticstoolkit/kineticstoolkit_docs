---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Plotting a line graph

The most common command of Matplotlib's pyplot module is probably {{plt_plot}}, which plots one or many series as a curve.

The input series can be either a [standard Python lists](../2_python/7_python_lists.md), a [NumPy Arrays](../4_numpy/2_numpy_ndarray.md), or a `Pandas DataFrames`. For one-dimensional data, it takes one list (y) or two lists (x, y) as arguments.

To plot the list `[1.0, 2.0, -1.0, -0.0]`, we do:

```python
import matplotlib.pyplot as plt


y = [1.0, 2.0, -1.0, -0.0]
plt.plot(y)
```

which returns the curve in [](#fig_matplotlib_qt5). If, instead, you see the figure inline, or in Spyder's *Graph* pane, or not at all, then you probably did not configure Matplotlib for interactive graphics. See [](../1_getting_started/3_getting_started_installing_spyder.md).


:::{figure} matplotlib_qt5.png
:label: fig_matplotlib_qt5
:width: 500px
A Matplotlib figure window.
:::


The different buttons on the figure allow some interaction with the plot:

|                                                           |                                                               |
|:---------------------------------------------------------:|:-------------------------------------------------------------:|
| ![](matplotlib_move.png) Move the figure around (panning) |             ![](matplotlib_zoom_to_rect.png) Zoom             |
| ![](matplotlib_back.png) Undo the last pan/zoom operation | ![](matplotlib_forward.png) Redo the last pan/zoom operation  |
|  ![](matplotlib_home.png) Reset to the initial pan/zoom   | ![](matplotlib_filesave.png) Save the figure to an image file |

By default, `x` starts at 0 and increments by 1 for each point. But we can also specify custom coordinates for `x`:

```{code-cell} ipython3
import matplotlib.pyplot as plt

x = [0.0, 5.0, 10.0, 15.0]
y = [1.0, 2.0, -1.0, -0.0]

plt.plot(x, y);
```

The `x` values don't have to be equidistant:

```{code-cell} ipython3
x = [0.0, 0.5, 1, 10]
y = [1.0, 2.0, -1.0, -0.0]

plt.plot(x, y);
```

