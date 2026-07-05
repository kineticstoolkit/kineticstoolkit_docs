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

# Styling and exporting videos and pictures

Every element of the Player can be stylized. Let's load the tennis serve data again, then we will use the properties of the Player to style its elements.

```{code-cell} ipython3
:tags: [remove-output, hide-cell]
import kineticstoolkit.lab as ktk

# Download and read markers from a sample C3D file
filename = ktk.doc.download("kinematics_tennis_serve_2players.c3d")
markers = ktk.read_c3d(filename)["Points"]
interconnections = dict()  # Will contain all segment definitions
interconnections["LLowerLimb"] = {
    "Color": (0, 0.5, 1),  # In RGB format (here, greenish blue)
    "Links": [  # List of lines that span lists of markers
        ["*LTOE", "*LHEE", "*LANK", "*LTOE"],
        ["*LANK", "*LKNE", "*LASI"],
        ["*LKNE", "*LPSI"],
    ],
}
interconnections["RLowerLimb"] = {
    "Color": (0, 0.5, 1),
    "Links": [
        ["*RTOE", "*RHEE", "*RANK", "*RTOE"],
        ["*RANK", "*RKNE", "*RASI"],
        ["*RKNE", "*RPSI"],
    ],
}
interconnections["LUpperLimb"] = {
    "Color": (0, 0.5, 1),
    "Links": [
        ["*LSHO", "*LELB", "*LWRA", "*LFIN"],
        ["*LELB", "*LWRB", "*LFIN"],
        ["*LWRA", "*LWRB"],
    ],
}
interconnections["RUpperLimb"] = {
    "Color": (1, 0.5, 0),
    "Links": [
        ["*RSHO", "*RELB", "*RWRA", "*RFIN"],
        ["*RELB", "*RWRB", "*RFIN"],
        ["*RWRA", "*RWRB"],
    ],
}
interconnections["Head"] = {
    "Color": (1, 0.5, 1),
    "Links": [
        ["*C7", "*LFHD", "*RFHD", "*C7"],
        ["*C7", "*LBHD", "*RBHD", "*C7"],
        ["*LBHD", "*LFHD"],
        ["*RBHD", "*RFHD"],
    ],
}
interconnections["TrunkPelvis"] = {
    "Color": (0.5, 1, 0.5),
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
p = ktk.Player(
    markers,
    interconnections=interconnections,
    up="z",
    anterior="-y",
    target=(0, 0.5, 1),
    azimuth=0.1,
    zoom=1.5, 
)
```

```{code-cell} ipython3
:tags: [remove-input]
p.set_contents(markers.get_ts_between_times(6, 8))

p._mpl_objects["Figure"]
```

## Styling the background

To set a white background:

```{code-cell} ipython3
p.background_color = 'w'

# Equivalent to p.background_color = (1.0, 1.0, 1.0)
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```


## Styling the grid

### Grid size and subdivisions

To have a smaller grid (4x4 metres) with a smaller subdivision size (50x50 cm):

```{code-cell} ipython3
p.grid_size = 4
p.grid_subdivision_size = 0.5
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

### Grid origin

The grid origin can be placed anywhere in the scene, using the `grid_origin` property. For example:

```{code-cell} ipython3
p.grid_origin = (0.0, 0.5, 0.0)
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

### Grid width

To get a thinner grid:

```{code-cell} ipython3
p.grid_width = 0.5
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

### Grid colour

To get a light grey grid:

```{code-cell} ipython3
p.grid_color = (0.75, 0.75, 0.75)
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```


## Styling points

### Point size

To get bigger points:

```{code-cell} ipython3
p.point_size = 10
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

### Point colour

The default point colour can be set by the `default_point_color` property:

```{code-cell} ipython3
p.default_point_color = 'r'

# Equivalent to: p.default_point_color = (1.0, 0.0, 0.0)
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

To assign individual colours, we add a `Color` info to the TimeSeries' data. For instance, to show Viktor's markers in dark green:

```{code-cell} ipython3
markers = p.get_contents()

for key in markers.data:
    if key.startswith("Viktor:"):
        markers = markers.add_info(key, "Color", (0.0, 0.75, 0.0))

p.set_contents(markers)
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```


## Styling interconnections

### Interconnection width

To get thicker interconnections:

```{code-cell} ipython3
p.interconnection_width = 4.0
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

### Interconnection colour

Colour is part of the [interconnection dictionary](player_interconnections.md). Therefore, we change interconnection colour using this dictionary. For instance, to set all interconnections to light grey:

```{code-cell} ipython3
interconnections = p.get_interconnections()

for segment in interconnections:
    interconnections[segment]["Color"] = (0.75, 0.75, 0.75)

p.set_interconnections(interconnections)
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

## Styling frames

### Frame size

To get half-metre long frames:

```{code-cell} ipython3
p.frame_size = 0.5
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```

### Frame width

To get thinner frames:

```{code-cell} ipython3
p.frame_width = 1.0
```

```{code-cell} ipython3
:tags: [remove-input]
p._mpl_objects["Figure"]
```


## Exporting

### Exporting to an image

The Player's current view can be exported to any file format supported by Matplotlib such as PNG, JPEG, SVG, or PDF, using {{ktk_player_to_image}}:

```
p.to_image("exported_image.png")
```

### Exporting to a video

The whole animation in the current viewpoint can be exported to an MP4 file using {{ktk_player_to_video}}:


```
p.to_video("exported_video.mp4")
```

```{code-cell} ipython3
:tags: [remove-input]
from IPython.display import Video
import os
p.to_video("exported_video.mp4", show_progress_bar=False)
display(Video("exported_video.mp4", embed=True, width=600, html_attributes='loop autoplay controls'))
os.remove("exported_video.mp4")
```

```{note}
To create videos, the package `ffmpeg` must be installed on your computer. If you installed Kinetics Toolkit using `conda`, then it is already installed. If you used `pip`, you must install it manually.
```
