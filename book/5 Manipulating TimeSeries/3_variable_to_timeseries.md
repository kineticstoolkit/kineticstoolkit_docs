---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Converting between variables and TimeSeries

We now know how to create a TimeSeries from scratch. We can also create a TimeSeries from other variables or even from other TimeSeries.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np
import pandas as pd
```

Any [list](../2%20Learning%20Python/7_python_lists.md), [NumPy array](../4%20Manipulating%20Arrays/2_numpy_ndarray.md), Pandas {{pd_series}} or Pandas {{pd_dataframe}} can be converted to a TimeSeries.


## Numpy Array ↔︎ TimeSeries

To create a TimeSeries from an array:

```{code-cell}
example_array = np.array([1, 2, 3, 4, 5])

example_array
```

```{code-cell}
ts = ktk.TimeSeries(example_array)

ts
```

There is no need to convert back to an array, as the `data` attribute of the TimeSeries already stores the data as arrays:

```{code-cell}
ts.data["data"]
```


## Python List ↔︎ TimeSeries

To create a TimeSeries from a list:

```{code-cell}
example_list = [1, 2, 3, 4, 5]

example_list
```

```{code-cell}
ts = ktk.TimeSeries(example_list)

ts
```

Conversely, we can use the NumPy array's {{np_tolist}} method to convert one of the TimeSeries data values to a list:

```{code-cell}
ts.data["data"].tolist()
```


## Pandas Series ↔︎ TimeSeries

To create a TimeSeries from a Pandas Series:

```{code-cell}
example_series = pd.Series([1, 2, 3, 4, 5])

example_series
```

```{code-cell}
ts = ktk.TimeSeries(example_series)

ts
```

Conversely, we can use Panda's Series constructor to convert one of the TimeSeries data to a Pandas Series:

```{code-cell}
pd.Series(ts.data["data"])
```


## Pandas DataFrame ↔︎ TimeSeries

To create a TimeSeries from a Pandas DataFrame:

```{code-cell} ipython3
example_dataframe = pd.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], columns=["x", "y"])

example_dataframe
```

```{code-cell} ipython3
ts = ktk.TimeSeries(example_dataframe)

ts
```

Conversely, we can use {{ktk_timeseries_to_dataframe}} to convert a TimeSeries to a Pandas DataFrame:

```{code-cell}
ts.to_dataframe()
```


## TimeSeries ↔︎ TimeSeries

As for most types in Python, a TimeSeries is a mutable type, which means that simply writing `ts2 = ts1` does not create a second TimeSeries `ts2` based on TimeSeries `ts1`. Instead, it creates a new variable that addresses the same TimeSeries. As a consequence, modifying `ts2` would also modify `ts1`. To create an independent copy of `ts1`, we use `ts2 = ts1.copy()`.

:::{note}
This same phenomenon also happens with most Python types, including NumPy arrays and Pandas DataFrames. This is why they also include a `copy` method.
:::

The {{ktk_timeseries_copy}} method has different arguments to select which attributes to copy. For instance, if we want to create TimeSeries with the same time and events as another one, but without its data or info, we would use:

```{code-cell}
ts2 = ts.copy(copy_data=False, copy_info=False)
```

Alternatively, we can create a new TimeSeries as we would from any other type:

```{code-cell}
ts2 = ktk.TimeSeries(ts)
```
