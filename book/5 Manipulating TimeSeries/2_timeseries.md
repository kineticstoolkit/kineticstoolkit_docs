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

# The TimeSeries class

In biomechanics, we often process data that is a function of time, e.g., electromyography, marker trajectories, force series, etc. When we analyze only a few data points and the sampling frequency is constant, using NumPy is usually sufficient. This is what we did in the last section in the different [NumPy exercises](../../3%20Part%20I%20-%20Learning%20Python%20for%20Biomechanics/4%20Manipulating%20Arrays%20using%20Numpy/numpy_exercises.md).

However, things can get more complicated when:
- data are of different natures, such as marker trajectories, EMG, measured forces, calculated forces, etc.;
- data were recorded by unsynchronized instruments at different sampling frequencies;
- data were recorded with inconstant sample frequencies;
- data are missing (e.g., occluded markers);
- data are noisy;
- etc.

For these reasons, Kinetics Toolkit provides a new type of variable: the {{ktk_timeseries}}.

A TimeSeries is a single container that hold time, data, events and general info.


## Time and data

A TimeSeries in its simplest form contains a time attribute and some data. For example:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ts = ktk.TimeSeries()                     # Create an empty TimeSeries
ts.time = np.arange(0, 10, 0.1)           # Assign time
ts.data["Sinus"] = np.sin(ts.time)        # Add a data series
ts.data["Cosinus"] = np.cos(ts.time)      # Add another data series
ts.data["SquareRoot"] = np.sqrt(ts.time)  # Add yet another data series

ts
```

We can also add data to a TimeSeries using its {{ktk_timeseries_add_data}} method. This method checks that each data series has the same number of samples, whereas assigning it directly to `data` (as above) does not perform such verification.

```{code-cell} ipython3
ts = ktk.TimeSeries()                             # Create an empty TimeSeries
ts.time = np.arange(0, 10, 0.1)                   # Assign time
ts = ts.add_data("Sinus", np.sin(ts.time))        # Add a data series
ts = ts.add_data("Cosinus", np.cos(ts.time))      # Add another data series
ts = ts.add_data("SquareRoot", np.sqrt(ts.time))  # Add yet another data series

ts
```

To see the TimeSeries data:

```{code-cell} ipython3
ts.data
```

TimeSeries can be plotted using their {{ktk_timeseries_plot}} method. We can also specify which of the series to plot.

```{code-cell} ipython3
plt.subplot(1, 3, 1)
ts.plot()

plt.subplot(1, 3, 2)
ts.plot("Cosinus")

plt.subplot(1, 3, 3)
ts.plot(["Sinus", "Cosinus"])

plt.tight_layout()
```

A TimeSeries can also contain multidimensional data, as long as the first dimension corresponds to time. For instance, this [dataset of wheelchair propulsion kinetics](../../5%20Appendix/dataset_kinetics_wheelchair_propulsion.md) expresses forces and moments as Nx4 series of vectors:

$$
\text{Forces} = \begin{bmatrix}
F_x(0) & F_y(0) & F_z(0) & 0 \\
F_x(1) & F_y(1) & F_z(1) & 0 \\
F_x(2) & F_y(2) & F_z(2) & 0 \\
... & ... & ... & ... \\
F_x(N-1) & F_y(N-1) & F_z(N-1) & 0
\end{bmatrix}
$$

$$
\text{Moments} = \begin{bmatrix}
M_x(0) & M_y(0) & M_z(0) & 0 \\
M_x(1) & M_y(1) & M_z(1) & 0 \\
M_x(2) & M_y(2) & M_z(2) & 0 \\
... & ... & ... & ... \\
M_x(N-1) & M_y(N-1) & M_z(N-1) & 0
\end{bmatrix}
$$

```{code-cell} ipython3
ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion.ktk.zip"))

ts.data
```

```{code-cell} ipython3
ts.plot()
```

## Events

In the figure above, we see that the TimeSeries contains cyclic data. These cycles could be delimited using events. There are several ways to edit the events of a TimeSeries, which will be presented later in section [](6_timeseries_event_management.md). For now, we will add the events manually using {{ktk_timeseries_add_event}}:

```{code-cell} ipython3
ts = ts.add_event(8.56, "push")
ts = ts.add_event(9.93, "recovery")
ts = ts.add_event(10.50, "push")
ts = ts.add_event(11.12, "recovery")
ts = ts.add_event(11.78, "push")
ts = ts.add_event(12.33, "recovery")
ts = ts.add_event(13.39, "push")
ts = ts.add_event(13.88, "recovery")
ts = ts.add_event(14.86, "push")
ts = ts.add_event(15.30, "recovery")
```

These 10 events are now added to the TimeSeries' list of events:

```{code-cell} ipython3
ts.events
```

If we plot the TimeSeries again, we can see the added events.

```{code-cell} ipython3
ts.plot()
```

## Info

The TimeSeries' `info` attribute contains metadata such as units and other information. This dictionary is addressed using two nested keys: the first (outer) one is generally what the information refers to (e.g., "Time", "Forces", "LateralFemoralEpicondyleR", "Speed"), and the second (inner) one defines the nature of the information (e.g., "Unit", "Date", "Name").

By default, `info` includes the time unit:

```{code-cell} ipython3
ts.info
```

You may use the {{ktk_timeseries_add_info}}, {{ktk_timeseries_rename_info}} and {{ktk_timeseries_remove_info}} to manage `info`:

```{code-cell} ipython3
ts = ts.add_info("Forces", "Unit", "N")
ts = ts.add_info("Moments", "Unit", "Nm")

ts.info
```

Unless explicitly mentioned, metadata is not used for calculation and is strictly optional. "Unit" info is however used by {{ktk_timeseries_plot}} to plot the units:

```{code-cell} ipython3
ts.plot()
```


## 💪 Exercise

The position of an object has been recorded in metres during one second at a sampling frequency of 100 Hz:

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

Create a TimeSeries that contains this data and its corresponding time, so that

```
ts.plot()
```

gives this:

```{code-cell} ipython3
:tags: [remove-input]

import kineticstoolkit.lab as ktk

# Create the TimeSeries
ts = ktk.TimeSeries()

# Assign the time
ts.time = np.arange(100)/100

# Assign the position
ts = ts.add_data("Position", p)

# Add the position unit
ts = ts.add_info("Position", "Unit", "m")

ts.plot()
```

```{code-cell} ipython3
:tags: [hide-cell]

import kineticstoolkit.lab as ktk

# Create the TimeSeries
ts = ktk.TimeSeries()

# Assign the time
ts.time = np.arange(100)/100

# Assign the position
ts = ts.add_data("Position", p)

# Add the position unit
ts = ts.add_info("Position", "Unit", "m")

ts.plot()
```

