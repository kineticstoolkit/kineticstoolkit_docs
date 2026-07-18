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

# Looping

In section [](6_python_conditions.md), we repeated a block for several iterations using the `while` keyword.

The `while` keyword is very useful when we do not know in advance how many iterations are needed. When the number of iterations is known in advance (e.g., looping through every element of a list), it is better to use `for` instead of `while`:

- `while`: Repeat a code block as long as a condition is true.
- `for`: Repeat a code block for every element of a variable.


## 💪 Exercise 1

A therapist measures a patient's maximal shoulder flexion angle several times. Write a program that creates a list of all these measurements based on user input, as shown in the following example:

:::{admonition} Example of program output
```
Enter max shoulder flexion (deg), or Enter to stop: <User enters 119>
Enter max shoulder flexion (deg), or Enter to stop: <User enters 124>
Enter max shoulder flexion (deg), or Enter to stop: <User enters 123>
Enter max shoulder flexion (deg), or Enter to stop: <User presses Enter>
Max shoulder flexion: [119.0, 124.0, 123.0]
```
:::

The number of measurements is unknown: your code must add elements to the list until the therapist presses Enter without entering a value.

:::{tip}
- You may want to see again [user input](4_python_strings.md), and [creating and adding data to lists](7_python_lists.md).
- The `input` function returns an empty string `""` when the user presses Enter without entering a value.
:::

::::{dropdown} Solution

```python
# Initialize an empty list of measurements
measurements = []

# Initialize a boolean variable that controls when we need to quit the loop
continue_asking = True

# Ask the values
while continue_asking:
    str_value = input("Enter max shoulder flexion (deg), or Enter to stop: ")
    if str_value == "":
        continue_asking = False
    else:
        measurements.append(float(str_value))

# Print the result
print("Max shoulder flexion:", measurements)
```
::::



## Looping for N iterations using `range`

When you know how many times a code block must be repeated, use the `range` keyword:

```{code-cell} ipython3
for i in range(3):
    print(f"This line is executed with i = {i}.")
```

Note that this code is exactly equivalent to this one that uses `while`:

```{code-cell} ipython3
i = 0
while (i < 3):
    print(f"This line is executed with i = {i}.")
    i += 1
```

However using `for` is a better practice here, because:
- the code intention is clearer: `for i in range(3)` literally means "loop three times";
- we do not need to manually initialize i and increment it, which is easy to forget and could lead to an infinite loop.


## 💪 Exercise 2

A therapist measures a patient's maximal shoulder flexion angle three times. Write a program that creates a list of these three measurements based on user input, as shown in the following example:

```
Enter max shoulder flexion (deg) [measurement 1/3]: <User enters 119>
Enter max shoulder flexion (deg) [measurement 2/3]: <User enters 124>
Enter max shoulder flexion (deg) [measurement 3/3]: <User enters 123>
Max shoulder flexion: [119.0, 124.0, 123.0]
```


::::{dropdown} Solution

```python
# Initialize an empty list of measurements
measurements = []

# Ask the values
for i in range(3):
    str_value = input(
        f"Enter max shoulder flexion (deg) [measurement {i + 1}/3]: "
    )
    measurements.append(float(str_value))

# Print the result
print("Max shoulder flexion:", measurements)
```
::::


## 💪 Exercise 3

Using an instrumented walkway, you recorded the following positions of heel strike, first for the right heel, then for the left heel, then for the right heel, according to [](fig_instrumented_walkway_looping).

```{figure} fig_instrumented_walkway
:label: fig_instrumented_walkway_looping
:width: 700px
Heel coordinates obtained via an instrumented walkway.
```


```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write a program that creates a list named `step_lengths` that contains the length of every step. The first step length should be `y[1] - y[0]`, the second should be `y[2] - y[1]`, and so on. In this specific example, we recorded nine steps, but your code should adapt for the length of `y` (e.g., if you recorded 15 heel strikes, your code should calculate 14 step lengths).

:::{tip}
Remember that you can obtain the length of a list using the `len` keyword.
:::

::::{dropdown} Solution
```{code-cell}
# Initialize an empty list to put the results of our calculations
step_lengths = []

# Count the number of steps in this set of data
n_steps = len(y) - 1

# Calculate the step lengths
for i in range(n_steps):
    step_lengths.append(y[i + 1] - y[i])

# Done
step_lengths
```
::::



## 💪 Exercise 4

Write a function that calculate speed based on position, using the central difference method:

```{math}
\text{speed}(t) = \left( {\text{position}(t+1) - \text{position}(t-1)} \right) * \dfrac{\text{sampling frequency}}{2}
```

The docstring of this function is:

```python
def calculate_speed(
    position: list[float],
    sampling_frequency: float
) -> list[float]:
    """
    Calculate speed based on position.

    Parameters
    ----------
    position
        A list of positions in metres.
    sampling_frequency
        The frequency at which the positions were measured in Hz.

    Returns
    -------
    list[float]
        A list of speeds in m/s. This list is the same size as `position`.
        Since speed cannot be calculated for the first and last times, values
        of zero are returned for these times.
    
    """
```

Then test it with the following position values that were sampled at 100 Hz:

```{code-cell}
list_of_positions = [
    30.5, 30.511, 30.523, 30.535, 30.548, 30.56, 30.572, 30.584, 30.595, 30.606,
    30.619, 30.631, 30.645, 30.658, 30.672, 30.687, 30.702, 30.716, 30.731,
    30.746, 30.763, 30.779, 30.795, 30.81, 30.824, 30.838, 30.853, 30.868, 30.884,
    30.901, 30.917, 30.934, 30.951, 30.969, 30.988, 31.006, 31.024, 31.042, 31.059,
    31.076, 31.092, 31.109, 31.125, 31.143, 31.161, 31.178, 31.196, 31.214, 31.232,
    31.25
]
```

::::{tip}
It is impossible to calculate speed for the first sample because it would require the position before the first sample. It will also be impossible to calculate speed for the last sample because it would require the position after the last sample. Simply fill the first and last samples of the speed with zero as shown in [](fig_padding_speed_with_zero).

```{figure} fig_padding_speed_with_zero
:label: fig_padding_speed_with_zero
:width: 500px
Padding the first and last indexes of `speed` with zeros.
```

::::

::::{dropdown} Solution
```{code-cell}
def calculate_speed(
    position: list[float],
    sampling_frequency: float
) -> list[float]:
    """
    Calculate speed based on position.

    Parameters
    ----------
    position
        A list of positions in metres.
    sampling_frequency
        The frequency at which the positions were measured in Hz.

    Returns
    -------
    list[float]
        A list of speeds in m/s. This list is the same size as `position`.
        Since speed cannot be calculated for the first and last times, values
        of zero are returned for these times.
    
    """
    speed = [0]  # First element

    # Calculate speed for every element but first and last
    for i in range(len(position) - 2):
        speed.append((position[i+2] - position[i]) * sampling_frequency / 2)

    speed.append(0)  # Last element
    return speed

# Test this function
calculate_speed(list_of_positions, 100)
```
::::


## Looping through a list

You can use `range` and `len` to read each element of a list, as you did in the previous exercises:

```{code-cell} ipython3
some_list = [1.0, 2.0, 3.0]

for index in range(len(some_list)):
    print(some_list[index])
```

However, in this case, we don't really need the index, apart from indexing the list. A much simpler method is to simply loop through the list itself instead of a range:

```{code-cell} ipython3
some_list = [1.0, 2.0, 3.0]

for element in some_list:
    print(element)
```

::::{attention}
Looping using this method only works for reading a list, not for modifying it. Let's see why.

Suppose we want to multiply every element of `some_list` by 10:

```{code-cell} ipython3
some_list = [1.0, 2.0, 3.0]

for element in some_list:
    element = element * 10

some_list
```


This did not work and the reason is not intuitive. The line `element = element * 100` in this code means "Calculate `element` times 100, and put the result in a new variable that we'll call `element`". In other words, at each iteration, the name `element` is overwritten and does not refer to the list anymore. Therefore, the list is not modified.

**Easy fix:** To write to a list, use its index:

```{code-cell} ipython3
some_list = [1.0, 2.0, 3.0]

for index in range(len(some_list)):
    some_list[index] = some_list[index] * 10

some_list
```

::::





## 💪 Exercise 5

You took some measurements in metres and need to convert them to millimetres.

```{code-cell}
meters = [0.329, 0.009, 0.210, 0.726, 0.686, 0.912, 0.285, 0.833, 0.334, 0.165]
```

By looping through this list, create another one named `millimeters` than contains the same measurement but in millimetres instead.

::::{dropdown} Solution
```{code-cell}
# Create an empty list of the same measurements in millimetres, which we will
# fill up using a loop.
millimeters = []

# Multiply each element of meters by 1000 and append it to the millimeters list.
for one_measurement in meters:
    millimeters.append(one_measurement * 1000)

# Done.
millimeters
```
::::


## 💪 Exercise 6

Someone pushes a carriage using a dynamometer as shown in [](fig_carriage_dynamometer).

```{figure} fig_carriage_dynamometer
:label: fig_carriage_dynamometer
:width: 500px
Pushing a carriage using a dynamometer.
```


```{code-cell}
push_force = [
    91.19, 99.22, 93.11, 91.76, 94.93, 96.54, 92.27, 96.01, 92.48,
    94.89, 91.55, 90.82, 97.91, 93.19, 95.65, 93.07, 93.65, 90.57,
    98.71, 99.97, 95.72, 96.27, 92.67, 93.4 , 98.84, 92.63, 97.03,
    93.93, 98.34, 95.82, 99.39, 99.29, 92.74, 90.29, 94.57, 90.69,
    93.16, 95.01, 93.16, 97.04, 97.23, 98.9 , 90.26, 97.46, 92.4 ,
    90.84, 97.39, 93.56, 97.47, 93.93
]
```

At the same time, a synchronized speed sensor reports the carriage speed in m/s.

```{code-cell}
carriage_speed = [
    1.05, 1.08, 1.04, 1.09, 1.04, 1.06, 1.04, 1.05, 1.05, 1.05, 1.04,
    1.01, 1.09, 1.09, 1.05, 1.01, 1.06, 1.03, 1.08, 1.08, 1.09, 1.00,
    1.00, 1.00, 1.01, 1.05, 1.06, 1.03, 1.07, 1.02, 1.03, 1.07, 1.07,
    1.02, 1.04, 1.06, 1.00, 1.01, 1.00, 1.04, 1.08, 1.00, 1.02, 1.06,
    1.03, 1.06, 1.05, 1.01, 1.04, 1.00,
]
```

Write a function `calculate_power` that calculates power using this formula:

$$
\text{power} = \text{force} \times \text{speed}
$$


```python
def calculate_power(force: list[float], speed: list[float]) -> list[float]:
    """
    Calculate the power based on force and speed.

    Parameters
    ----------
    force
        A list of forces in newtons.
    speed
        A list of speeds in m/s. Its length must be the same as force.

    Returns
    -------
    list[float]
        A list of powers in watts.

    """
```

and use it to calculate the power developed by the person to push the carriage.

::::{dropdown} Solution

```{code-cell}
def calculate_power(force: list[float], speed: list[float]) -> list[float]:
    """
    Calculate the power based on force and speed.

    Parameters
    ----------
    force
        A list of forces in newtons.
    speed
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

# Test the function with the supplied data
calculate_power(push_force, carriage_speed)
```

::::


## 💪 Exercise 7

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

::::{dropdown} Solution
```{code-cell} ipython3
# Calculate the sum
total = 0
for participant in participants:
    total += participant["Height"]

# Divide by the number of participants
average = total / len(participants)

# Show the result
print(f"The average height is {average} m.")
```
::::


## Looping through a list using `enumerate`

If you need both the index and the value, use `enumerate`:

```{code-cell} ipython3
some_list = [10, 20, 30, 40]

for i_element, element in enumerate(some_list):
    print("The element index is", i_element)
    print("The element is", element)
```

::::{note}
This is the first time we see a function that has two return values. In reality, `enumerate` returns the tuple (`i_element`, `element`), and Python allows unpacking a tuple's contents into multiple variables simultaneously:

```python
example_tuple = (1, 2, 3)
value1, value2, value3 = example_tuple
```

Here, we unpack the tuple returned by `enumerate` in two variables:

```python
for i_element, element in enumerate(the_list):
```

::::


## Looping through a dict

Similar to lists, you can loop through every element of a dictionary using the `for` instruction, which returns every key one by one:

```{code-cell} ipython3
some_dict = {
    "one": 1.0,
    "two": 2.0,
    "three": 3.0,
    "four": 4.0,
}

for key in some_dict:
    print(f"Key {key} contains this value: {some_dict[key]}")
```


## Looping through a dict using `items`

Similar to `enumerate`, you can access both the key and value using the `items` method:

```{code-cell} ipython3
for key, value in some_dict.items():
    print(f"Key {key} contains this value: {value}")
```
