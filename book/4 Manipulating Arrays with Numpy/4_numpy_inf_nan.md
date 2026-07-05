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




# Infinity and Not-A-Number (nan)

Some arithmetic operations, such as division by zero, lead to infinity or undertermined numbers, which normally result in an error:

```{code-cell} ipython3
:tags: [raises-exception]

1 / 0
```

Since operations on arrays perform many arithmetic operations at once, it would be inconvenient to get an error each time only a few calculations fail. For this reason, instead of generating errors, NumPy only warns and provides special constants to express infinity ({{np_inf}}) and undetermined numbers ({{np_nan}}, not-a-number):

```{code-cell} ipython3
import numpy as np

a = np.array([0.0, 1.0, -1.0, 1.0])
b = np.array([0.0, 0.0, 0.0, 1.0])

c = a / b

c
```

To know which operations resulted in `nan` or `inf`, use {{np_isnan}} and {{np_isinf}}:

```{code-cell} ipython3
np.isnan(c)
```

```{code-cell} ipython3
np.isinf(c)
```

:::{tip} Missing data
It is common in data analysis to use `np.nan` for representing missing data. For instance, we could record the (x, y, z) trajectory of a reflective marker and use (`nan`, `nan`, `nan`) when the marker is not seen by the cameras.
:::
