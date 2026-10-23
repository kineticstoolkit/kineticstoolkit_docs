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

#todo This has been moved.

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
