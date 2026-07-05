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


# Creating point/vector/transform series in Kinetics Toolkit


## Series of numbers (float, int)

Since a float or an integer has no dimension, a **series** of N floats or integers has one dimension of length N:

    [x(t0), x(t1), x(t2), ...]

A series of numbers, e.g., a series of angles, is created directly as an array:

```{code-cell}
float_series = np.array([0.0, 0.1, 0.2])
```


## Constants

In Kinetics Toolkit, numbers, points, vectors, and transforms are expressed as series, where the first dimension of any series corresponds to time.

Therefore, a vector $[1, 2, 3, 0]$ must be expressed as `[[1.0, 2.0, 3.0, 0.0]]` (note the double brackets), because expressing it as `[1.0, 2.0, 3.0, 0.0]` instead (single brackets) would mean a series of 4 floats.

A quick way to convert a constant array to a series is to use {{np_newaxis}}:

```{code-cell} ipython3
one_vector = np.array([1.0, 2.0, 3.0, 0.0])
series_of_one_vector = one_vector[np.newaxis]
```


## Series of points/vectors

Since a point has four coordinates (x, y, z, 1), then a **series** of N points has a shape of (N, 4):

```python
    [
        [x(t0), y(t0), z(t0), 1.0],
        [x(t1), y(t1), z(t1), 1.0],
        [x(t2), y(t2), z(t2), 1.0],
        [ ... ,  ... ,  ... , ...],
    ]
```

The functions {{ktk_geometry_create_point_series}} and {{ktk_geometry_create_vector_series}} creates such point/vector series using different forms:

### Using multiple arrays

In this case, the arguments `x`, `y`, and `z` accept arrays of floats:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ktk.geometry.create_point_series(
    x=[1.0, 2.0, 3.0], y=[4.0, 5.0, 6.0], z=[7.0, 8.0, 9.0]
)
```

```{code-cell}
ktk.geometry.create_vector_series(
    x=[1.0, 2.0, 3.0], y=[4.0, 5.0, 6.0], z=[7.0, 8.0, 9.0]
)
```

### Using a single array

The default argument accepts an array of NxM where M could be:
- M=1: N × [x]
- M=2: N × [x, y]
- M=3: N × [x, y, z]
- M=4: N × [x, y, z, 1] or N × [x, y, z, 0]:

```{code-cell} ipython3
ktk.geometry.create_point_series(
    [
        [0.0, 0.0, 5.0],
        [0.1, 0.0, 5.0],
        [0.2, 0.0, 5.0],
        [0.3, 0.0, 5.1],
    ]
)
```

```{code-cell} ipython3
ktk.geometry.create_vector_series(
    [
        [0.0, 0.0, 5.0],
        [0.1, 0.0, 5.0],
        [0.2, 0.0, 5.0],
        [0.3, 0.0, 5.1],
    ]
)
```


### Series of constant values

Using the argument `length`, we can repeat a constant over `length` samples:

```{code-cell} ipython3
ktk.geometry.create_point_series([[1.0, 2.0, 3.0]], length=5)
```

```{code-cell} ipython3
ktk.geometry.create_vector_series([[1.0, 2.0, 3.0]], length=5)
```


## Series of transforms

Since a transform has a shape of (4, 4), then a **series** of N frames has a shape of (N, 4, 4):

    [
        [
            [R00(t0), R01(t0), R02(t0), px(t0)],
            [R10(t0), R11(t0), R12(t0), py(t0)],
            [R20(t0), R21(t0), R22(t0), pz(t0)],
            [    0.0,     0.0,     0.0,    1.0],
        ],
        [
            [R00(t1), R01(t1), R02(t1), px(t1)],
            [R10(t1), R11(t1), R12(t1), py(t1)],
            [R20(t1), R21(t1), R22(t1), pz(t1)],
            [    0.0,     0.0,     0.0,    1.0],
        ],
        ...
    ]


The function {{ktk_geometry_create_transform_series}} can create transforms using multiple input forms:

### Using rotation angles

We use this method when we already know the orientation angles. Real-life cases include expressing coordinate systems for an inclined surface, a turning wheel, etc.

:::{figure}
:label: fig_geometry_create_transform_series_angles
:width: 3in
![](_static/images/fig_geometry_create_transform_series_angles.png)

Creating transforms using rotation angles.
:::

In this case, pictured in {numref}`fig_geometry_create_transform_series_angles`, we create a transform based on a rotation of 30° around the z axis:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ktk.geometry.create_transform_series(
    angles=[30], seq="z", degrees=True, positions=[[0.15, 0.70, 0.0]]
)
```

We can also combine multiple rotations around multiple axes. For instance, for a rotation of 30° around z, followed by a rotation of 10° around x, followed by a rotation of 20° around y, we would use:

```{code-cell} ipython3
ktk.geometry.create_transform_series(
    angles=[[30.0, 10.0, 20.0]], seq="zxy", degrees=True
)
```

3D rotations will be discussed later in section [](6_geometry_angles.md) along with the importance of the rotation order.

### Using points (e.g. reflective markers)

We use this method to create transforms based on known positions such as markers affixed on bony landmarks as pictured in {numref}`fig_geometry_create_transform_series_points`.

In this case, we know the position of the shoulder, elbow, and wrist. We want to create a transform that has its y axis aligned with the shoulder-elbow line, and its z axis perpendicular to the shoulder-elbow-wrist plane.

:::{figure}
:label: fig_geometry_create_transform_series_points
:width: 3in
![](_static/images/fig_geometry_create_transform_series_points.png)

Creating transforms using points.
:::

We start by creating point series for the three markers. In a real-case scenario, this could be the trajectory of markers as read from a c3d file.

```{code-cell} ipython3
shoulder = ktk.geometry.create_point_series([[0.15, 0.70]])
elbow = ktk.geometry.create_point_series([[0.34, 0.37]])
wrist = ktk.geometry.create_point_series([[0.60, 0.15]])

print(f"Shoulder: {shoulder}")
print(f"Elbow: {elbow}")
print(f"Wrist: {wrist}")
```

The transform is then created using:

```{code-cell} ipython3
ktk.geometry.create_transform_series(
    y=shoulder - elbow,  # Direction of the y axis
    xy=wrist - elbow,  # Another vector in the xy plane, oriented ~toward z
    positions=shoulder,  # Origin
)
```

### Using quaternions (e.g., IMUs)

We use this method to create transforms based on the known 3D orientation of rigid bodies in space, expressed as quaternions. While a 3D rotation matrix requires nine numbers, a quaternion only requires four. It is therefore a more efficient way to express 3D rotations.

Due to this more efficient representation of the same operation, measurement systems often use this representation to communicate 3D orientations. This is the case with inertial measurement units (IMUs), and with rigid body orientations measured by optoelectronic systems such as Vicon (Tracker) or Optitrack (Motive).

:::{figure}
:label: fig_geometry_create_transform_series_quaternions
:width: 3in
![](_static/images/fig_geometry_create_transform_series_quaternions.png)

Creating transforms using quaternions.
:::

In this case, which is pictured in {numref}`fig_geometry_create_transform_series_quaternions`, the orientation of the arm's coordinate system is given by quaternion [0.0, 0.0, 0.259, 0.966]. To convert this quaternion and the position of the shoulder to its transform equivalent:

```{code-cell}
ktk.geometry.create_transform_series(
    quaternions=[[0.0, 0.0, 0.259, 0.966]], positions=[[0.15, 0.7]]
)
```


## 💪 Exercise 1

Using {{ktk_geometry_create_point_series}}, create a NumPy array that corresponds to the following trajectory:

$$
\vec{p}(t_0) = (3, 4, 5) \\
\vec{p}(t_1) = (4, 5, 5) \\
\vec{p}(t_2) = (5, 6, 5) \\
\vec{p}(t_3) = (6, 7, 5) \\
\vec{p}(t_4) = (7, 8, 5) \\
$$

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

p = np.array(
    [
        [3.0, 4.0, 5.0, 1.0],
        [4.0, 5.0, 5.0, 1.0],
        [5.0, 6.0, 5.0, 1.0],
        [6.0, 7.0, 5.0, 1.0],
        [7.0, 8.0, 5.0, 1.0],
    ]
)

# or

p = ktk.geometry.create_point_series(
    [[3, 4, 5], [4, 5, 5], [5, 6, 5], [6, 7, 5], [7, 8, 5]]
)

p
```


## 💪 Exercise 2

Using {{ktk_geometry_create_vector_array}}, create a NumPy array that corresponds to the following time-invariant vector:

$$
\vec{v} = (1, 2, 0)
$$

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

v = np.array([[1.0, 2.0, 0.0, 0.0]])

# or

v = ktk.geometry.create_vector_series([[1, 2, 0]])

v
```


## 💪 Exercise 3

In {numref}`fig_geometry_basics_exercise`, the position of the elbow in global coordinates is $(0.34, 0.371, 0)$. Therefore, the transform that expresses the position and incline of the forearm is:

$$
~^\text{global}_\text{forearm}T = \begin{bmatrix}
\cos(\theta) & -\sin(\theta) & 0 & 0.34 \\
\sin(\theta) & \cos(\theta) & 0 & 0.371 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Using {{ktk_geometry_create_transform_array}}, create a NumPy array that expresses the series of frames for a movement consisting of three inclines: 0°, 15°, and 25°.

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

frames = np.array(
    [
        [
            [np.cos(0.0), -np.sin(0.0), 0.0, 0.34],
            [np.sin(0.0), np.cos(0.0), 0.0, 0.371],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        [
            [np.cos(np.deg2rad(15.0)), -np.sin(np.deg2rad(15.0)), 0.0, 0.34],
            [np.sin(np.deg2rad(15.0)), np.cos(np.deg2rad(15.0)), 0.0, 0.371],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
        [
            [np.cos(np.deg2rad(25.0)), -np.sin(np.deg2rad(25.0)), 0.0, 0.34],
            [np.sin(np.deg2rad(25.0)), np.cos(np.deg2rad(25.0)), 0.0, 0.371],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ],
    ]
)

# or

frames = ktk.geometry.create_transform_series(
    angles=[0, 15, 25], degrees=True, seq="z", positions=[[0.34, 0.371]]
)

frames
```

