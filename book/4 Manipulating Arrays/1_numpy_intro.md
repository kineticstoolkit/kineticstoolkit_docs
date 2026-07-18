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

# Introduction to NumPy

NumPy is a central package in the Python ecosystem and is used by virtually every science-related module. The main goal of {{numpy}} is to perform mathematical operations not only on floats, but also on vectors and matrices, and to perform these operations very quickly.

As an example, let's say we need to average multiple measurements. We could do this easily using basic Python code, by summing every element of a list, and then by dividing the sum by the number of elements:

```{code-cell} ipython3
list_of_float = [1.0, 2.0, 3.0, 2.5, 2.75, 1.5]

# Calculate the sum of every elements
sum = 0
for one_float in list_of_float:
    sum += one_float
    
# Divide by the number of elements
mean = sum / len(list_of_float)

mean
```

NumPy makes it both easier and faster:

```{code-cell} ipython3
import numpy as np

np.mean(list_of_float)
```

This chapter covers the basics of NumPy for biomechanics.

:::{tip}
If you already know Matlab, then this [cheat sheet](https://numpy.org/doc/stable/user/numpy-for-matlab-users.html) could be useful.
:::

```{figure}
:label: fig_numpy_logo
:width: 4in
![NumPy Logo](_static/images/fig_numpy_logo.png)

Numpy logo.
```



## Importing NumPy

As for Matplotlib, NumPy must be imported before using it. It is very common to import NumPy using the `np` alias:

```{code-cell}
import numpy as np
```

So that every NumPy function is available under the `np` namespace:

```{code-cell}
np.mean([1, 2, 3])
```
