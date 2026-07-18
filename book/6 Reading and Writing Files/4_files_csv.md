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

# Reading/writing CSV files


# Reading CSV files

To ensure great compatibility between Kinetics Toolkit and other frameworks, TimeSeries can be converted from and to Pandas {{pd_dataframe}} using the {{ktk_timeseries_from_dataframe}} and {{ktk_timeseries_to_dataframe}} methods. Therefore, as long as a data file can be opened in Pandas, it can then be converted to a TimeSeries, as shown in {numref}`fig_ktk_dataflow`.

Comma Separated Values (CSV) files are ubiquitous in research. They are text files where values are separated usually by commas, but sometimes by other delimiters such as `;` or tabs. The first line often contains labels to indicate the nature of each column. Here is the content of a typical CSV file:

```
    Time,Force,Position
    0,0,0
    0.1,0,0.01
    0.2,0,0.02
    0.3,0,0.03
    0.4,0.3,0.04
    0.5,0.5,0.05
    0.6,0.6,0.06
    0.7,0.5,0.07
    0.8,0.3,0.08
    0.9,0,0.09
    1,0,0.1
```

First, we will read it as a DataFrame using {{pd_read_csv}}:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import pandas as pd

df = pd.read_csv(
    ktk.doc.download("timeseries_dataframe_example1.csv"),
    index_col="Time",
)

df
```

:::{important}
Note the use of the `index_col` parameter. This is the name of the column that corresponds to time. It is always required to correctly convert the DataFrame to a TimeSeries.
:::

We now convert the DataFrame to a TimeSeries:

```{code-cell} ipython3
ts = ktk.TimeSeries.from_dataframe(df)

ts.plot()
```


### Importing multidimensional data

In the first example, the force sensor was unidimensional; however, for a tridimensional force sensor, we would expect three signals (x, y, z). In this new example, we will import the following CSV file:

```
    Time,Fx,Fy,Fz,Position
    0,0,-9.81,0,0
    0.1,0,-9.81,0,0.01
    0.2,0,-9.81,0,0.02
    0.3,0,-9.81,0,0.03
    0.4,0.3,-9.81,1.5,0.04
    0.5,0.5,-9.81,2.5,0.05
    0.6,0.6,-9.81,3,0.06
    0.7,0.5,-9.81,2.5,0.07
    0.8,0.3,-9.81,1.5,0.08
    0.9,0,-9.81,0,0.09
    1,0,-9.81,0,0.1
```

We first read the CSV file as a DataFrame:

```{code-cell} ipython3
df = pd.read_csv(
    ktk.doc.download("timeseries_dataframe_example2.csv"),
    index_col="Time",
)

df
```

Then we import this DataFrame as a TimeSeries:

```{code-cell} ipython3
ts = ktk.TimeSeries.from_dataframe(df)

ts.data
```

The CSV file was correctly read as a TimeSeries. However, force components are scattered into three separate arrays. Would it be possible to read it as one Nx3 array instead?

To this effect, simply rename the columns of the DataFrame, either in the original CSV file or after reading it, using index brackets as it would be accessed in the resulting array:

```{code-cell} ipython3
df.columns = ["Forces[:,0]", "Forces[:,1]", "Forces[:,2]", "Position"]

df
```

We can now import this new DataFrame as a TimeSeries, with the three force signals combined in one Nx3 array:

```{code-cell} ipython3
ts = ktk.TimeSeries.from_dataframe(df)

ts.data
```

```{code-cell} ipython3
ts.data["Forces"]
```

For series of arrays with more than one dimension, the brackets would have multiple indexes. For example, a series of Nx4x4 homogeneous matrices would require 16 columns and the indexes would go from [0,0] to [3,3].


## Writing CSV files

To export a TimeSeries to a CSV file, we do the opposite sequence. We first convert the TimeSeries to a DataFrame, then we use the DataFrame's {{dataframe_to_csv}} method to create a CSV file.

In this example, we read some 3D marker positions from a sample C3D file and export these positions as a CSV file. Let's first download and read a sample C3D file. This file is provided by https://www.c3d.org as a test suite for C3D software development. For conciseness, we will only keep the following markers: "RFT1" and "RFT2".

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import pandas as pd

filename = ktk.doc.download("c3d_test_suite_sample.c3d")
c3d_contents = ktk.read_c3d(filename, convert_point_unit=True)
markers = c3d_contents["Points"].get_subset(["RFT1", "RFT2"])

markers
```

```{code-cell} ipython3
markers.data
```

To convert this TimeSeries to a CSV file, we first create a DataFrame:

```{code-cell} ipython3
df = markers.to_dataframe()

df
```

Then we export this DataFrame to a CSV file. Let's print the first 3 lines of this file:

```{code-cell} ipython3
df.to_csv("output.csv", index_label="Time")
```

Here are the first lines of the exported CSV file, ready to be processed in another software:

```{code-cell} ipython3
:tags: [remove-input]

!head -5 output.csv
```

