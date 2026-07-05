---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Dictionaries

The last fundamental built-in Python type is the dictionary (`dict`). Like lists and tuples, a dictionary contains any number of elements. However, lists and tuples store elements in a sequential way that we address using indices or slices, whereas dictionaries store elements non-sequentially using keys. This section introduces how to create, read, and modify dictionaries.

:::{tip}
If you come from Matlab, Python's `dict` fulfills the same role as Matlab's `struct`.
:::


## Creating dictionaries and accessing/modifying entries

A dictionary is created using curly braces `{}` and colons `:`, using a "key: value" syntax:

```{code-cell} ipython3
empty_dict = {}
dict_of_integers = {1: 11, 2: 22, 5: 55}
```

Here, we used integers for both the keys and values, but in reality:
- the key can be of many types such as integers or strings;
- the value can be of any type.

```{code-cell} ipython3
dict_of_anything = {
    1: "String for integer key 1",
    2: "String for integer key 2",
    "three": "String for string key 'three'",
    "some_int_value": 10,
    "some_float_value": 10.0,
    "some_list": [1, 3, 5, 7],
    "some_nested_dict": {
        "a": "A",
        "b": "B",
    },
}
```

To access a dictionary entry, we use `[]`, exactly as we would index a [list](7_python_lists.md):

```{code-cell} ipython3
dict_of_anything[2]
```

```{code-cell} ipython3
dict_of_anything["three"]
```

```{code-cell} ipython3
dict_of_anything["some_nested_dict"]
```

To change the value of an existing element:

```{code-cell} ipython3
dict_of_anything[2] = 66

dict_of_anything
```

We can list the available keys in a dictionary using its `keys` method:

```{code-cell} ipython3
dict_of_anything.keys()
```

or we can test if the dictionary contains a certain key using the `in` keyword:

```{code-cell} ipython3
print(1 in dict_of_anything)
print(3 in dict_of_anything)
```


## 💪 Exercise 1

Here is a list of dictionaries that contain personal information about the participants of a research project:

```{code-cell} ipython3
participants = [
    {"ID": 101, "Sex": "F", "Height": 1.45, "Weight": 56.0},
    {"ID": 125, "Sex": "M", "Height": 1.72, "Weight": 72.0},
    {"ID": 126, "Sex": "M", "Height": 1.85, "Weight": 94.0},
    {"ID": 132, "Sex": "F", "Height": 1.82, "Weight": 80.0},
]
```

Write code that calculates the average height among all participants. The number of participants may vary; therefore, your function should work for lists of any length.

```{code-cell} ipython3
:tags: [hide-cell]

# Calculate the sum
total = 0
for participant in participants:
    total += participant["Height"]

# Divide by the number of participants
average = total / len(participants)

# Show the result
print(f"The average height is {average} m.")
```


## 💪 Exercise 2

We have a list of dictionaries that contain personal information about the participants of a research project:

```{code-cell} ipython3
participants = [
    {"ID": 101, "Sex": "F", "Height": 1.45, "Weight": 56.0},
    {"ID": 125, "Sex": "M", "Height": 1.72, "Weight": 72.0},
    {"ID": 126, "Sex": "M", "Height": 1.85, "Weight": 94.0},
    {"ID": 132, "Sex": "F", "Height": 1.82, "Weight": 80.0},
]
```

Write code that iterates through all elements of this list to create a new list that contains only the participants' IDs: `[101, 125, 126, 132]`.

```{code-cell} ipython3
:tags: [hide-cell]

# Initialize an empty list
ids = []

for participant in participants:
    ids.append(participant["ID"])

# Show the result
ids
```


## 💪 Exercise 3

Someone pushes a carriage using a dynamometer as pictured in {numref}`fig_carriage_dynamometer`. The push force and position are measured in newtons and metres every tenth of a second, during five seconds.

```{code-cell}
push_force = [
    91.19, 99.22, 93.11, 91.76, 94.93, 96.54, 92.27, 96.01, 92.48,
    94.89, 91.55, 90.82, 97.91, 93.19, 95.65, 93.07, 93.65, 90.57,
    98.71, 99.97, 95.72, 96.27, 92.67, 93.4 , 98.84, 92.63, 97.03,
    93.93, 98.34, 95.82, 99.39, 99.29, 92.74, 90.29, 94.57, 90.69,
    93.16, 95.01, 93.16, 97.04, 97.23, 98.9 , 90.26, 97.46, 92.4 ,
    90.84, 97.39, 93.56, 97.47, 93.93
]

carriage_position = [
    111.5, 111.613, 111.73, 111.852, 111.98, 112.103, 112.225, 112.34,
    112.452, 112.567, 112.692, 112.818, 112.952, 113.085, 113.228, 113.37,
    113.52, 113.666, 113.813, 113.969, 114.13, 114.296, 114.454, 114.602,
    114.749, 114.887, 115.033, 115.186, 115.347, 115.511, 115.676, 115.844,
    116.017, 116.199, 116.386, 116.568, 116.745, 116.922, 117.095, 117.262,
    117.424, 117.592, 117.757, 117.931, 118.113, 118.289, 118.469, 118.644,
    118.826, 119.001
 ]
```

Write a function named `calculate_speed_and_power` with the following docstring:

```
def calculate_speed_and_power(force, position, sampling_frequency):
    """
    Calculate speed and power based on force and position.

    Parameters
    ----------
    force : list[float]
        A list of forces in newtons.
    position : list[float]
        A list of positions in meters. Its length must be the same as `force`.
    sampling_frequency : float
        The frequency at which the positions were measured in Hz.
        
    Returns
    -------
    list[dict]
        A list of the same length of `force` and `position`, that contains
        dictionaries with the following keys:
        - "Force": force in newtons
        - "Position": position in meters
        - "Speed": speed in m/s
        - "Power": power in watts.

    Example
    -------
    To get the power at the 5th sample, we would do:
    >>> data = calculate_speed_and_power(force, position, sampling_frequency)
    >>> power_5th_sample = data[4]["Power"]

    """
```

:::{tip}
You are strongly encouraged to reuse the functions `calculate_speed` and `calculate_power` that you wrote in the exercises of [](8_python_looping.md).
:::

```{code-cell}
:tags: [hide-cell]
def calculate_speed(position, sampling_frequency):
    """
    Calculate speed based on position.

    Parameters
    ----------
    position : list[float]
        A list of positions in meters.
    sampling_frequency : float
        The frequency at which the positions were measured in Hz.

    Returns
    -------
    list[float]
        A list of speeds in m/s. This list is the same length as `position`.
        Since speed cannot be calculated for the first and last times, zero
        values are returned for these times.
    
    """
    speed = [0]  # First element

    # Calculate speed for every element but first and last
    for i in range(1, len(position) - 1):
        speed.append((position[i+1] - position[i-1]) * sampling_frequency / 2)

    speed.append(0)  # Last element
    return speed


def calculate_power(force, speed):
    """
    Calculate the power according to force and speed.

    Parameters
    ----------
    force : list[float]
        A list of forces in newtons.
    speed : list[float]
        A list of speeds in m/s. Its length must be the same as force.

    Returns
    -------
    list[float]
        A list of powers in watts.

    """
    power = []  # Initialize the output list
    
    for i in range(len(force)):
        power.append(force[i] * speed[i])

    return power


def calculate_speed_and_power(force, position, sampling_frequency):
    """
    Calculate speed and power based on force and position.

    Parameters
    ----------
    force : list[float]
        A list of forces in newtons.
    position : list[float]
        A list of positions in meters. Its length must be the same as `force`.
    sampling_frequency : float
        The frequency at which the positions were measured in Hz.
        
    Returns
    -------
    list[dict]
        A list of the same length of `force` and `position`, that contains
        dictionaries with the following keys:
        - "Force": force in newtons
        - "Position": position in meters
        - "Speed": speed in m/s
        - "Power": power in watts.

    Example
    -------
    To get the power at the 5th sample, we would do:
    >>> data = calculate_speed_and_power(force, position, sampling_frequency)
    >>> power_5th_sample = data[4]["Power"]

    """
    # Calculate speed based on position
    speed = calculate_speed(position, sampling_frequency)

    # Calculate power based on speed and force
    power = calculate_power(force, speed)

    # Generate a list of dictionaries with this information
    output = []
    for i in range(len(position)):
        output.append(
            {
                "Force": force[i],
                "Position": position[i],
                "Speed": speed[i],
                "Power": power[i],
            }
        )
        
    return output


# Test it
data = calculate_speed_and_power(
    push_force,
    carriage_position,
    sampling_frequency=10
)

data[4]
```

## Adding and removing entries

Accessing a dictionary using a key that is not part of the dictionary results in a KeyError:

```{code-cell} ipython3
dict_of_integers = {1: 11, 2: 22, 5: 55}
```

```{code-cell} ipython3
:tags: [raises-exception]
dict_of_integers[3]
```

However, assigning a value to a key that does not exist **adds** this key. This is in fact how we add entries to a dictionary:

```{code-cell} ipython3
dict_of_integers[3] = 33

dict_of_integers
```

To remove an entry from a dictionary, we use the `pop` method, which behaves [like the list's pop method](python_lists_modify.md). It returns the value being deleted, and removes this entry from the dictionary.

```{code-cell} ipython3
print(dict_of_integers.pop(1))  # Remove the element with key 1
print(dict_of_integers)
```

## 💪 Exercise 4

Here is a list of dictionaries that contain personal information about the participants of a research project:

```{code-cell} ipython3
participants = [
    {"ID": 101, "Sex": "F", "Height": 1.45, "Weight": 56.0},
    {"ID": 125, "Sex": "M", "Height": 1.72, "Weight": 72.0},
    {"ID": 126, "Sex": "M", "Height": 1.85, "Weight": 94.0},
    {"ID": 132, "Sex": "F", "Height": 1.82, "Weight": 80.0},
]
```

Write code that adds a new key `BMI` to each of these dictionaries, where:

```{math}
\text{BMI} = \text{Weight}/\text{Height}^2
```

```{code-cell} ipython3
:tags: [hide-cell]

for participant in participants:
    participant["BMI"] = participant["Weight"] / (participant["Height"] ** 2)

# Show the result
participants
```


## Looping through a dictionary's entries

Similar to lists, we can loop through every element of a dictionary using the `for` instruction. The variable returned by `for` is the key. For example, to loop over every key of this dictionary:

```{code-cell} ipython3
dict_of_anything = {
    1: "String for integer key 1",
    2: "String for integer key 2",
    "three": "String for string key 'three'",
    "some_int_value": 10,
    "some_float_value": 10.0,
    "some_list": [1, 3, 5, 7],
    "some_nested_dict": {
        "a": "A",
        "b": "B",
    },
}
```

we would do:

```{code-cell} ipython3
for key in dict_of_anything:
    print(f"Key {key} contains this value: {dict_of_anything[key]}")
```


## 💪 Exercise 5

We affix an inclinometer on a person's arm. We ask the person to reach different positions in the sagittal plane as shown in {numref}`fig_shoulder_flexion_inclinometer`. Each position is reached twice.

```{figure}
:label: fig_shoulder_flexion_inclinometer
:width: 7in
![](_static/images/fig_shoulder_flexion_inclinometer.png)

Different shoulder flexion angles.
```

The inclinometer's readings are stored in degrees in a dictionary as follows:

```{code-cell} ipython3
incline = {
    "Reference": -5.0,
    "TargetA_Repetition1": 32.3,
    "TargetB_Repetition1": 73.9,
    "TargetC_Repetition1": 112.1,
    "TargetA_Repetition2": 35.7,
    "TargetB_Repetition2": 82.1,
    "TargetC_Repetition2": 105.8,
}
```

Write code that creates a new dictionary named `flexion`, that calculates the shoulder flexion angle for each repetition of TargetA, TargetB and TargetC. This new dictionary (`flexion`), will have the following form:

```
{
    "TargetA_Repetition1": (flexion angle),
    "TargetB_Repetition1": (flexion angle),
    "TargetC_Repetition1": (flexion angle),
    "TargetA_Repetition2": (flexion angle),
    "TargetB_Repetition2": (flexion angle),
    "TargetC_Repetition2": (flexion angle),
}
```

The flexion angle is calculated as the incline in the target position, minus the incline at the reference position. Your code must adapt to any number of target positions, and any number of repetitions.

```{code-cell} ipython3
:tags: [hide-cell]

# Create an empty dictionary
flexion = {}

for key in incline:
    if key != "Reference":
        flexion[key] = incline[key] - incline["Reference"]

# Show the result
flexion
```
