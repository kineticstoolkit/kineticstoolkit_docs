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

# TimeSeries

A TimeSeries is a single container that holds time, data, events and general info. Let's load an example:

```{code-cell}
import kineticstoolkit.lab as ktk


filename = ktk.doc.download("timeseries_example.json.zip")
ts = ktk.load(filename)

ts.plot()
```

Here are the different elements of a TimeSeries:

```{code-cell}
ts
```


## Time

A TimeSeries always includes a time property, which is shared across every data. Time is stored as a unidimensional NumPy array.

```{code-cell}
ts.time
```

## Data

A TimeSeries can contain any number of signals contained in its `data` dictionary, each being stored as a NumPy array. Signals can have any dimensions, but the first axis always corresponds to time. In this TimeSeries, we have two signals of shape 5000x4, which are 5000 recordings of forces and moments expresses as Nx4 series:

$$
\text{Forces} = \begin{bmatrix}
F_x(0) & F_y(0) & F_z(0) & 0 \\
F_x(1) & F_y(1) & F_z(1) & 0 \\
F_x(2) & F_y(2) & F_z(2) & 0 \\
... & ... & ... & ... \\
F_x(4999) & F_y(4999) & F_z(4999) & 0
\end{bmatrix}
$$

$$
\text{Moments} = \begin{bmatrix}
M_x(0) & M_y(0) & M_z(0) & 0 \\
M_x(1) & M_y(1) & M_z(1) & 0 \\
M_x(2) & M_y(2) & M_z(2) & 0 \\
... & ... & ... & ... \\
M_x(4999) & M_y(4999) & M_z(4999) & 0
\end{bmatrix}
$$

```{code-cell}
ts.data
```

## Events

A TimeSeries may contain events, each defined by a time and a name. Events can share a same name, which is expected in cyclic data.

```{code-cell}
ts.events
```

## Info

A TimeSeries also stores optional information on its contents, such as units. The `info` dictionary is addressed using two nested keys: the first (outer) one is generally what the information refers to (e.g., "Time", "Forces", "LateralFemoralEpicondyleR", "Speed"), and the second (inner) one defines the nature of the information (e.g., "Unit", "Date", "Name").

```{code-cell} ipython3
ts.info
```

Unless explicitly mentioned, theses metadata are not used for calculation and are strictly optional. "Unit" info is however used by {{ktk_timeseries_plot}} to plot the units, as seen above.

