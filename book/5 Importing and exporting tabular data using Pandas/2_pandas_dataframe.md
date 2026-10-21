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

# DataFrames

The most useful type provided by Pandas is the DataFrame. We can see it as a bidimensional Numpy array, with these main differences:

| NumPy array                       | Pandas DataFrame                                   |
| --------------------------------- | -------------------------------------------------- |
| Every elements have the same type | Every elements of a same column have the same type |
| Columns are addressed by position | Columns can also be addressed by name              |
| Rows are addressed by position    | Rows can also be addressed by index                |
| Have a fixed number of columns    | New columns can easily be created                  |


Since they are so similar, it is trivial to construct a DataFrame from an array:

```{code-cell} ipython3
import numpy as np
import pandas as pd

ar = np.array(
    [
        [1,  6, 11, 16],
        [2,  7, 12, 17],
        [3,  8, 13, 18],
        [4,  9, 14, 19],
        [5, 10, 15, 20]
    ]
)

df = pd.DataFrame(ar)

df 
```

By default, the column names and the indexes (rows) are increasing integers. But we can also name these columns and indexes.

```{code-cell} ipython3
df = pd.DataFrame(
    ar,
    columns=["x", "y", "z", "radius"],
    index=np.arange(5)/10,
)

df
```


## Indexing, slicing and filtering

We can index a DataFrame exactly like we would with an array: see section [](../4%20Manipulating%20Arrays%20using%20Numpy/8_numpy_indexing_sliging_filtering_nd.md) for a refresher. However, we do not put the brackets directly on the DataFrame, but on its `iloc` (integer location) attribute.

```{code-cell} ipython3
# Get line 1 (index 0.1), column 2 (z)
df.iloc[1, 2]
```

```{code-cell} ipython3
# Get line 1 (index 0.1), columns 0 to 2 (x, y, z)
df.iloc[1, 0:3]
```

However, it is often much more convenient to extract columns based on their name:

```{code-cell} ipython3
# Get column "radius" as a Series
df["radius"]
```


```{code-cell} ipython3
# Get columns "x", "y" and "z" as a new (smaller) DataFrame
df[["x", "y", "z"]]
```

and then extract data using either the line number (using `iloc`) or index (using `loc`).

```{code-cell} ipython3
# Get "x", "y" and "z" at line 1
df[["x", "y", "z"]].iloc[1]
```

```{code-cell} ipython3
# Get "x", "y" and "z" at index 0.1
df[["x", "y", "z"]].loc[0.1]
```

