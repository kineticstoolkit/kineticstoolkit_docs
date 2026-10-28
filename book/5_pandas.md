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

# Chapter 5 - Importing and Exporting Tabular Data using Pandas

{{pandas}} is a huge and very popular package that is particularly useful for working with 1d series and 2d tabular data.

This book does not pretend to cover even a microscopic part of the vast possibilities offered by Pandas. It mainly covers how to use Pandas as an intermediary container to import and export data between different software (e.g., Excel, R, Jasp, etc.), and different Python packages such as [NumPy](../4_numpy.md) and the [Kinetics Toolkit](part_ii.md).


```{figure} fig_pandas_logo.png
:label: fig_pandas_logo
:width: 300px
The Pandas logo
```


## Importing Pandas

Usually, Pandas is imported in the `pd` namespace:

```{code-cell} ipython3
import pandas as pd
```


## DataFrame

The most useful type provided by Pandas is the {{pd_dataframe}}. We can see it as a table with optionally labelled columns:

```{code-cell} ipython3
some_data = [
    [1,  6, 11, 16],
    [2,  7, 12, 17],
    [3,  8, 13, 18],
    [4,  9, 14, 19],
    [5, 10, 15, 20]
]

df = pd.DataFrame(
    some_data,
    columns=["x", "y", "z", "radius"],
)

df
```

