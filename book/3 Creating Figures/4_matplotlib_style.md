---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Styling plots

## Title, axis labels, legend and grid

We can add axis labels, a legend, a title and a grid using these functions:

- {{plt_xlabel}} adds a label for the horizontal (x) axis;
- {{plt_ylabel}} adds a label for the vertical (y) axis;
- {{plt_legend}} adds a legend to identify the series;
- {{plt_title}} adds a title to the graph;
- {{plt_grid}} adds a grid to the background.

For example:

```{code-cell} ipython3
import matplotlib.pyplot as plt

x = [0.0, 5.0, 10.0, 15.0, 20.0]
y1 = [0.0, 1.0, 4.0, 3.0, -2.0]
y2 = [1.0, 2.0, 3.0, 4.0, 5.0]

# Plot the data
plt.plot(x, y1)
plt.plot(x, y2)

# Add axis labels
plt.xlabel("Time (s)")
plt.ylabel("Amplitude (m)")

# Add a legend (labels are in the same order as they have been plotted)
plt.legend(["Instrument 1", "Instrument 2"])

# Add a title
plt.title("Comparing a same measurement using two instruments")

# Add a grid
plt.grid(True);
```

:::{tip} Legend labels
Another, less error-prone way to add legends is to define the labels at plot time. Instead of:

```
plt.plot(x, y1)
plt.plot(x, y2)
plt.legend(["Instrument 1", "Instrument 2"])
```

we may do:

```
plt.plot(x, y1, label="Instrument 1")
plt.plot(x, y2, label="Instrument 2")
plt.legend()
```

Both methods give the same results, but in the the second one, the legend always matches what is displayed on the figure, even if we modified the number of `plt.plot` calls and forgot to update the `plt.legend` call accordingly.
:::

## 💪 Exercise 1

Using a video camera, you recorded the position of a sprinter every 2 seconds. The recorded data are:

```{code-cell} ipython3
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # metres
```

Write a code that produces this figure:

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt

plt.plot(t, p)
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True);
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]
import matplotlib.pyplot as plt

plt.plot(t, p)
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True);
```


## 💪 Exercise 2

Using a video camera, you recorded the position of a sprinter every 2 seconds. The recorded data are:

```{code-cell} ipython3
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # metres
```

You also used five timing gates placed at positions 0m, 25m, 50m, 75m, and 100m. The times recorded by these timing gates are:

```{code-cell} ipython3
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]
```

Write a code that produces this figure:

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True);
```

```{code-cell} ipython3
:tags: [hide-cell, remove-output]
import matplotlib.pyplot as plt

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.grid(True)
plt.legend(["Video camera", "Timing gates"]);
```


## Markers, line style and colour

The optional, third argument `fmt` of the {{plt_plot}} function defines optional markers, line styles and line colours. This argument is a string composed of these characters:

### Marker

- `.` dot
- `o` round
- `x` cross (x)
- `+` cross (+)
- `^` triangle
- `d` diamond
- `s` square

By default, no marker is plotted.

### Line style

- `-` full line
- `--` dashed line
- `-.` dash-dotted line
- `:` dotted line

Default is a full line, unless a marker has been set, in which case the default is no line.

### Colour

- `r` red
- `g` green
- `b` blue
- `c` cyan
- `m` magenta
- `y` dark yellow
- `w` white
- `k` black

Default is the next colour in the current colour cycle.

Here are some examples:

```{code-cell} ipython3
import matplotlib.pyplot as plt

y = [0.0, 1.0, -1.0, 2.0, 0.5, 0.0]

plt.subplot(2, 2, 1)
plt.plot(y, ".-r")
plt.title("dot markers, full line, red")

plt.subplot(2, 2, 2)
plt.plot(y, "--g")
plt.title("no marker, dashed line, green")

plt.subplot(2, 2, 3)
plt.plot(y, "s-.b")
plt.title("square markers, dash-dotted line, blue")

plt.subplot(2, 2, 4)
plt.plot(y, "oc")
plt.title("round markers, no line, cyan")

plt.tight_layout()
```




## Axes

When we create a plot interactively, we can zoom on a particular section using the figure's Zoom and Pan buttons. It is also possible to zoom programmatically while we create the figure, using {{plt_axis}}.


### Rectangular zoom

Let's create some random data:

```{code-cell}
import matplotlib.pyplot as plt

random_data = [
    0.60921838, 0.80049539, 0.11593785, 0.90703271, 0.75252107,
    0.72976933, 0.93364321, 0.14401492, 0.35255034, 0.68628490,
    0.76262073, 0.48124243, 0.73965093, 0.21237858, 0.63081351,
    0.75098067, 0.87658458, 0.68637267, 0.30947229, 0.19968510,
    0.59710015, 0.98464582, 0.05031455, 0.56996651, 0.74360835,
    0.30706612, 0.92693383, 0.63387122, 0.30740088, 0.46847444,
    0.99559865, 0.84777408, 0.21486266, 0.65472302, 0.51600203,
    0.3724475 , 0.0579805 , 0.62423827, 0.33997655, 0.14256265,
    0.5013935 , 0.98862076, 0.58028518, 0.15716675, 0.83572021,
    0.0119542 , 0.7257411 , 0.99901993, 0.69608303, 0.46573617
]

plt.plot(random_data, "o-");
```

To zoom on a specific portion of the plot, we call {{plt_axis}}, which takes as an argument a list containing `[xmin, xmax, ymin, ymax]`. For example, to better see the portion between $x \geq 20$ and $x \leq 30$:

```{code-cell}
plt.plot(random_data, "o-")
plt.axis([20, 30, 0, 1]);
```

### Square zoom

By default, plots are rectangular and will adapt their shape to optimize the scale on both x and y axes. However, in some circumstances, we need both x and y axes to have the same scale, e.g., to plot the (x, y) trajectory of a point in space. To set the same scale to both axes, we use `plt.axis("square")`.

For example, plotting the (x, y) coordinates of a true circle looks like an ellipse by default:

```{code-cell}
x = [ 1.        ,  0.96592583,  0.8660254 ,  0.70710678,  0.5       ,
      0.25881905,  0.        , -0.25881905, -0.5       , -0.70710678,
     -0.8660254 , -0.96592583, -1.        , -0.96592583, -0.8660254 ,
     -0.70710678, -0.5       , -0.25881905, -0.        ,  0.25881905,
      0.5       ,  0.70710678,  0.8660254 ,  0.96592583,  1.        ]
     
y = [ 0.        ,  0.25881905,  0.5       ,  0.70710678,  0.8660254 ,
      0.96592583,  1.        ,  0.96592583,  0.8660254 ,  0.70710678,
      0.5       ,  0.25881905,  0.        , -0.25881905, -0.5       ,
     -0.70710678, -0.8660254 , -0.96592583, -1.        , -0.96592583,
     -0.8660254 , -0.70710678, -0.5       , -0.25881905, -0.        ]
     
plt.plot(x, y, "o-");
```

This is solved by setting the axis to "square":

```{code-cell}
plt.plot(x, y, "o-")
plt.axis("square");
```


## 💪 Exercise

In a previous exercise, using these data:

```{code-cell} ipython3
# Video camera data
t = [0.0, 2.0, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0, 16.0, 18.0, 20.0]  # seconds
p = [0.0, 8.9, 28.0, 45.2, 60.4, 67.4, 75.5, 86.2, 93.0, 95.3, 100.0]  # metres

# Timing gates data (placed at positions 0m, 25m, 50m, 75m, and 100m)
timing_gates_time = [0.0, 2.65, 5.70, 10.25, 20.0]  # seconds
```

you generated the following figure:

```{code-cell} ipython3
:tags: [remove-input]
import matplotlib.pyplot as plt

plt.plot(t, p)
plt.plot(timing_gates_time, [0, 25, 50, 75, 100])
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True);
```

You now need to print it in black and white for publication in a journal. To maximize the clarity of the figure, you want to use markers and line styles instead of grey shades.

Generate the figure again, but this time with these specifications:

- The video camera curve must be a solid black line with square markers.
- The timing gates curve must be a dashed black line with round markers.

```{code-cell} ipython3
:tags: [hide-cell]
import matplotlib.pyplot as plt

plt.plot(t, p, "s-k")
plt.plot(timing_gates_time, [0, 25, 50, 75, 100], "o--k")
plt.title("Race profile of a sprinter")
plt.xlabel("Time (s)")
plt.ylabel("Position (m)")
plt.legend(["Video camera", "Timing gates"])
plt.grid(True);
```

