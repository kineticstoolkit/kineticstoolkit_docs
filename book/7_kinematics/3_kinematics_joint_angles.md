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


# Calculating joint angles from a kinematic acquisition

In this section, we will calculate the elbow joint angles during the propulsion of a racing wheelchair. At the end of this tutorial, we will plot curves of elbow flexion and pronation angles during the complete acquisition.

:::{caution}
Please be sure to understand the concepts of frame, homogeneous transform, and Euler angles before continuing. If you don't, start with section [](../3%20Performing%203D%20Geometrical%20Operations/1_geometry.md).
:::

Calculating joint angles requires the following steps:

**Step 1.** Read the marker trajectories.

**Step 2.** Calculate series of frames that express the orientation of all segments that compose the analyzed joints (how are both segments oriented in space). Here, we calculate frame series for the upper arm and forearm.

**Step 3.** Express a series of homogeneous transforms between the proximal and distal frames: how the distal (forearm) segment is oriented in space compared to the proximal segment (upper arm);

**Step 4.** Extract the series of Euler angles from these homogeneous transforms (what series of three angles allow such relative orientation);

**Step 5.** Interpret these Euler angles as rotations around anatomical axes.

## Read and visualize marker trajectories

We start by downloading and visualizing some data:

```{code-cell} ipython3
:tags: [remove-output]

import kineticstoolkit.lab as ktk

# Read the markers
markers = ktk.read_c3d(
    ktk.doc.download("kinematics_racing_full.c3d")
)["Points"]

# Interconnect markers for easier visualization
interconnections = {
    "ArmR": {
        "Color": [1, 0.25, 0],
        "Links": [
            ["AcromionR", "MedialEpicondyleR"],
            ["AcromionR", "LateralEpicondyleR"],
            ["AcromionR", "OlecraneR"],
        ],
    },
    "ForearmR": {
        "Color": [1, 0.5, 0],
        "Links": [
            ["MedialEpicondyleR", "RadialStyloidR"],
            ["MedialEpicondyleR", "UlnarStyloidR"],
            ["LateralEpicondyleR", "RadialStyloidR"],
            ["LateralEpicondyleR", "UlnarStyloidR"],
            ["OlecraneR", "RadialStyloidR"],
            ["OlecraneR", "UlnarStyloidR"],
            ["UlnarStyloidR", "RadialStyloidR"],
        ],
    },
}
```

Showing these markers in the Player:

```{code-cell} ipython3
:tags: [remove-output]
# Visualize in the player
%matplotlib qt5

p = ktk.Player(markers, interconnections=interconnections)
```

```{code-cell} ipython3
:tags: [remove-input]
p.set_contents(markers.get_ts_between_times(0, 1))
p.zoom=3.5
p.azimuth=0.8
p.elevation=0.16
p.pan=(0.2, -0.7)
p.playback_speed=0.25

# Show one second (only needed in Notebooks)
p._to_animation()
```

## Create local coordinate systems

To calculate the elbow angles, we need to express frames for the arm and forearm segments. We will use the recommendations of the International Society of Biomechanics [^1] to define these local coordinate systems:

### Arm coordinate system

Following the ISB recommendations, the local coordinate system for the humerus is defined as follow:

1. The origin is GH (glenohumeral joint).
2. The y axis is the line between GH and the midpoint of EL (lateral elbow epicondyle) and EM (medial elbow epicondyle), pointing to GH.
3. The x axis is the normal to the GH-EL-EM plane, pointing forward.
4. The z axis is perpendicular to x and y, pointing to the right.

**1. The origin is GH (glenohumeral joint)**

We don't have a marker for the glenohumeral joint, but we have one for the acromion. We will approximate GH by the acromion.

```{code-cell} ipython3
origin = markers.data["AcromionR"]
```

**2. The y axis is the line between GH and the midpoint of EL (lateral elbow epicondyle) and EM (medial elbow epicondyle), pointing to GH**

```{code-cell} ipython3
y = markers.data["AcromionR"] - 0.5 * (
    markers.data["LateralEpicondyleR"] + markers.data["MedialEpicondyleR"]
)
```

**3. The x axis is the normal to the GH-EL-EM plane, pointing forward**

Since x is normal to the GH-EL-EM plane, this plane is a yz plane. We need to define a second vector (other than y) to form this yz plane.

```{code-cell} ipython3
yz = markers.data["LateralEpicondyleR"] - markers.data["MedialEpicondyleR"]
```

Note that the direction of the yz vector is important. For the plane normal to be forward, the cross product of y and yz must also point forward. In this case, following the [right-hand/screw rule](https://en.wikipedia.org/wiki/Right-hand_rule), y (upward) cross yz (right) effectively yields a forward vector.

As an easier rule of thumb, look at definition 4: the z vector will point to the right. Then just make the yz vector also point to (grossly) the right since in anatomical position, the right lateral epicondyle is to the right of the right medial epicondyle.

We have now defined everything to create the series of humerus frame. We first create an empty TimeSeries for our frames:

```{code-cell} ipython3
frames = ktk.TimeSeries(time=markers.time)
```

Now, we will create the `ArmR` transform series.

```{code-cell} ipython3
frames.data["ArmR"] = ktk.geometry.create_transform_series(positions=origin, y=y, yz=yz)
```

Let's visualize it:

```{code-cell} ipython3
p.set_contents(markers.merge(frames))
```

```{code-cell} ipython3
:tags: [remove-input]
p.set_contents(
    markers.get_ts_between_times(0, 1).merge(
        frames.get_ts_between_times(0, 1)
    )
)
p._to_animation()
```

### Forearm frame

We will now proceed with the exact same steps to create the forearm coordinate system. From the ISB [^1]:

**1. The origin is US (ulnar styloid process).**

```{code-cell} ipython3
origin = markers.data["UlnarStyloidR"]
```

**2. The y axis is the line between US and the midpoint between EL and EM, pointing proximally.**

```{code-cell} ipython3
y = (
    0.5
    * (markers.data["LateralEpicondyleR"] + markers.data["MedialEpicondyleR"])
    - markers.data["UlnarStyloidR"]
)
```

**3. The x axis is the line perpendicular to the plane through US, RS, and the midpoint between EL and EM, pointing forward.**

**4. The z axis is perpendicular to x and y, pointing to the right.**

This means that US, RS, and the elbow center make a yz plane. Since z will point to the right in anatomical position, we will create a yz vector that points grossly to the right in anatomical position.

```{code-cell} ipython3
yz = markers.data["RadialStyloidR"] - markers.data["UlnarStyloidR"]
```

We are now ready to create the `ForearmR` frame series.

```{code-cell} ipython3
frames.data["ForearmR"] = ktk.geometry.create_transform_series(positions=origin, y=y, yz=yz)
```

Let's visualize our markers with both new frames:

```{code-cell} ipython3
p.set_contents(markers.merge(frames))
```

```{code-cell} ipython3
:tags: [remove-input]
p.set_contents(
    markers.get_ts_between_times(0, 1).merge(
        frames.get_ts_between_times(0, 1)
    )
)
p._to_animation()
```


## Find the series of homogeneous transforms between both segments

Now that we have expressed frames for both the arm and forearm, we can find the homogeneous transform between both frames. This is equivalent to expressing the forearm frame in the local coordinates system of the arm.

```{code-cell} ipython3
arm_to_forearm = ktk.geometry.get_local_coordinates(
    frames.data["ForearmR"], frames.data["ArmR"]
)

arm_to_forearm
```

## Extract the series of Euler angles

We now have a series of homogeneous matrices, from which we will extract Euler angles corresponding to flexion and pronation. We will use the {{ktk_geometry_get_angles}} function to extract these Euler angles. We, however, first need to define the sequence of rotation for these angles. Still following the recommendations of the International Society of Biomechanics [^1], we define the series of rotations from the arm to forearm as:

**First rotation:** Around the humerus' z axis. Corresponds to a flexion (positive) or hyperextension (negative).

**Second rotation:** Around the forearm's rotated x axis. Corresponds to a "carrying angle" due to a tilt in the humeral flexion/extension axis at the humero-ulnar joint and an angulation of the ulna itself.

**Third rotation:** Around the forearm's rotated y axis. Corresponds to a pronation (positive) or supination (negative).

These rotations are relative to moving axes (every other rotation is performed around a new frame generated by the previous rotation). Therefore, we will use 'ZXY' (capital letters - see {{ktk_geometry_get_angles}} for the conventions) as the sequence of rotations.

```{code-cell} ipython3
euler_angles = ktk.geometry.get_angles(arm_to_forearm, "ZXY", degrees=True)

euler_angles
```

## Plot the Euler angles

Now that we have calculated the angles, we create a last TimeSeries that represents the meaning of these angles.

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt
plt.figure()
```

```{code-cell} ipython3
angles = ktk.TimeSeries(time=markers.time)

angles.data["Elbow flexion"] = euler_angles[:, 0]
angles.data["Forearm pronation"] = euler_angles[:, 2]

angles = angles.add_info("Elbow flexion", "Unit", "deg")
angles = angles.add_info("Forearm pronation", "Unit", "deg")

angles.plot()
```

```{code-cell} ipython3
:tags: [remove-input]
# Hack because now Matplotlib is qt5 and it won't revert back to inline.
from IPython.display import Image
import os
import matplotlib.pyplot as plt
plt.savefig("temp.png")
display(Image("temp.png", embed=True))
os.remove("temp.png")
```

From this curve, we can now see that the elbow goes from a total extension to a flexion of about 100 degrees, while the forearm stays in a pronated angle of about 125 to 170 degrees (defined from a fully supinated position in anatomical position).

The process would be identical for any joint:

1. Create the series of reference frames for the two segments that compose the analyzed joint;
2. Express the series of rigid transforms from the proximal to distal joint;
3. Extract the series of Euler angles from these rigid transforms;
4. Interpret these Euler angle as anatomical rotation.

[^1]: G. Wu et al., "ISB recommendation on definitions of joint coordinate systems of various joints for the reporting of human joint motion - Part II: shoulder, elbow, wrist and hand," Journal of Biomechanics, vol. 38, no. 5, pp. 981--992, 2005.
