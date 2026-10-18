---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Modules and packages

This section presents how to separate your code in modules, and how to import modules and packages to extend Python's functionality.


## Modules

As your code grows, you may want to split your code into multiple files. For example, you may want to put the functions you use the most in a separate file and reuse this file from one script to another. Such separate file is called a module.

Let's create a file named `example_module.py` which contents is:

```python
# Contents of example_module.py

def print_hello():
    print("======")
    print("Hello!")
    print("======")
```

If this script is saved in the current working folder, then you can load it and use it using the `import` command. Then you can use any function it defines by prefixing it with the module name and a dot:

```{code-cell} ipython3
import example_module

example_module.print_hello()
```


## Packages

Congratulation! At this point, you learned the most important elements of the Python programming language for human movement biomechanics. But you may feel that some elements are missing: how do I open a CSV file? How do I create a figure with graphical data? How to I perform trigonometric operations? etc.

Here come the packages. A package consists in one or many modules that have been programmed and shared by others to extend Python's functionality. Several thousands of packages are available for free via [PyPI](https://pipy.org) and [conda-forge](https://conda-forge.org). In this book, we introduce the most important ones: {{ matplotlib }}, {{ numpy }} and {{ pandas }} for any data processing, and {{ kineticstoolkit }} for human movement biomechanics. These packages should already be installed in your setup; if not, please refer to section [](../1%20Getting%20Started/2_getting_started_installing_python.md) to install them.

You import a package exactly as you import a module. Here, we import the {{pyplot}} module of the {{matplotlib}} package:

```{code-cell} ipython3
import matplotlib.pyplot
```

Once imported, we access the module's contents under the `matplotlib.pyplot` namespace:

```{code-cell} ipython3
matplotlib.pyplot.plot([0, 1, 4], "o-");
```


## Namespaces and aliases

A **namespace** is a name that groups different objects (functions, variables, classes). It is used to avoid ambiguities between two modules that could use identical names to define their respective objects. For instance, Python provides the function `max` that returns the maximum value between two floats. NumPy also provides a function `max` that returns the maximum value of an array. Namespaces avoid name clashes: Python's max is accessed using `max()`, while NumPy's max is accessed using `numpy.max()`.

To avoid typing `matplotlib.pyplot` each time we need a pyplot function, it is very common to import it using an **alias**:

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

This line behaves like the previous import, but this time `matplotlib.pyplot` is imported into the `plt` namespace instead of the `matplotlib.pyplot` namespace. This leads to shorter and cleaner lines of code:


```{code-cell} ipython3
plt.plot([0, 1, 4], "o-");
```

The next chapters of this book will guide you in learning the most important packages for analyzing movement biomechanics.
