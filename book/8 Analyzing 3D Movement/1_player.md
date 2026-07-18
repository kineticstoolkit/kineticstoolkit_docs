---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Visualizing points, vectors and transforms in 3D

In this chapter, we will use the {{ktk_kinematics}} module to process real acquisitions of 3D markers, calculate a series of joint angles, and reconstruct virtual markers using different methods such as calibration markers or probing.

Before calculating kinematics, we will learn how to use the {{ktk_player}} to visualize points, transforms (e.g., local coordinate systems), and forces (or other vectors) in three dimensions.

![](_static/images/frontpage.gif)

## Player Basics

:::{note}
The Player is an interactive class that needs an interactive Matplotlib backend. See section [](../../1%20Getting%20Started/2_getting_started_installing.md) for more information.
:::

In this section, we will use kinematic data of [tennis serves](../../5%20Appendix/dataset_kinematics_tennis_serve.md) as a [TimeSeries](../5%20Manipulating%20TimeSeries/2_timeseries.md) of marker positions.

```{code-cell} ipython3
%matplotlib agg

import kineticstoolkit.lab as ktk

# Download and read markers from a sample C3D file
filename = ktk.doc.download("kinematics_tennis_serve_2players.c3d")
markers = ktk.read_c3d(filename)["Points"]
```

To visualize these markers, we instantiate a {{ktk_player}} using one of these methods:

```
p = ktk.Player(markers)

# or

p = ktk.Player()
p.set_contents(markers)
```

Then we can start playback by pressing `space bar`, or using:

```
p.play()
```

```{code-cell} ipython3
:tags: [remove-input]

p = ktk.Player()
p.set_contents(markers.get_ts_between_times(6, 8))
p._to_animation()
```

Press `h` to print a help overlay on how to control the Player using the keyboard:

```{code-cell} ipython3
:tags: [remove-input]

print(ktk.player.HELP_TEXT)
```

Note the coloured global reference frame on the bottom. This reference frame and every other follow the same standard colour scheme:

- x = Red
- y = Green
- z = Blue

Once a player has been instantiated, many properties can be modified to control or customize it:

```{code-cell} ipython3
p
```

We will learn how to use these properties in the following sections.

:::{note}
Every property can be set directly at creation time, for example:

```
p = ktk.Player(markers, up="z", anterior="-y")
```
:::

## Orienting the data

We clearly see that these data do not match the orientation of the Player's ground plane. In these data, the vertical axis is z, and the antero-posterior axis is y, pointing backward. To align the Player correctly to the data:

```{code-cell} ipython3
p.up = "z"
p.anterior = "-y"
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

## Setting the viewpoint

Use the mouse to change the viewpoint interactively.

In addition, once the Player is correctly aligned to the data, we can set the viewpoint using the keyboard (numbers 1-6) or {{ktk_player_set_view}}:

```{code-cell} ipython3
p.set_view("front")
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

```{code-cell} ipython3
p.set_view("top")
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

To revert to the initial view (at the instantiation of the Player):

```{code-cell} ipython3
p.set_view("initial")
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

It is also possible to set a custom viewpoint, using these properties (some of them are illustrated in {numref}`fig_player_view_point`):
- `target`: where the camera looks
- `azimuth`: from what angle in the transverse plane
- `elevation`: from what angle relative to the transverse plane
- `pan`: panning in (x, y), in the camera's point of view
- `zoom`: zoom, in the camera's point of view

:::{figure}
:label: fig_player_view_point
:width: 4.5in
![Player custom viewpoint](_static/images/player_view_point.png)

Visual representation of `target`, `azimuth` and `elevation`.
:::

For example:

```{code-cell} ipython3
p.target = (0.0, 0.0, 1.0)
p.azimuth = 3.1416 / 4  # pi/4 = 45 deg
p.elevation = 3.1416 / 6  # pi/6 = 30 deg
p.zoom = 0.75
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```


## Interconnecting points

To interconnect points, we use the `interconnections` property of the Player, which is a dict that follows this form:

:::{figure}
:label: fig_player_interconnections
:width: 5in
![Player custom viewpoint](_static/images/player_interconnections.png)

Interconnection dictionary.
:::

For example, to interconnect Derrick's right lower limb, we would do:

```{code-cell} ipython3
# Name "RLowerLimb" is arbitrary, anything would do.
p.interconnections["RLowerLimb"] = {"Links": [
    ["Derrick:RTOE", "Derrick:RHEE", "Derrick:RANK", "Derrick:RTOE"], # Feet
    ["Derrick:RANK", "Derrick:RKNE"], # Shank
    ["Derrick:RKNE", "Derrick:RPSI", "Derrick:RASI", "Derrick:RKNE"]  # Thigh
]}  
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

Let's assign a red colour to this side, and do the same in blue for the left side.

```{code-cell} ipython3
p.interconnections["RLowerLimb"]["Color"] = "r"
p.interconnections["LLowerLimb"] = {"Links": [
    ["Derrick:LTOE", "Derrick:LHEE", "Derrick:LANK", "Derrick:LTOE"], # Feet
    ["Derrick:LANK", "Derrick:LKNE"], # Shank
    ["Derrick:LKNE", "Derrick:LPSI", "Derrick:LASI", "Derrick:LKNE"]  # Thigh
], "Color": "b"}
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

### Wildcards

To draw links for both Viktor and Derrick, we could repeat the same code by replacing every occurrence of "Derrick:" with "Viktor:". However, we can also use wildcards (`*`), which is much more convenient. A wildcard means "assign any name in place of `*`". We may choose to use wildcards as a prefix or as a suffix. Here, we use it as a prefix, for every body segment:

```{code-cell} ipython3
p.interconnections["LLowerLimb"] = {
    "Color": "b",
    "Links": [  # List of lines that span lists of markers
        ["*LTOE", "*LHEE", "*LANK", "*LTOE"],
        ["*LANK", "*LKNE"],
        ["*LKNE", "*LPSI", "*LASI", "*LKNE"],
    ],
}

p.interconnections["RLowerLimb"] = {
    "Color": "r",
    "Links": [
        ["*RTOE", "*RHEE", "*RANK", "*RTOE"],
        ["*RANK", "*RKNE"],
        ["*RKNE", "*RPSI", "*RASI", "*RKNE"],
    ],
}

p.interconnections["LUpperLimb"] = {
    "Color": (0.0, 0.5, 1.0),
    "Links": [
        ["*LSHO", "*LELB", "*LWRA", "*LFIN"],
        ["*LELB", "*LWRB", "*LFIN"],
        ["*LWRA", "*LWRB"],
    ],
}

p.interconnections["RUpperLimb"] = {
    "Color": (1.0, 0.5, 0.0),
    "Links": [
        ["*RSHO", "*RELB", "*RWRA", "*RFIN"],
        ["*RELB", "*RWRB", "*RFIN"],
        ["*RWRA", "*RWRB"],
    ],
}

p.interconnections["Head"] = {
    "Color": (1.0, 0.5, 1.0),
    "Links": [
        ["*C7", "*LFHD", "*RFHD", "*C7"],
        ["*C7", "*LBHD", "*RBHD", "*C7"],
        ["*LBHD", "*LFHD"],
        ["*RBHD", "*RFHD"],
    ],
}

p.interconnections["TrunkPelvis"] = {
    "Color": (0.5, 1.0, 0.5),
    "Links": [
        ["*LASI", "*STRN", "*RASI"],
        ["*STRN", "*CLAV"],
        ["*LPSI", "*T10", "*RPSI"],
        ["*T10", "*C7"],
        ["*LASI", "*LSHO", "*LPSI"],
        ["*RASI", "*RSHO", "*RPSI"],
        ["*LPSI", "*LASI", "*RASI", "*RPSI", "*LPSI"],
        ["*LSHO", "*CLAV", "*RSHO", "*C7", "*LSHO"],
    ],
}
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```


## Visualizing transforms (rigid bodies)

The Player can also draw rigid bodies represented by [homogeneous transform series (Nx4x4)](../3%20Performing%203D%20Geometrical%20Operations/geometry_transforms.md). For instance, let's create two series of transforms that revolve around the x and z axes:

```{code-cell} ipython3
:tags: [remove-output]

import numpy as np
import kineticstoolkit.lab as ktk

# Create a TimeSeries with two rotating transforms
transforms = ktk.TimeSeries(time=np.linspace(0, 5, 100))

transforms.data["RotationAroundX"] = ktk.geometry.create_transform_series(
    angles=np.linspace(0, 2 * np.pi, 100),
    positions=[[0.2, 0.0, 0.0]],
    seq="x",
)

transforms.data["RotationAroundZ"] = ktk.geometry.create_transform_series(
    angles=np.linspace(0, 2 * np.pi, 100),
    positions=[[0.0, 0.0, 0.2]],
    seq="z",
)

# Show these frames in the Player
p = ktk.Player(transforms)
```

```{code-cell} ipython3
:tags: [remove-input]

p.azimuth = 0.8
p.elevation = 0.16
p.zoom = 10
p._to_animation()
```



## Visualizing forces and other vectors

In addition to points and frames (local coordinate systems), the {{ktk_player}} can represent forces or other vectors using its `vectors` property.

We start by loading a gait c3d file.

```{code-cell} ipython3
:tags: [remove-output]

import kineticstoolkit.lab as ktk
import numpy as np

contents = ktk.read_c3d(
    ktk.doc.download("c3d_sample.c3d"), convert_point_unit=True
)

p = ktk.Player(contents["Points"])
```

```{code-cell} ipython3
:tags: [remove-input]

points = contents["Points"].get_ts_between_times(3, 5.5)
# force_platforms = force_platforms.get_ts_between_times(3, 5.5)
p = ktk.Player(points)
p.zoom = 1.628894626777442
p.azimuth = 0.688
p.elevation = 0.26
p.pan = (-0.4663898987149148, -0.3352733755899471)
p._to_animation()
```

Let's add a vector at the right shoulder, which could, for example, represent the joint reaction force. For now, we will simply create a dummy sinusoidal vector:

```{code-cell} ipython3
forces = ktk.TimeSeries(time=contents["Points"].time)
forces.data["ShoulderForce"] = 500 * ktk.geometry.create_vector_series(
    y=np.sin(3 * forces.time)
)
```

Now we create a new Player that shows both points and forces:

```{code-cell} ipython3
:tags: [skip-execution]

p = ktk.Player(contents["Points"], forces)
```

```{code-cell} ipython3
:tags: [remove-input]

points = contents["Points"].get_ts_between_times(3, 5.5)
forces = forces.get_ts_between_times(3, 5.5)
p = ktk.Player(points, forces)
p.zoom = 1.628894626777442
p.azimuth = 0.688
p.elevation = 0.26
p.pan = (-0.4663898987149148, -0.3352733755899471)
p._to_animation()
```

The force is not shown yet because the Player does not know how to represent the vector "ShoulderForce". This is configured by the Player's `vectors` property, which is a dict where:
- The key is the name of the force. Here, "ShoulderForce".
- The value is a dict with:
    - "Origin": The name of the point the vector originates from. Here, "r should", as read from the C3D file.
    - "Scale": Optional, the scale of the vector in meters per vector unit. It is 1 by default, but here we will set 0.001, which means in this case that the line will be one millimetre per newton.
    - "Color": Optional, an RGB colour tuple.

To show the shoulder force:

```{code-cell} ipython3
p.vectors["ShoulderForce"] = {"Origin": "r should", "Scale": 0.001}
```

```{code-cell} ipython3
:tags: [remove-input]

p._to_animation()
```

### Force platforms

The previous section was a dummy example to show how to represent vectors in the Player. In this same file, we also have force platform contents. For visualization, we need to downsample it so that everything is on the same sampling rate:

```{code-cell} ipython3
points = contents["Points"]
force_platforms = contents["ForcePlatforms"].resample(points.time)
```

We can now visualize the points and force platform data in the Player:

```{code-cell} ipython3
:tags: [skip-execution]

p = ktk.Player(points, force_platforms)
```

```{code-cell} ipython3
:tags: [remove-input]

points = contents["Points"].get_ts_between_times(3, 5.5)
force_platforms = (
    contents["ForcePlatforms"]
    .resample(points.time)
    .get_ts_between_times(3, 5.5)
)
p = ktk.Player(points, force_platforms)
p.zoom = 1.628894626777442
p.azimuth = 0.688
p.elevation = 0.26
p.pan = (-0.4663898987149148, -0.3352733755899471)
p._to_animation()
```

As we see, the Player draws the platforms and the ground reaction forces by default, based on the default value of its `interconnections` and `vector` properties.

```{code-cell} ipython3
p.interconnections
```

```{code-cell} ipython3
p.vectors
```

In these values, wildcards `*` are used to mean:
- Any point ending with `_Corner1` is connected to a matching point ending with `_Corner2`;
- Any point ending with `_Corner2` is connected to a matching point ending with `_Corner3`;
- etc.
- Any vector ending with `Force` is connected to a matching point ending with `COP`.

