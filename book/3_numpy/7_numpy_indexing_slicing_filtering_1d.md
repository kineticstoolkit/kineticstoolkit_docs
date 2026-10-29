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


# Indexing, slicing and filtering one-dimensional arrays

This section presents how to access specific indexes of an array in the aim of creating new arrays or modifying arrays.


## Indexing and slicing 1d arrays

Indexing and slicing a one-dimensional array is identical to indexing a [Python list](../1_python/7_python_lists.md).

:::{tip}
As a reminder:

- Indexing means accessing one element using an index: `the_array[2]`
- Slicing means accessing several elements using a slice: `the_array[0:3]`
:::

Throughout this section, we will work with two example arrays:
- `data`: some random data;
- `time`: the corresponding time.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

data = np.array([0.0, 0.58, 0.95, 0.95, 0.58, 0.0, -0.59, -0.96, -0.96, -0.59])
time = np.arange(10) / 10

plt.plot(time, data, "s-")
plt.grid(True);
```

As mentioned above, **indexing** a one-dimensional array is identical to [indexing a list](../2%20Learning%20Python/python_lists_indexing.md). To read one element of a list/array:

```{code-cell} ipython3
data[2]  # Read the 3rd element
```

To write one element of a list/array:

```{code-cell} ipython3
data[2] = 0.58  # Assign 0.35 to the 3rd element

# Plot the result
plt.plot(time, data, "s-")
plt.grid(True)

data[2] = 0.95  # Reset to its original value
```

Negative indexing also works:

```{code-cell} ipython3
# Read the last data
data[-1]
```


**Slicing** a one-dimensional array is identical to [slicing a list](../2%20Learning%20Python/python_lists_slicing.md). To read several elements of a list/array:

```{code-cell} ipython3
# Keep only the values at indexes 2, 4, 6 and 8 of the original array
# Start at 2 (incl.), up to 9 (excl.) by steps of 2:
data_subset = data[2:9:2]
time_subset = time[2:9:2]

# Plot the result
plt.plot(time, data, "s-", label="original data")
plt.plot(time_subset, data_subset, "o-", label="subset")
plt.grid(True)
plt.legend();
```

To write several elements of a list/array:

```{code-cell} ipython3
# Replace values at indexes 2, 4, 6, 8 of the original list/array by
# [-0.7, -0.8, -0.9, -1.0]

modified_data = data.copy()
modified_data[2:9:2] = [-0.7, -0.8, -0.9, -1.0]

# Plot the result
plt.plot(time, data, "s-", label="original data")
plt.plot(time, modified_data, "o-", label="modified data")
plt.grid(True)
plt.legend();
```


:::{tip}
Note the line:

```
modified_data = data.copy()
```

Using the {{ndarray_copy}} method is required here, because otherwise we are just telling Python to assign an additional name (`modified_data`) to the same variable (`data`). In this case, modifying `modified_data` would also modify `data` since they are both the same array. Using the `copy` method creates a new, unique array so that modifying one won't modify the other.
:::


## 💪 Exercise 1

You used an accelerometer to detect a small movement. The acceleration returned by the instrument is expressed by this list, at a sampling frequency of 100 Hz.

```{code-cell} ipython3
acc = [0.01, 0.01, 0.00, 0.00, 0.02, 0.77, 0.82, 0.86, 0.81, 0.74, 0.07, 0.02]
```

```{code-cell} ipython3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

acc = np.array(acc)
time = np.arange(acc.shape[0]) / 100

plt.plot(time, acc, "o-r")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration")
plt.grid(True);
```

However, by carefully inspecting your signal, you realize that the data is late by 40 milliseconds. You want to fix this delay, but you also want to keep the same number of samples in your signal.

- Using NumPy slicing, write a code that moves forward every data by 40 ms.
- Fill the missing data at the end with zeros.

In summary, you want to produce the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]

new_acc = acc.copy()
new_acc[0:-4] = acc[4:]
new_acc[-5:] = 0

time = np.arange(acc.shape[0]) / 100
fig = plt.figure()
plt.plot(time, acc, "o-r")
plt.plot(time, new_acc, "o--b")
plt.plot(
    np.array([5, 2, 3, 2, 3, 2, 5]) / 100,
    [0.4, 0.4, 0.5, 0.4, 0.3, 0.4, 0.4],
    "k",
    linewidth=5,
)
plt.xlabel("Time (s)")
plt.ylabel("Acceleration")
plt.grid(True);
```

::::{dropdown} Tip 1
Do not forget to convert the list to an array.
::::

::::{dropdown} Tip 2
Separate the problem in two separate steps. First shift the signal, then fill the rest of the signal with zeroes. We suggest to plot the intermediary result between both steps to check if the first step worked as expected.
::::

::::{dropdown} Tip 3
Shifting the signal is equivalent to reading a certain portion of the signal, and then assign this portion to another portion of the signal.
::::

::::{dropdown} Solution
```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt


# Convert acc to an array
acc = np.array(acc)

# We will plot intermediary steps, to better visualize what we do.
plt.subplot(1, 3, 1)
plt.plot(acc, "o-")
plt.title("Original signal")

# STEP 1 - Shift the signal.
#
# At 100 Hz, the sampling period is 1/100 = 0.01. Therefore, 40 ms is 4 samples.
# We need to shift the acceleration by -4 samples. In other words, we need to
# assign acc[from sample 4 to the end] to acc[from sample 0 to the end-4]
acc[:-4] = acc[4:]

# Plot the new signal
plt.subplot(1, 3, 2)
plt.plot(acc, "o-")
plt.title("Shifted signal")

# STEP 2 - Fill the rest with zeros
acc[-4:] = 0

# Let's see the result
plt.subplot(1, 3, 3)
plt.plot(acc, "o-")
plt.title("End result")

plt.tight_layout();
```
::::


## Filtering 1d arrays

:::{important}
This section is about manipulating NumPy arrays, and more precisely about selecting specific indexes in an array using a mask of booleans or integers. This is not about filtering a time series using a moving average or Butterworth filter, which will be seen later in section [](../5_timeseries/8_filters.md).
:::

We learned how to access **one data** using indexing, and **multiple regularly-spaced data** using slicing. To read **multiple non-regularly-spaced data**, we use filtering. We call it filtering because we selectively filter out some data using a mask.

Using these NumPy arrays:

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

data = np.array([0.0, 0.58, 0.95, 0.95, 0.58, 0.0, -0.59, -0.96, -0.96, -0.59])
time = np.arange(10) / 10
```

Let's say we want to keep only the following indexes:

```{code-cell} ipython3
:tags: [remove-input]

bool_mask = [True, False, False, True, False, False, False, False, True, True]

plt.plot(time, data, "s-")
for i, value in enumerate(bool_mask):
    if value:
        plt.text(
            time[i],
            data[i] + 0.04,
            "$\\checkmark$",
            ha="center",
            fontsize=50,
            color="g",
        )
    else:
        plt.text(
            time[i], data[i] + 0.04, "x", ha="center", fontsize=30, color="r"
        )
plt.grid(True);        
```

We can create a mask to select directly which items to keep, and which items to reject.

This mask can be either a **boolean** mask, which is the same shape as `data`, and where each data to keep is True, and where each data to discard is False:

```{code-cell} ipython3
bool_mask = [True, False, False, True, False, False, False, False, True, True]
```

of an **integer** mask, where we explicitly list the indexes to keep:

```{code-cell} ipython3
int_mask = [0, 3, 8, 9]
```

In any case, we then use this mask between brackets, as we would index or slice the array:

```{code-cell} ipython3
plt.subplot(3,1,1)
plt.plot(time, data, "s-")
plt.title("Original data")

plt.subplot(3,1,2)
plt.plot(time[bool_mask], data[bool_mask], "s-")
plt.title("Filtered data, using a mask of bool")

plt.subplot(3,1,3)
plt.plot(time[int_mask], data[int_mask], "s-")
plt.title("Filtered data, using a mask of int")

plt.tight_layout();
```

:::{tip}
Since indexes can also be negative, then masks of integers can also use negative values.
:::

### Creating a mask using a comparison operation

In section [](3_numpy_arithmetics.md), you learned how to generate arrays of bool by comparing an array to a number using comparison operators such as `==`, `<`, `>=`, etc. These comparisons are a powerful way to filter an array. For example, to keep every positive value and reject the rest:

```{code-cell} ipython3
to_keep = data >= 0  # Create a boolean mask of the values to keep
print("to_keep =", to_keep)

plt.plot(time, data, "s-", label="Original data")
plt.plot(time[to_keep], data[to_keep], "o-", label="Filtered data")
plt.legend();
```

Or, as another example, to replace any negative value by 0:

```{code-cell} ipython3
is_negative = data < 0
print("is_negative =", is_negative)

new_data = data.copy()
new_data[is_negative] = 0  

plt.plot(time, data, "s-", label="Original data")
plt.plot(time, new_data, "o-", label="New data")
plt.legend();
```


## 💪 Exercise 2

You measured the step length of a person during 10 steps. Here are these measurements:

```{code-cell} ipython3
import numpy as np

step_length = np.array(
    [0.707, 0.730, 0.752, 0.707, 0.691, 0.726, 0.722, 0.726, 0.710, 0.661]
)  # in metres
```

For each of these questions, write a single line of code that prints the requested step lengths.

1. From the third step up to the end.

::::{dropdown} Solution
```{code-cell} ipython3
step_length[2:]
```
::::

2. The last two steps;

::::{dropdown} Solution
```{code-cell} ipython3
step_length[-2:]
```
::::

3. All steps, but without the first two and the last two.

::::{dropdown} Solution
```{code-cell} ipython3
step_length[2:-2]
```
::::

4. Every other step starting from the third.

::::{dropdown} Solution
```{code-cell} ipython3
step_length[2::2]
```
::::

5. Steps 2, 5, 6, and 7, with step 0 being the first.

::::{dropdown} Solution
```{code-cell} ipython3
step_length[[2, 5, 6, 7]]

# Note the double bracket: this is equivalent to write:
# >> mask = [2, 4, 6, 7]
# >> step_length[mask]
```
::::

6. The first and the last one.

::::{dropdown} Solution
```{code-cell} ipython3
step_length[[0, -1]]
```
::::


## 💪 Exercise 3

The position of an object was recorded in metres over one second at a sampling frequency of 100 Hz:

```{code-cell} ipython3
import numpy as np

p = np.array(
    [
        0.    , 0.0099, 0.0196, 0.0291, 0.0384, 0.0475, 0.0564, 0.0651,
        0.0736, 0.0819, 0.09  , 0.0979, 0.1056, 0.1131, 0.1204, 0.1275,
        0.1344, 0.1411, 0.1476, 0.1539, 0.16  , 0.1659, 0.1716, 0.1771,
        0.1824, 0.1875, 0.1924, 0.1971, 0.2016, 0.2059, 0.21  , 0.2139,
        0.2176, 0.2211, 0.2244, 0.2275, 0.2304, 0.2331, 0.2356, 0.2379,
        0.24  , 0.2419, 0.2436, 0.2451, 0.2464, 0.2475, 0.2484, 0.2491,
        0.2496, 0.2499, 0.25  , 0.2499, 0.2496, 0.2491, 0.2484, 0.2475,
        0.2464, 0.2451, 0.2436, 0.2419, 0.24  , 0.2379, 0.2356, 0.2331,
        0.2304, 0.2275, 0.2244, 0.2211, 0.2176, 0.2139, 0.21  , 0.2059,
        0.2016, 0.1971, 0.1924, 0.1875, 0.1824, 0.1771, 0.1716, 0.1659,
        0.16  , 0.1539, 0.1476, 0.1411, 0.1344, 0.1275, 0.1204, 0.1131,
        0.1056, 0.0979, 0.09  , 0.0819, 0.0736, 0.0651, 0.0564, 0.0475,
        0.0384, 0.0291, 0.0196, 0.0099
    ]
)
```

Knowing that:

$$
v(i) = \dfrac{p(i+1) - p(i-1)}{t(i+1) - t(i-1)}
$$

Write a program of only 1 to 2 lines that calculates the speed of the object. Then, plot the velocity and position on the same figure to check your result.

::::{tip}
Due to the calculation of speed requiring position values before and after the current sample, the velocity array will be 2 values shorter than the position array, as illustrated in {numref}`fig_speed_calculation`.

```{figure} fig_speed_calculation.png
:label: fig_speed_calculation
:width: 500px
Calculating speed leads to a shorter array.
```

::::

```{code-cell} ipython3
:tags: [remove-cell]
import numpy as np

t = np.arange(100) / 100
p = t - t**2
```

::::{dropdown} Solution
```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(100) / 100
v = (p[2:] - p[0:-2]) / (t[2:] - t[0:-2])

# Since the time step is regular at 0.01, we could also calculate v using a single line:
v = (p[2:] - p[0:-2]) / (2 * 0.01)

# Plot the result
plt.plot(t, p, label="Position (m)")
plt.plot(t[1:-1], v, label="Velocity (m/s)")
plt.xlabel("Time (s)")
plt.grid(True)
plt.legend()
plt.show()
```
::::


## 💪 Exercise 4

You have recorded a noisy signal:

```{code-cell} ipython3
signal = np.array(
    [
        0.436, 0.493, 0.467, 0.467, 0.482, 0.497, 0.474, 0.493, 0.474, 0.467,
        0.470, 0.455, 0.482, 0.501, 0.470, 0.482, 0.467, 0.467, 0.558, 0.413,
        0.463, 0.444, 0.463, 0.417, 0.528, 0.455, 0.486, 0.459, 0.490, 0.459,
    ]
)
```

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt

plt.plot(signal);
```

You want to smooth this signal using a moving average with a window of three samples. This means creating a new array where each value is the average of the three neighbour values of the raw signal, as illustrated in {numref}`fig_moving_average`.

```{figure} fig_moving_average.png
:label: fig_moving_average
:width: 450px
Filtering using a moving average.
```


Using only one line, apply this filter to the raw, noisy signal. Then, plot both the raw and filtered signals on the same figure to verify your result.

::::{dropdown} Solution
```{code-cell} ipython3
:tags: [hide-cell]
import numpy as np
import matplotlib.pyplot as plt


filtered = (signal[0:-2] + signal[1:-1] + signal[2:]) / 3

plt.plot(signal, label="raw")
plt.plot(filtered, label="filtered")
plt.legend();
```
::::


