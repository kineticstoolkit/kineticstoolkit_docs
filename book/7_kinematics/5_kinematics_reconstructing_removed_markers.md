---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-cell]
%matplotlib inline
```

# Reconstructing removed markers

Rigid bodies affixed to segments are generally used to reconstruct points where it is difficult or impossible to affix a real marker. For example, if a marker would be at risk of falling during the action, it can be installed during a short calibration acquisition and then removed during the action.

The following example represents such a situation:
- With a rigid body of three markers affixed to the left arm, and a single marker affixed to the left lateral elbow epicondyle, an acquisition of a few seconds was recorded with the participant barely moving.
- After removing the elbow epicondyle marker, a task was recorded.
- We want to reconstruct the trajectory of the left lateral elbow epicondyle during the task, even if it was not present during the task.

## Loading sample data

We will create two TimeSeries, one that represents the markers during the static acquisition, and the other representing the markers during the task.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt
import numpy as np

# Static acquisition
markers_static = ktk.read_c3d(
    ktk.doc.download("kinematics_racing_static.c3d")
)["Points"]
markers_static = markers_static.get_subset(
    ["ArmL1", "ArmL2", "ArmL3", "LateralEpicondyleL"]
)
plt.subplot(2, 2, 1)
markers_static.plot("ArmL1")
plt.subplot(2, 2, 2)
markers_static.plot("ArmL2")
plt.subplot(2, 2, 3)
markers_static.plot("ArmL3")
plt.subplot(2, 2, 4)
markers_static.plot("LateralEpicondyleL")
plt.suptitle("Static acquisition")
plt.tight_layout()

# Task acquisition
markers_task = ktk.read_c3d(
    ktk.doc.download("kinematics_racing_propulsion.c3d")
)["Points"]
markers_task = markers_task.get_subset(
    [
        "ArmL1",
        "ArmL2",
        "ArmL3",
    ]
)
plt.figure()
plt.subplot(2, 2, 1)
markers_task.plot("ArmL1")
plt.subplot(2, 2, 2)
markers_task.plot("ArmL2")
plt.subplot(2, 2, 3)
markers_task.plot("ArmL3")
plt.suptitle("Task acquisition")
plt.tight_layout()
```

## Creating a cluster of markers

The idea is very similar to section [](4_kinematics_reconstructing_occluded_markers.md), where we reconstructed missing markers that belonged to the same rigid body. In this new example, since the lateral elbow epicondyle belongs to the same segment as the rigid body, we can include it in the definition of the marker cluster.

```{code-cell} ipython3
cluster = ktk.kinematics.create_cluster(
    markers_static,
    ["ArmL1", "ArmL2", "ArmL3", "LateralEpicondyleL"],
)
```

## Tracking the cluster

Now, we can track this cluster to reconstruct the whole set of four markers, including the epicondyle, during the propulsion acquisitions.

```{code-cell} ipython3
reconstructed_markers_task = ktk.kinematics.track_cluster(
    markers_task,
    cluster,
)

# Plot the results
plt.subplot(2, 2, 1)
reconstructed_markers_task.plot("ArmL1")
plt.subplot(2, 2, 2)
reconstructed_markers_task.plot("ArmL2")
plt.subplot(2, 2, 3)
reconstructed_markers_task.plot("ArmL3")
plt.subplot(2, 2, 4)
reconstructed_markers_task.plot("LateralEpicondyleL")
plt.tight_layout()
```
