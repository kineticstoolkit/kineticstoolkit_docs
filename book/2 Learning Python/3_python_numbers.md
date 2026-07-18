---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: python 3 (ipykernel)
  language: python
  name: python3
---

# Numbers

Numbers belong to different sets, each fulfilling a different role. Python provides three sets of numbers:

- Integer numbers: `int`
- Real numbers: `float`
- Complex numbers: `complex`

```{figure} fig_number_sets
:label: fig_number_sets
:width: 500px
The three sets of numbers in Python.
```

This book focus only on integers and real numbers (floats).


## Integers (`int`)


Integers are generally used to represent ranks, indexes, counts:

- An index in a list (e.g, 5th value of a list)
- A number of repetitions
- A number of events
- The size of a vector
- The length of a list
- etc.

Any number that does not contain a decimal point is considered an `int` by Python:

```{code-cell} ipython3
some_int = 3
```


## Floats (`float`)

Floats are generally used to represent real, physical values:

- A force in newtons
- A distance in meters
- A power in watts
- An angle in radians
- etc.

Any number that contains a decimal point is considered a `float` by Python:

```{code-cell} ipython3
some_float = 3.0
```

Use `type` or `isinstance` to know the type of a variable:

```{code-cell}
print(type(some_int))
print(type(some_float))
```

or `isinstance`:

```{code-cell}
print(isinstance(some_int, int))  # Is it an integer?
print(isinstance(some_int, float))  # Is it a float?
```


## Converting between integers and floats

Use `float()` to convert a value to a float:

```{code-cell} ipython3
some_int = 3

float(some_int)
```

Use `int()` to convert a value to an integer. Note however that the decimal component of the number will be lost:

```{code-cell} ipython3
some_float = 3.1416

int(some_float)
```



## Arithmetic operations between integers and floats

When we perform operations between different types, Python may automatically convert integers to floats to ensure that the result holds the correct value. For example, adding an integer to another integer results in an integer:

```{code-cell} ipython3
a = 2 + 4

type(a)
```

However, adding a float to an integer results in a float:

```{code-cell} ipython3
b = 2 + 4.5

type(b)
```

A special case is the division, which always results in a float, even if we divide two integers, and even if the result is round:

```{code-cell} ipython3
c = 4 / 2

type(c)
```


## 💪 Exercise

We want to create a variable named `mass` that will contain the mass of a person in kg. This person has a mass of 68 kg. Since this is a physical value, it should be a float, hence the decimal point:

```python
mass = 68.0
```

How would you create the following variables?

- `hip_height`: The height of the hip in standing position, which is 1 m.
- `i_trial`: The trial number where someone reached the highest isometric contraction, which is 3.
- `n_trials`: The total number of trials someone tried to reach the highest isometric contraction, which is 4.
- `emg_max`: The EMG value measured during a maximal isometric contraction, which is 34 μV.

::::{dropdown} Solution
```python
hip_height = 1.0
i_trial = 3
n_trials = 4
emg_max = 34.0
```
::::
