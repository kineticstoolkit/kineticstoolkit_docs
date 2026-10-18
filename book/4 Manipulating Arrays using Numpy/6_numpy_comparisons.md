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


# Comparisons and logical operators

## Comparison operators

We can use comparison operators such as `>` or `==` to compare two arrays element-wise. In this case, the result is an array of booleans:

```{code-cell} ipython3
import numpy as np

a = np.array(
    [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0],
    ]
)

b = np.array(
    [
        [5.0, 5.0, 5.0],
        [5.0, 5.0, 5.0],
        [5.0, 5.0, 5.0],
    ]
)

a > b
```


We can also compare arrays with a single number instead of another array:

```{code-cell} ipython3
a > 5.0
```

```{code-cell} ipython3
a == 5.0
```

```{code-cell} ipython3
a >= 5.0
```


To find the indices of the array where the comparison returned true, we can use {{np_nonzero}}:

```{code-cell}
a = np.array([1.0, 2.2, 10.4, 4.6, 5.8, 6.0, 1.2])

print("Result of the comparison:", a > 5)
print("Indices where the result was True:", np.nonzero(a > 5))
```

## 💪 Exercise

We recorded this series of vertical forces using a gait force platform:

```{code-cell} ipython3
import numpy as np

force = np.array(
    [
        17.61, 21.42, 17.61, 17.61, 17.61, 32.85, 25.23, 17.61, 29.04, 32.85,
        25.23, 21.42, 67.14, 810.0, 870.95, 802.38, 726.19, 775.71, 947.14,
        985.23, 954.76, 863.33, 783.33, 676.66, 520.47, 295.71, 150.95, 48.09,
        -1.42, 2.38, 17.61, 2.38, 6.19, 6.19, 6.19, 2.38, 6.19, 13.80,
    ]
)
```

```{code-cell} ipython3
:tags: [remove-input]

import matplotlib.pyplot as plt
import kineticstoolkit.lab as ktk

plt.plot(force)
plt.xlabel("# sample")
plt.ylabel("Force (N)");
```

We want to identify the weight support phase, defined as any sample where the force is higher than 100 newtons.

- Write a one-line code that creates a NumPy array named `is_weight_support`, which has the same shape as `force` and that contains `True` during the weight support phase, and `False` otherwise.

- Verify your code by plotting both `force` and `is_weight_support` on the same figure.

```{code-cell} ipython3
:tags: [hide-cell]
import matplotlib.pyplot as plt

# We create a mask to keep only the weight support phase
is_weight_support = force > 100

# Verify
plt.plot(force, label="Force (N)")
plt.plot(is_weight_support * 1000, label="Weight support (True/False)")
plt.legend();

# Note that we plotted (is_weight_support * 1000) instead of
# is_weight_support to match the vertical scale of the force plot
# so that the comparison is more visible on the figure.
```


## Logical operators

We already learned Python's logical operators `not`, `or`, and `and`. Unfortunately, these operators work only on booleans, not on arrays of booleans. However, NumPy provides equivalent operators:

| Python's operator on `bool` | NumPy's equivalent operator for arrays of `bool` |
|:---------------------------:|:------------------------------------------------:|
|            `not`            |                       `~`                        |
|            `or`             |                       `\|`                       |
|            `and`            |                       `&`                        |

{numref}`fig_numpy_boolean_operators` illustrates the behaviour of each operator.

:::{figure}
:label: fig_numpy_boolean_operators
![Logical operators on Python and Numpy](_static/images/fig_numpy_boolean_operators.png)

Correspondence between logical operations on bool and ndarray.
:::

#todo write an exercise on numpy logical operators
