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

# Rotating and translating point/vector/transform series

We now know how to construct a transform, which is a 4x4 matrix that represents the position and orientation of a local coordinate system in respect to a reference coordinate system.

We learned that a transform always has this form:

$$
T =
\begin{bmatrix}
R_{11} & R_{12} & R_{13} & p_x \\
R_{21} & R_{22} & R_{23} & p_y \\
R_{31} & R_{32} & R_{33} & p_z \\
0      & 0      & 0      & 1
\end{bmatrix}
$$

where:

- $R$ is a function of three rotation angles and represents the orientation of the local coordinate system;
- $p$ is the position of the local coordinate system's origin.

In addition to representing positions and orientations, the same matrix can also represent rigid transformations such as translations and rotations, thus its name **homogeneous transform**. In this case:

- $R$ represents a rotation;
- $p$ is a translation.

Any coordinate (point, vector, or frame) that is multiplied by the homogeneous transform will be rotated by $R$ and translated by $p$:

$$
^\text{global} p_{\text{tranformed}} ~~~ = ~~~ T ~~~ ^\text{global} p_\text{initial}
$$

The following examples show how the same homogeneous transform can move either points, vectors, or frames.


## Moving points

Let's say we want to rotate the point located at (10, 0, 0) by 30 degrees around the origin's z-axis, then translate it 2 units to the right as shown in {numref}`fig_geometry_moving_points`.

```{figure}
:label: fig_geometry_moving_points
:width: 4in
![](_static/images/fig_geometry_moving_points.png)

Rotating and translating a point in respect to the global reference frame.
```

We first express the original coordinates of the point:

$$
^\text{global} p_\text{initial} =
\begin{bmatrix}
10 \\ 0 \\ 0 \\ 1
\end{bmatrix}
$$

We then express the rotation and translation that we want to apply to this point:

$$
T =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

We multiply the position by the transform to obtain the final position of the point:

$$
^\text{global} p_{\text{tranformed}} =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 10 \\ 0 \\ 0 \\ 1 \end{bmatrix} \\ =
\begin{bmatrix} 10\cos(30) + 2 \\ 10\sin(30) \\ 0 \\ 1 \end{bmatrix} =
\begin{bmatrix} 10.66 \\ 5 \\ 0 \\ 1 \end{bmatrix}
$$

The final coordinates of the point are (10.66, 5, 0).


### Application in Kinetics Toolkit

We can do the same in Kinetics Toolkit, using the function {{ktk_geometry_create_transform_series}}. The transform $T$ used in this section is created using:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

T = ktk.geometry.create_transform_series(
    angles=[30],
    degrees=True,
    seq="z",  # Which means a rotation around the z axis
    positions=[[2, 0, 0, 1]],  # 4th column
)

T
```

:::{caution}
Note that the `angles` and `positions` values are enclosed in brackets. This is because all functions in the {{ktk_geometry}} module work on series of data, and the first dimension is always reserved for time. Please consult [](2_geometry_series.md) for more information.
:::

The function {{ktk_geometry_matmul}} performs matrix multiplications on data series. It can therefore be used to obtain the solution to the previous examples.

```{code-cell} ipython3
ktk.geometry.matmul(T, [[10, 0, 0, 1]])
```

### Direct transformation in Kinetics Toolkit

Kinetics Toolkit's geometry module also provides simpler functions to perform basic geometry operations, such as {{ktk_geometry_rotate}}, {{ktk_geometry_translate}}, and {{ktk_geometry_scale}}. If we don't need to express a full homogeneous transform, then it is generally simpler to use these functions:

```{code-cell} ipython3
point = [[10, 0, 0, 1]]
rotated_point = ktk.geometry.rotate(point, seq="z", angles=[30], degrees=True)
final_point = ktk.geometry.translate(rotated_point, translations=[[2, 0, 0]])

final_point
```


## 💪 Exercise 1

The global coordinates of a point are:

$$
\vec{p} = (1, 2, 0)
$$

Using Kinetics Toolkit's geometry module, rotate this point anti-clockwise by 20° then translate it by one unit to the left.

a) Do this exercise by creating the corresponding homogeneous transform using {{ktk_geometry_create_transform_series}}, then by multiplying this transform by the point coordinates using {{ktk_geometry_matmul}}.

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

p = np.array([[1.0, 2.0, 0.0, 1.0]])
T = ktk.geometry.create_transform_series(
    angles=[20], degrees=True, seq="z", positions=[[-1.0, 0.0, 0.0]]
)

ktk.geometry.matmul(T, p)
```

b) Do this exercise using the {{ktk_geometry_rotate}} and {{ktk_geometry_translate}} functions.

```{code-cell} ipython3
:tags: [hide-cell]

p = np.array([[1.0, 2.0, 0.0, 1.0]])

rotated_p = ktk.geometry.rotate(p, angles=[20], degrees=True, seq="z")
final_p = ktk.geometry.translate(rotated_p, translations=[[-1.0, 0.0, 0.0]])

final_p
```



## 💪 Exercise 2

The trajectory of a point in global coordinates is:

$$
\vec{p}(t_0) = (3, 4, 5) \\
\vec{p}(t_1) = (4, 5, 5) \\
\vec{p}(t_2) = (5, 6, 5) \\
\vec{p}(t_3) = (6, 7, 5) \\
\vec{p}(t_4) = (7, 8, 5) \\
$$

Using Kinetics Toolkit's geometry module, rotate this whole trajectory counterclockwise on the z-axis by 20° then translate it by one unit to the left.

a) Do this exercise by creating the corresponding homogeneous transform using {{ktk_geometry_create_transform_series}}, then by multiplying this transform by the point coordinates using {{ktk_geometry_matmul}}.

```{code-cell} ipython3
:tags: [hide-cell]

import kineticstoolkit.lab as ktk
import numpy as np


p = np.array(
    [
        [3.0, 4.0, 5.0, 1.0],
        [4.0, 5.0, 5.0, 1.0],
        [5.0, 6.0, 5.0, 1.0],
        [6.0, 7.0, 5.0, 1.0],
        [7.0, 8.0, 5.0, 1.0],
    ]
)

T = ktk.geometry.create_transform_series(
    angles=[20], degrees=True, seq="z", positions=[[-1.0, 0.0, 0.0]]
)

ktk.geometry.matmul(T, p)
```

b) Do this exercise using the {{ktk_geometry_rotate}} and {{ktk_geometry_translate}} functions.

```{code-cell} ipython3
:tags: [hide-cell]

p = np.array(
    [
        [3.0, 4.0, 5.0, 1.0],
        [4.0, 5.0, 5.0, 1.0],
        [5.0, 6.0, 5.0, 1.0],
        [6.0, 7.0, 5.0, 1.0],
        [7.0, 8.0, 5.0, 1.0],
    ]
)

rotated_p = ktk.geometry.rotate(p, angles=[20], degrees=True, seq="z")
final_p = ktk.geometry.translate(rotated_p, translations=[[-1.0, 0.0, 0.0]])

final_p
```



## Rotating vectors

For this second example, let's apply this same transform to a vector of 10 units toward the x-axis (10, 0, 0) as shown in {numref}`fig_geometry_moving_vectors`.

```{figure}
:label: fig_geometry_moving_vectors
:width: 4in
![](_static/images/fig_geometry_moving_vectors.png)

Rotating a vector in respect to the global reference frame.
```


The same equation applies:

$$
^\text{global} \vec{v}_{\text{tranformed}} ~~~ = ~~~ T ~~~ ^\text{global} \vec{v}_\text{initial}
$$

Although vector $\vec{v}_\text{initial}$ shares the same coordinates as $p_\text{initial}$ in the previous example, it is written differently (with a 0 instead of a 1 in the fourth coordinate). This is because the fourth element is responsible for translations, and contrary to a point, a vector cannot be translated.

$$
^\text{global} \vec{v}_\text{initial} =
\begin{bmatrix}
10 \\ 0 \\ 0 \\ 0
\end{bmatrix}
$$

We multiply this vector by the transform to obtain the final vector:

$$
^\text{global} \vec{v}_{\text{tranformed}} =
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix} 10 \\ 0 \\ 0 \\ 0 \end{bmatrix} \\ =
\begin{bmatrix} 10\cos(30) \\ 10\sin(30) \\ 0 \\ 0 \end{bmatrix} =
\begin{bmatrix} 8.66 \\ 5 \\ 0 \\ 0 \end{bmatrix}
$$

The final coordinates of the vector are (8.66, 5, 0).


### Application in Kinetics Toolkit

The transform $T$ can be created using:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

T = ktk.geometry.create_transform_series(
    angles=[30],
    degrees=True,
    seq="z",  # Which means a rotation around the z axis
)

T
```

The rotated vector is:

```{code-cell} ipython3
ktk.geometry.matmul(T, [[10, 0, 0, 1]])
```

### Direct transformation in Kinetics Toolkit

We can also rotate the vector directly using {{ktk_geometry_rotate}}):

```{code-cell} ipython3
ktk.geometry.rotate([[10, 0, 0, 0]], seq="z", angles=[30], degrees=True)
```



## Moving frames (transforms)

The orientation and position of a frame (defined as a coordinate system attached to a segment) are expressed by a [homogeneous transform](geometry_transforms.md). We remind that the first three columns are three vectors (the direction of three axes), and the fourth column is a point (the position of the origin). Therefore, since a homogeneous transform can move both points and vectors, it can also move complete frames.

```{figure}
:label: fig_geometry_moving_frames
:width: 5in
![](_static/images/fig_geometry_moving_frames.png)

Rotating and translating a local frame in respect to the global reference frame.
```

Let's use the same homogeneous transform to rotate and translate the frame  $^\text{global} _\text{local-initial} F$ (which reads as *Frame 'local' in its initial pose, expressed in global coordinates*) as shown in {numref}`fig_geometry_moving_frames`.

$$
^\text{global} _\text{local-tranformed} F ~~~ = ~~~ T ~~~ ^\text{global} _\text{local-initial} F
$$

We first express the unrotated frame $^\text{global} _\text{local-initial} F$:

$$
^\text{global} _\text{local-initial} F
=
\begin{bmatrix}
\cos(0) & -\sin(0) & 0 & 10 \\
\sin(0) & \cos(0) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
=
\begin{bmatrix}
1 & 0 & 0 & 10 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

The transformed frame is calculated using:

$$
^\text{global} _\text{local-transformed} F
=
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 2 \\
\sin(30) & \cos(30) & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 & 10 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\\=
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 10.66 \\
\sin(30) & \cos(30) & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$


### Application in Kinetics Toolkit

The transform $T$ is created using:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

T = ktk.geometry.create_transform_series(
    angles=[30],
    degrees=True,
    seq="z",  # Which means a rotation around the z axis
    positions=[[2.0, 0.0, 0.0, 1.0]],
)

T
```

The initial local frame is expressed as:

```{code-cell} ipython3
initial_frame = np.array(
    [
        [
            [1.0, 0.0, 0.0, 10.0],
            [0.0, 1.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]
    ]
)
```

The rotated frame is:

```{code-cell} ipython3
ktk.geometry.matmul(T, initial_frame)
```

### Direct transformation in Kinetics Toolkit

We can also rotate and translate the initial frame using {{ktk_geometry_rotate}} and {{ktk_geometry_translate}}:

```{code-cell} ipython3
rotated_frame = ktk.geometry.rotate(
    initial_frame, seq="z", angles=[30], degrees=True
)
final_frame = ktk.geometry.translate(rotated_frame, [[2.0, 0.0, 0.0]])

final_frame
```


# 💪 Exercise 3

In {numref}`fig_geometry_basics_exercise`, the position of the elbow in the arm coordinate system is $(0, -0.5, 0)$.

Using Kinetics Toolkit's geometry module, express the position of the elbow in global coordinates for shoulder flexion movements of 0°, 5°, 10°, and 15°.

a) Do this exercise by creating the corresponding homogeneous transform using {{ktk_geometry_create_transform_series}}, then by multiplying this transform by the point coordinates using {{ktk_geometry_matmul}}.

```{code-cell} ipython3
:tags: [hide-cell]

import numpy as np

import kineticstoolkit.lab as ktk

p_elbow_ref_arm = np.array([[0.0, -0.5, 0.0, 1.0]])

T_arm = ktk.geometry.create_transform_series(
    angles=[0, 5, 10, 15],
    degrees=True,
    seq="z",
)

ktk.geometry.matmul(T_arm, p_elbow_ref_arm)
```

b) Do this exercise using the  {{ktk_geometry_rotate}} and {{ktk_geometry_translate}} functions.

```{code-cell} ipython3
:tags: [hide-cell]

p_elbow_ref_arm = np.array([[0.0, -0.5, 0.0, 1.0]])

ktk.geometry.rotate(
    p_elbow_ref_arm,
    angles=[0, 5, 10, 15],
    seq="z",
)
```
