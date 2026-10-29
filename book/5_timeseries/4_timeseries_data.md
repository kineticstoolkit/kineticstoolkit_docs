---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Adding, removing and renaming data

This section shows how to use these methods for data manipulation:

|                                |                               |
| ------------------------------ | ----------------------------- |
| {{ktk_timeseries_add_data}}    | {{ktk_timeseries_get_subset}} |
| {{ktk_timeseries_remove_data}} | {{ktk_timeseries_merge}}      |
| {{ktk_timeseries_rename_data}} |                               |

We will use this sample of 39 bilateral markers with 1092 samples recorded at 50 Hz during tennis serve:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt
import numpy as np

markers = ktk.read_c3d(ktk.doc.download("kinematics_tennis_serve.c3d"))[
    "Points"
]
```


## Adding data

The TimeSeries loaded above has many markers, which makes lots of data to visualize and process; we even get a warning that not all lines have been plotted.

```{code-cell} ipython3
markers.plot()
```

To keep only the data we need, one method is to make a copy of the TimeSeries with no data using {{ktk_timeseries_copy}}, and then selectively add the data we need using {{ktk_timeseries_add_data}}:

```{code-cell} ipython3
# Copy the TimeSeries without its data
selected_markers = markers.copy(copy_data=False)

# Add the markers to this new TimeSeries
for key in ["Derrick:C7", "Derrick:T10", "Derrick:STRN", "Derrick:CLAV"]:
    selected_markers = selected_markers.add_data(key, markers.data[key])

selected_markers.plot()
```

:::{tip} Direct assignment
This line:

```python
    selected_markers = selected_markers.add_data(key, markers.data[key])
```

could be replaced by a direct assignment:

```python
    selected_markers.data["key"] = markers.data["key"]
```

However, it is often a good idea to use {{ktk_timeseries_add_data}} since it also performs dimension checks, while no check is performed with direct assignments.
:::

:::{tip} Modifying the TimeSeries in place
This line:

```python
    selected_markers = selected_markers.add_data(key, markers.data[key])
```

creates a new TimeSeries each time it is called. This is a design choice to prevent user errors: working on a copy of a TimeSeries is always safer because it always keeps the original one intact. However, it may be a performance hit with very large TimeSeries.

Most TimeSeries methods have an "in_place" argument that explicitly instruct to modify the original TimeSeries instead of creating a new one. Use it when performance is an issue:

```python
    selected_markers.add_data(key, markers.data[key], in_place=True)
```

:::


## Removing data

We could do the same by removing the superfluous data from the TimeSeries, using {{ktk_timeseries_remove_data}}:

```{code-cell} ipython3
# Copy the whole TimeSeries, with all data
selected_markers = markers.copy()

# Delete the unwanted markers from this new TimeSeries
for key in markers.data:
    if key not in ["Derrick:C7", "Derrick:T10", "Derrick:STRN", "Derrick:CLAV"]:
        selected_markers = selected_markers.remove_data(key)

selected_markers.plot()
```

As a shortcut method, you can also use {{ktk_timeseries_get_subset}}, which returns a TimeSeries with only a selection of data keys:

```{code-cell} ipython3
selected_markers = markers.get_subset(
    [
        "Derrick:C7",
        "Derrick:T10",
        "Derrick:STRN",
        "Derrick:CLAV",
    ],
)

selected_markers.plot()
```

## Renaming data

Use the {{ktk_timeseries_rename_data}} to change the name of a data key:

```{code-cell} ipython3
selected_markers = selected_markers.rename_data("Derrick:C7", "C7")
selected_markers = selected_markers.rename_data("Derrick:T10", "T10")
selected_markers = selected_markers.rename_data("Derrick:STRN", "Sternum")
selected_markers = selected_markers.rename_data("Derrick:CLAV", "Clavicular")

selected_markers.plot()
```

## Merging data

Let say we have two different TimeSeries, one for the left lower limb and one for the right one:

```{code-cell} ipython3
left_lower_limb = markers.get_subset(
    [
        "Derrick:LANK",
        "Derrick:LHEE",
        "Derrick:LKNE",
        "Derrick:LTOE",
    ]
)

right_lower_limb = markers.get_subset(
    [
        "Derrick:RANK",
        "Derrick:RHEE",
        "Derrick:RKNE",
        "Derrick:RTOE",
    ]
)

plt.subplot(1,2,1)
left_lower_limb.plot(legend=False)
plt.subplot(1,2,2)
right_lower_limb.plot(legend=False)
```

To merge these TimeSeries, we could simply use the {{ktk_timeseries_add_data}} method as we did above:

```{code-cell} ipython3
merged = left_lower_limb.copy()

for key in right_lower_limb.data:
    merged = merged.add_data(key, right_lower_limb.data[key])

merged.plot(legend=False)
```

As a shortcut method, we can also use {{ktk_timeseries_merge}}:

```{code-cell} ipython3
merged = left_lower_limb.merge(right_lower_limb)

merged.plot(legend=False)
```

Using {{ktk_timeseries_merge}} has several other benefits, such as merging events, information, and even optionally resample TimeSeries that may have been recorded at different sampling rates.

