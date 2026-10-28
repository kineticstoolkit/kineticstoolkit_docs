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

This section presents how to separate your code in modules, and introduces how to use external packages to extend Python's functionality.


## Modules

As your code grows, you may want to split your code into multiple files. For example, you could put the functions you use the most in a separate file and reuse this file from one script to another. Such separate file is called a module.

Let's create a file named `example_module.py` in the current working directory. Its contents is:

```python
# Contents of example_module.py

def print_header(text):
    """Print text underlined."""
    separator = ""
    for i in text:  # For each character of the text
        separator += "-"  # Add a matching - character
    print("")  # Skip a line
    print(text)  # Print the text
    print(separator)  # Print a separator
```

You can now load and use the `print_header` function in any script, using:


```{code-cell} ipython3
from example_module import print_header


print_header("This is a header")
print("This is some text")

print_header("This is another header")
print("This is some text")

```

To import the entire contents of the module instead of just a function, use:

```{code-cell} ipython3
import example_module


example_module.print_header("This is a header")
print("This is some text")

example_module.print_header("This is another header")
print("This is some text")

```

Note that in this case, the module's contents is accessed via a prefix, which is the module name. This prefix is called a namespace, which is simply a way to group objects together, avoiding possible conflicts if two modules defined two objects with the same name.


## Packages

🎉 Congratulation! At this point, you learned the most important elements of the Python programming language for human movement biomechanics. 🎉

But you may feel that some elements are missing:
- How do I open a CSV file?
- How do I create a figure with graphical data?
- How to I perform trigonometric operations?
- etc.

Here come the packages. A package consists in one or many modules that have been programmed and shared by others to extend Python's functionality. Several thousands of packages are available for free via [PyPI](https://pipy.org) and [conda-forge](https://conda-forge.org). In this book, we introduce the most important ones: {{ matplotlib }}, {{ numpy }} and {{ pandas }} for any data processing, and {{ kineticstoolkit }} for human movement biomechanics. These packages should already be installed in your setup; if not, please refer to section [](../1_getting_started/2_getting_started_installing_python.md) to install them.

You import a package exactly as you import a module. Here is an example with the {{pyplot}} module of the {{matplotlib}} package:

```{code-cell} ipython3
import matplotlib.pyplot


matplotlib.pyplot.plot([0, 1, 4], "o-");
```


## Aliases

To avoid typing `matplotlib.pyplot` each time we need a pyplot function, it is very common to import it using an **alias**:

```{code-cell} ipython3
import matplotlib.pyplot as plt
```

This line behaves like the previous import, but this time `matplotlib.pyplot` is imported into the `plt` namespace instead of the `matplotlib.pyplot` namespace. This leads to shorter and cleaner lines of code:


```{code-cell} ipython3
plt.plot([0, 1, 4], "o-");
```

The next chapters of this book will guide you in learning the most important packages for analyzing movement biomechanics.
