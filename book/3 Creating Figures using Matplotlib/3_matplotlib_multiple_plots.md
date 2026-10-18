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


# Plotting multiple series

## Plotting multiple series in a same figure

Many series can be plotted on the same figure, simply by calling `plt.plot` multiple times:

```{code-cell} ipython3
import matplotlib.pyplot as plt

x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

plt.plot(x, y1)
plt.plot(x, y2);
```

By default, any new plot is added to the same figure. Use {{plt_clf}} to clear the current figure.

## Plotting multiple series in multiple figures

Simply use {{plt_figure}} to prepare a new, empty figure that will be used for each subsequent plot, leaving the original one intact:

```{code-cell} ipython3
import matplotlib.pyplot as plt

x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

plt.plot(x, y1)

plt.figure()
plt.plot(x, y2);
```

## Plotting multiple series side by side in a same figure

In some situations, it is useful to show multiple plots side by side in the same figure. This can be done using the {{plt_subplot}} function, which splits a figure into a grid and specifies the location of the next plot on this grid. Its arguments are:

1. The number of lines (int);
2. The number of columns (int);
3. The location of the next plot, starting at 1 in the upper left corner, then going left to right then up to down:

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt

for i in range(12):
    plt.subplot(3, 4, i + 1)
    plt.xticks([])
    plt.yticks([])
    plt.text(0.5, 0.5, f"Location {i+1}", ha="center", va="center")
plt.tight_layout()
```

For instance, to spread five plots on two lines and three columns:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y1 = [1.0, 2.0, 3.0, 1.0]
y2 = [1.0, 3.0, -1.0, 2.0]
y3 = [-1.0, 4.0, -2.0, 2.0]
y4 = [-1.0, -4.0, -3.0, 0.0]
y5 = [2.0, 3.0, -1.0, 1.0]

plt.subplot(2, 3, 1)
plt.plot(y1)
plt.title("First plot")

plt.subplot(2, 3, 2)
plt.plot(y2)
plt.title("Second plot")

plt.subplot(2, 3, 3)
plt.plot(y3)
plt.title("Third plot")

plt.subplot(2, 3, 4)
plt.plot(y4)
plt.title("Fourth plot")

plt.subplot(2, 3, 5)
plt.plot(y5)
plt.title("Fifth plot");
```

We can see that the titles of the second line overlap with the horizontal axes of the first line. This is a common issue with Matplotlib: it does not know how to optimize the spacing while we progressively build the figure. Calling {{plt_tight_layout}} just after building the figure optimizes the spacing so that everything looks clean.

```{code-cell} ipython3
plt.subplot(2, 3, 1)
plt.plot(y1)
plt.title("First plot")

plt.subplot(2, 3, 2)
plt.plot(y2)
plt.title("Second plot")

plt.subplot(2, 3, 3)
plt.plot(y3)
plt.title("Third plot")

plt.subplot(2, 3, 4)
plt.plot(y4)
plt.title("Fourth plot")

plt.subplot(2, 3, 5)
plt.plot(y5)
plt.title("Fifth plot")

plt.tight_layout()
```
