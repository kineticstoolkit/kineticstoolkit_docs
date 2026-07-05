---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.6
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Reading/writing C3D files

## Reading C3D files

Let's first download a sample C3D file:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

filename = ktk.doc.download("c3d_sample.c3d")
```

We read it using {{ktk_read_c3d}}:

```{code-cell} ipython3
c3d_contents = ktk.read_c3d(filename)

c3d_contents
```

:::{caution}
As indicated in the warning above, the points in this file are expressed in millimetres; however, Kinetics Toolkit uses SI units and therefore metres by default. The point positions have been converted to metres by default, and therefore you can ignore this warning, or suppress it altogether using:

```
c3d_contents = ktk.read_c3d(filename, convert_point_unit=True)
```

You can generally ignore this warning if you read unprocessed marker positions and analog signals.

You should not ignore this warning if you are reading a C3D file that has been processed by some software or pipeline to calculate joint kinetics, powers, etc., and if these values are expressed as "points" in the C3D. Consult the help of {{ktk_read_c3d}} for more details.
:::

The content of the file is expressed as a dictionary with two keys:
- `Points`: A TimeSeries that contains the point data (markers)
- `Analogs` (only when applicable): A TimeSeries that contains the raw analog data from force platforms, EMG, or other analog signals recorded into the C3D file.
- `ForcePlatforms` (only when applicable): A TimeSeries that contains the forces, moments, centres of pressure, and force platform positions.

### Points

Each data key of the Points TimeSeries corresponds to one point (marker):

```{code-cell} ipython3
c3d_contents["Points"].data
```

We will learn how to visualize these markers using an interactive player in [](../8%20Performing%203D%20Movement%20Analyses/1_player.md). For now, let's plot some of them:

```{code-cell} ipython3
c3d_contents["Points"].plot(["c7", "r should"])
```

### Analogs

Each data key of the Analogs TimeSeries corresponds to one analog signal:

```{code-cell} ipython3
c3d_contents["Analogs"].data
```

Let's plot some of them:

```{code-cell} ipython3
c3d_contents["Analogs"].plot(["Left Rectus femoris", "Left Semimembranosus"])
```

### Force platforms

The `ForcePlatforms` TimeSeries contains information regarding all force platforms in the file. In this particular file, there are 6 force platforms, represented as FP0 to FP5:
- The position of the force platforms is given by `FPx_Corner1` to `FPx_Corner4`.
- Their local coordinate systems are given by the `FPx_LCS` transform series.
- Ground reaction forces are given by `Forces`.
- Moments are reported both around the force platform geometrical centre (`FPx_MomentAtCentre`) and at the point of pressure (`FPx_MomentAtCOP`).
- The centre of pressure is reported in `FPx_COP`.

```{code-cell} ipython3
c3d_contents["ForcePlatforms"].data
```

Let's plot the COP on force plates 0:

```{code-cell} ipython3
c3d_contents["ForcePlatforms"].plot('FP0_COP')
```

### Quick visualization

Although visualizing data using the interactive 3D {{ktk_player}} is explained in section [](../8%20Performing%203D%20Movement%20Analyses/1_player.md), here is how we can quickly visualize the kinematic and kinetic data in this file. Note that every TimeSeries provided to the Player must have the same sampling rate, which means we need to downsample the force platform data to the points sampling rate:

```{code-cell} ipython3
:tags: [skip-execution]

ktk.Player(
    c3d_contents["Points"],
    c3d_contents["ForcePlatforms"].resample(c3d_contents["Points"].time)
)
```

```{code-cell} ipython3
:tags: [remove-input]

%matplotlib qt5

points = c3d_contents["Points"].get_ts_between_times(3, 5)
ktk.Player(
    points,
    c3d_contents["ForcePlatforms"].resample(points.time)
)._to_animation()
```


## Writing C3D files

Writing a new C3D file is done using {{ktk_write_c3d}}. In this example, suppose that we forgot to zero the force plates before recording, and our workflow requires that the input C3D file has zeroed vertical forces. We will open this C3D file as in the previous section, correct the analog signals, and then save a new C3D file.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

filename = ktk.doc.download("c3d_test_suite_sample.c3d")
c3d_contents = ktk.read_c3d(filename, convert_point_unit=True)

points = c3d_contents["Points"]
analogs = c3d_contents["Analogs"]
```

Let's take a look at the forces:

```{code-cell} ipython3
analogs.plot(["FZ1", "FZ2"])
```

There are some offsets in these signals that could be corrected by subtracting the median of the signal:

```{code-cell} ipython3
analogs.data["FZ1"] -= np.median(analogs.data["FZ1"])
analogs.data["FZ2"] -= np.median(analogs.data["FZ2"])

analogs.plot(["FZ1", "FZ2"])
```

Much better. To save these corrected data as a new C3D file, we use {{ktk_write_c3d}}:

```{code-cell} ipython3
ktk.write_c3d("corrected.c3d", points=points, analogs=analogs)
```
