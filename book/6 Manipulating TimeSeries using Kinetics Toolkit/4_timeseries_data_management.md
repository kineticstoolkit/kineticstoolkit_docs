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


# Adding, renaming, and removing data, reconstructing missing data

This section shows how to use these methods for data management:

- {{ktk_timeseries_add_data}}
- {{ktk_timeseries_rename_data}}
- {{ktk_timeseries_remove_data}}
- {{ktk_timeseries_get_subset}}
- {{ktk_timeseries_merge}}

We will use this sample [kinematic acquisition](../../5%20Appendix/dataset_kinematics_tennis_serve.md) of 39 bilateral markers with 1092 samples recorded at 50 Hz during tennis serve:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

markers = ktk.read_c3d(ktk.doc.download("kinematics_tennis_serve.c3d"))[
    "Points"
]
```

## Adding data

The TimeSeries loaded above has many markers, which makes lots of data to visualize and process:

```{code-cell} ipython3
markers.plot()
```

+++ {"jp-MarkdownHeadingCollapsed": true}

To keep only the data we need, it is often practical to make a copy of the TimeSeries with no data using {{ktk_timeseries_copy}}, and selectively add the data we need using {{ktk_timeseries_add_data}}:

```{code-cell} ipython3
# Copy the TimeSeries without its data
selected_markers = markers.copy(copy_data=False)

# Add the markers to this new TimeSeries
for key in ["Derrick:C7", "Derrick:T10", "Derrick:STRN", "Derrick:CLAV"]:
    selected_markers = selected_markers.add_data(key, markers.data[key])

selected_markers.plot()
```

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

## Subsetting

As a shortcut method, we can also use {{ktk_timeseries_get_subset}}, which returns a TimeSeries with only a selection of data keys:

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

Using {{ktk_timeseries_merge}} has several other benefits, such as merging events, information, and even resample TimeSeries that may have been recorded at different sampling rates.


## Missing data

This section shows how to use these methods:

- {{ktk_timeseries_isnan}}
- {{ktk_timeseries_fill_missing_samples}}

It happens regularly that we record suboptimal data, which may include missing samples. For instance, in [these kinematic data of tennis serve](../../5%20Appendix/dataset_kinematics_tennis_serve.md), the marker on the right shoulder dissapears regularly:

```{code-cell}
import kineticstoolkit.lab as ktk
import numpy as np


filename = ktk.doc.download("kinematics_tennis_serve_nan.c3d")
markers = ktk.read_c3d(filename)["Points"]
markers.plot("Derrick:RSHO")
```


### Finding missing samples

Similarly to NumPy's {{np_isnan}} function, TimeSeries provide the {{ktk_geometry_isnan}} method that returns which samples are missing as a list of bool:

```{code-cell}
is_missing = markers.isnan("Derrick:RSHO")
```

Using {{np_nonzero}}, the list of missing indexes is:

```{code-cell}
np.nonzero(is_missing)
```

### Filling missing samples

If the gaps are not too wide, we can fill these gaps using {{ktk_timeseries_fill_missing_samples}}:

```{code-cell}
filled_markers = markers.fill_missing_samples(
    max_missing_samples=20
)

filled_markers.plot("Derrick:RSHO")
```

We see in the figure above that any gap larger than 20 samples has been left untouched. It is always a good idea to set such as maximal gap according to the sampling rate and movement being recorded, so that we do not interpolate too much and create invalid data.

Now, look at the blue curve. The default linear interpolation method was not optimal for these data, as it introduces obvious discontinuities in the signal. We may opt for another method, such as a cubic spline:

```{code-cell}
filled_markers = markers.fill_missing_samples(
    max_missing_samples=20,
    method="cubic",
)

filled_markers.plot("Derrick:RSHO")
```

