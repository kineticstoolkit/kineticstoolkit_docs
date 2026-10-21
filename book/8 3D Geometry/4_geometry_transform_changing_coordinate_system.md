# Changing between local and global coordinates

In section [](1_geometry_basics.md), we learned about the homogeneous transform, which is a 4x4 matrix that defines the **position and orientation of a coordinate system with respect to a reference coordinate system.**

In section [](4_geometry_transform_changing_coordinate_system.md), we learned that the same 4x4 matrix can also be defined as a **translation and rotation of a point, vector, or transform.**

In this new section, we will use both definitions to see the third and last role of the homogeneous transform, which is **remapping points, vectors, and transforms from one coordinate system to another.**


## Expressing local coordinates in global coordinates

Let's start with this example, where we want to express the yellow point of {numref}`fig_geometry_change_coordinate_system` in global coordinates.


:::{figure}
:label: fig_geometry_change_coordinate_system
:width: 4in
![](_static/images/fig_geometry_change_coordinate_system.png)

Expressing a local point in global coordinates.
:::


The unknown is the yellow point's coordinates with respect to the global frame:

```{math}
:label: eq_geometry_transform_unkown
^\text{global} p = \text{?}
```

Instead of considering point $p$ as a point in its own local coordinate system, let's imagine that it was first expressed in the global reference frame ($^\text{global} p_\text{initial}$). Then, it was rotated by 30 degrees around the origin, then translated by (7, 5, 0) to reach its final position ($^\text{global} p_\text{transformed}$), as shown in {numref}`fig_geometry_transformation_sequence`.


:::{figure}
:label: fig_geometry_transformation_sequence
:width: 8in
![](_static/images/fig_geometry_transformation_sequence.png)

Transformation sequence from local coordinates to global coordinates.
:::

This operation is expressed by:

```{math}
:label: eq_geometry_transform_transformation

^\text{global} p_\text{transformed}
~~~ =
~~~ T
~~~ ^\text{global} p_\text{initial}
```


where $T$ represents a rotation of 30 degrees and a translation of (7, 5, 0) units.

Now, let's put {numref}`fig_geometry_change_coordinate_system` and {numref}`fig_geometry_transformation_sequence` in relation.

The first image of {numref}`fig_geometry_transformation_sequence` expresses the yellow point in its local reference frame. Therefore:

```{math}
:label: eq_geometry_localp_equivalence
^\text{global} p_\text{initial} = ^\text{local} p
```

The last image of {numref}`fig_geometry_transformation_sequence` expresses the yellow point in global coordinates. Therefore:

```{math}
:label: eq_geometry_globalp_equivalence
^\text{global} p_\text{transformed} = ^\text{global} p
```

By substituting {eq}`eq_geometry_localp_equivalence` and {eq}`eq_geometry_globalp_equivalence` into {eq}`eq_geometry_transform_transformation`, we get:

```{math}
^\text{global} p = T ~~~ ^\text{local} p
```

where T, which was formerly interpreted as the transformation applied in {numref}`fig_geometry_transformation_sequence`, is now interpreted as the local reference frame itself: a coordinate system that has been rotated by 30 degrees and translated by (7, 5, 0) units.

We see that if we know the local coordinates of a point $^\text{local} p$, and we know the coordinates of its local reference frame $T$, then the global coordinates of the point are obtained simply by multiplying $T$ and $^\text{local} p$.

Now, let's solve the problem. We know the yellow point's coordinate (2, 1, 0) in respect to the local frame:

$$
^\text{local}p = \begin{bmatrix}
2 \\ 1 \\ 0 \\ 1
\end{bmatrix}
$$

We also know how to express the local frame as a homogeneous transform:

$$
~^\text{global}_\text{local}T = \begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 7 \\
\sin(30) & \cos(30) & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Therefore:

$$
^\text{global}p
=
\begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 7 \\
\sin(30) & \cos(30) & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\ 1 \\ 0 \\ 1
\end{bmatrix}
\\=
\begin{bmatrix}
0.866 & -0.5 & 0 & 7 \\
0.5 & 0.866 & 0 & 5 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
2 \\ 1 \\ 0 \\ 1
\end{bmatrix}
=
\begin{bmatrix}
8.232 \\ 6.866 \\ 0 \\ 1
\end{bmatrix}
$$

The position of the yellow point, in global coordinates, is (8.232, 6.866, 0).



## Expressing global coordinates in local coordinates

We get global coordinates using:

$$
^\text{global}p 
~~~ =
~~~ ^\text{global}_\text{local}T
~~~ ^\text{local}p 
$$

The reverse transform is literally the inverse of the homogeneous matrix:

$$
^\text{global}_\text{local}T^{-1}
~~~ ^\text{global}p 
~~~ =
~~~ ^\text{global}_\text{local}T^{-1}
~~~ ^\text{global}_\text{local}T
~~~ ^\text{local}p 
$$

$$
^\text{global}_\text{local}T^{-1}
~~~ ^\text{global}p 
~~~
=
~~~ ^\text{local}p 
$$


## Example

This ability to switch between coordinate systems is very powerful. Let's get back to {numref}`fig_geometry_local_coordinates_rotated`.

Using this information:
1. The length of the upper arm is 38 cm;
2. The shoulder is located 15 cm forward and 70 cm upward from the global origin;
3. The upper arm is inclined at 30 degrees to the vertical.

We want to know the position of the elbow in global coordinates.

**Solution:**

The first piece of information allows us to express the position of the elbow in the local upper arm coordinate system:

$$
~^\text{upper arm}p_\text{elbow} = \begin{bmatrix}
0 \\ -0.38 \\ 0 \\ 1
\end{bmatrix}
$$

The second and third points of information allow us to express the upper arm frame:

$$
~^\text{global}_\text{upper arm}T = \begin{bmatrix}
\cos(30) & -\sin(30) & 0 & 0.15 \\
\sin(30) & \cos(30) & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix} \\=
\begin{bmatrix}
0.866 & -0.5 & 0 & 0.15 \\
0.5 & 0.866 & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
$$

Therefore, the position of the elbow in the global coordinate system is:

$$
^\text{global}p_\text{elbow}
~~~=
~~~^\text{global}_\text{upper arm}T
~~~^\text{upper arm}p_\text{elbow}
$$

$$
^\text{global}p_\text{elbow}
\\=
\begin{bmatrix}
0.866 & -0.5 & 0 & 0.15 \\
0.5 & 0.866 & 0 & 0.7 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}
\begin{bmatrix}
0 \\ -0.38 \\ 0 \\ 1
\end{bmatrix} \\=
\begin{bmatrix}
0.34 \\ 0.371 \\ 0 \\ 1
\end{bmatrix}
$$

Its global coordinates are $(0.34, 0.371, 0)$.

## Changing coordinate systems using Kinetics Toolkit

Using the {{ktk_geometry_create_transform_series}} and {{ktk_geometry_matmul}} functions introduced in the previous section, we can solve this problem as follows:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

T_upperarm = ktk.geometry.create_transform_series(
    angles=[30], degrees=True, seq="z", positions=[[0.15, 0.7, 0]], 
)

local_p_elbow = [[0, -0.38, 0, 1]]

global_p_elbow = ktk.geometry.matmul(T_upperarm, local_p_elbow)

global_p_elbow
```

However, since changing coordinates between reference frames is so common, Kinetics Toolkit also provides the functions {{ktk_geometry_get_global_coordinates}} and {{ktk_geometry_get_local_coordinates}}. These functions are simple shortcuts but are easier to remember:

```{code-cell} ipython3
global_p_elbow = ktk.geometry.get_global_coordinates(
    local_coordinates=local_p_elbow, reference_frames=T_upperarm
)

global_p_elbow
```

```{code-cell} ipython3
local_p_elbow = ktk.geometry.get_local_coordinates(
    global_coordinates=global_p_elbow, reference_frames=T_upperarm
)

local_p_elbow
```

