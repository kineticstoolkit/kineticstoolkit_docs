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

# Kinematic chains

## Series of homogeneous transforms

Now that we understand how powerful homogeneous transforms are, we will take it one step further, and chain multiple transforms.

In this example, we will calculate the position of the wrist in global coordinates, according to {numref}`fig_geometry_basics_exercise`, based on this known information:

- the length of the upper arm is 38 cm;
- the shoulder is located 15 cm forward and 70 cm upward to the global origin;
- the upper arm is inclined at 30 degrees of the vertical.
- the length of the forearm is 34 cm;
- the elbow is flexed 20 degrees.


**Solution:**

The way to solve this problem is to see it as a chain of parent-child relations between coordinate systems (CS). Let's consider the previous example in the form of a parent-child chain.

$$
\text{global CS} \rightarrow \text{upper arm CS} \rightarrow \text{elbow}
$$

- The position of the elbow was a child of the upper arm frame;
- The upper arm frame was a child of the global frame;

We solved $^\text{global}p_\text{elbow}$ by expressing:

1. the position of the elbow **in its parent frame**: $^\text{upper arm}p_\text{elbow}$;
2. the upper arm frame **in its parent frame**: $^\text{global}_\text{upper arm}T$.

and by using this equation.

$$
^\text{global}p_\text{elbow}
=
(^\text{global}_\text{upper arm}T)
(^\text{upper arm}p_\text{elbow})
$$


This new problem is similar, with the difference that we now have an additional chain:

$$
\text{global CS} \rightarrow \text{upper arm CS} \rightarrow \text{forearm CS} \rightarrow \text{wrist}
$$

- The position of the wrist is a child of the forearm frame:
- The forearm frame is a child of the upper arm frame;
- The upper arm frame is a child of the global frame;


We solve $^\text{global}p_\text{wrist}$ by expressing:

1. the position of the wrist **in its parent frame**: $^\text{forearm}p_\text{wrist}$;
2. the forearm frame **in its parent frame**: $^\text{upper arm}_\text{frame}T$;
3. the upper arm frame **in its parent frame**: $^\text{global}_\text{upper arm}T$.

This leads to this equation:

$$
^\text{global}p_\text{wrist}
=
(^\text{global}_\text{upper arm}T)
(^\text{upper arm}_\text{forearm}T)
(^\text{forearm}p_\text{wrist})
$$

:::{tip}
Take a look at how using this notation, the upper and lower indices cancel out to give the final transformation.
:::


## Navigating between chain elements using Kinetics Toolkit

Using Kinetics Toolkit, we can solve this example by performing the last equation. We first express the local position of the wrist, and the reference frames of the forearm and upper arm:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

# position of the wrist in the forearm coordinate system
forearm_p_wrist = [[0, -0.34, 0, 1]]

# forearm frame in the upper arm coordinate system
upperarm_T_forearm = ktk.geometry.create_transform_series(
     angles=[20],
     degrees=True,
     seq="z",
     positions=[[0, -0.38, 0]], 
)

# upper arm frame in the global coordinate system
global_T_upperarm = ktk.geometry.create_transform_series(
    angles=[30],
    degrees=True,
    seq="z", 
    positions=[[0.15, 0.7, 0]]
)
```

Then we apply the multiplication directly:

```{code-cell} ipython3
global_p_wrist = ktk.geometry.matmul(
    global_T_upperarm, ktk.geometry.matmul(upperarm_T_forearm, forearm_p_wrist)
)

global_p_wrist
```

Another, equivalent method, is to iteratively express everything in global coordinates using {{ktk_geometry_get_global_coordinates}}. We already defined the upper arm frame:

```{code-cell} ipython3
global_T_upperarm
```

Then we proceed with the forearm frame:

```{code-cell} ipython3
global_T_forearm = ktk.geometry.get_global_coordinates(
    local_coordinates=upperarm_T_forearm, reference_frames=global_T_upperarm
)

global_T_forearm
```

Then we proceed with the wrist:

```{code-cell} ipython3
global_p_wrist = ktk.geometry.get_global_coordinates(
    forearm_p_wrist, reference_frames=global_T_forearm
)

global_p_wrist
```
