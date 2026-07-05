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

In section [](python_lists_modify_exercise2.md), we repeated a similar instruction multiple times:

```
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])
```

While this was perfectly fine for only three repetitions, it would not scale well for tens or even hundreds of repetitions.

When we need to repeat operations multiple times, we can use two types of loops: `while` and `for`. This section explains when and how to use each form. Looping through a dictionary will be covered later in section [](9_python_dicts.md).


## Looping using **while**

The `while` instruction repeats a code block as long as a condition is true. Its syntax is:

```
while condition:
    instruction1()
    instruction2()
    instruction3()
    ...
```

where `condition` is a [boolean variable](6_python_conditions.md). Each repetition of a code block is called an *iteration*.

Here is an example with five iterations of a code block:

```{code-cell}
i = 0

while i < 5:
    print(f"Now, the variable i is {i}.")
    i += 1

print("done")
```

We see that as long as `i` was strictly lower than 5, the `while` instruction executed the code block. When `i` equaled 5, the `(i < 5)` condition evaluated to False, and therefore the `while` instruction stopped executing the code block.

Here is a practical example where we took some measurements in metres and stored them in a list. We want to convert this list to another list where the measurements are in millimetres instead:

```{code-cell}
# Measurements in meters:
meters = [0.329, 0.009, 0.210, 0.726, 0.686, 0.912, 0.285, 0.833, 0.334, 0.165]

# Create an empty list of the same measurements in millimeters, which we will
# fill up using a while loop.
millimeters = []

# Multiply each element of meters by 1000, and append it to the millimeters list.
i = 0
while i < len(meters):
    millimeters.append(meters[i] * 1000)
    i += 1

# Done.
millimeters
```

:::{tip} Looping
While this example works perfectly well and is indeed a correct demonstration of how `while` works, we will see later that for this specific example, other methods such as using [for](python_for.md) or [NumPy](../4%20Manipulating%20Arrays%20with%20Numpy/1_numpy_intro.md) would be less error-prone and faster.
:::


## 💪 Exercise 1

Using an instrumented walkway, we recorded the following positions of heel strike, first for the right heel, then for the left heel, then for the right heel, and son on according to {numref}`fig_instrumented_walkway`.

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write a program that creates a list named `step_lengths` which contains the length of every step. The first step length should be `y[1] - y[0]`, the second should be `y[2] - y[1]`, and so on. In this specific example, we recorded nine steps, but your code should work for any number of steps.

```{code-cell}
:tags: [hide-cell]

# Initialize an empty list to put the results of our calculations
step_lengths = []

# Count the number of steps in this set of data
n_steps = len(y) - 1

# Calculate the step lengths
i = 0
while i < n_steps:
    step_lengths.append(y[i + 1] - y[i])
    i += 1

# Done
step_lengths
```

## 💪 Exercise 2

A therapist measures a patient's maximal shoulder flexion angle several times. Write a program that creates a list of all these measurements based on [user input](python_strings_input.md), as shown in the following example:

:::{admonition} Example of program output
```none
Enter max shoulder flexion (deg), or Enter to stop: <User enters 119>
Enter max shoulder flexion (deg), or Enter to stop: <User enters 124>
Enter max shoulder flexion (deg), or Enter to stop: <User enters 123>
Enter max shoulder flexion (deg), or Enter to stop: <User presses Enter>
Max shoulder flexion: [119.0, 124.0, 123.0]
```
:::

:::{tip}
The [input](python_strings_input.md) function returns an empty string `""` when the user presses Enter without entering a value.
:::

#todo put solution elsewhere

Solution:

```
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
:::


## 💪 Exercise 3

Using a force plate, we recorded the vertical ground reaction force during one step, at a sampling frequency of 20 Hz:

```{code-cell}
grf = [
    0.5, 0.9, 0.2, 0.0, 0.3, 0.2, 0.4, 0.7, 5.5, 7.1, 4.5, 37.7, 180.8,
    400.2, 603.1, 598.4, 584.2, 620.6, 635.5, 602.7, 246.0, 14.5, -1.2,
    -0.7, 0.4, 0.5, 0.8, 0.6
]
```

```{code-cell}
:tags: [remove-input]
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(len(grf))/20, grf)
plt.xlabel('Time (s)')
_ = plt.ylabel('Force (N)')
```

We consider the step to begin when the force exceeds a given threshold and to end when the falls below this threshold. Write a function `calculate_step_time` that calculates the duration of the step, and then test it with a threshold of 50 N.

```
def calculate_step_time(grf, threshold, sampling_frequency):
    """
    Calculate the step time using vertical ground reaction forces.

    Parameters
    ----------
    grf : list[float]
        A list of vertical ground reaction forces in newtons. There must
        be only one step in this list.
    threshold : float
        A value above which we consider the step begins, and below which
        the step ends.
    sampling_frequency : float
        The sampling frequency in Hz.

    Returns
    -------
    float
        The duration of the step.

    """
```

:::{tip}
- Start by finding at which index the step begins.
- From this index, find at which index the step ends.
- Calculate the step time using the difference between the indexes and the sampling frequency.
:::

```{code-cell}
:tags: [hide-cell]
def calculate_step_time(grf, threshold, sampling_frequency):
    # Find i_begin
    current_index = 0
    while grf[current_index] < threshold:
        current_index += 1
    i_begin = current_index

    # Find i_end
    while grf[current_index] >= threshold:
        current_index += 1
    i_end = current_index

    # Calculate and return the step time
    return (i_end - i_begin) / sampling_frequency

# Test it
calculate_step_time(grf, threshold=50, sampling_frequency=20)
```


## Looping using **for**

We learned to use [while](python_while.md) to repeat a code block as long as a condition is true. While the `while` statement is very powerful and sufficient for any looping, it is sometimes clearer to use the `for` statement instead.

The `for` statement means: "repeat this code block for each element in this variable".

This allows us to easily iterate through each element of a list:

```
for variable_name in the_list:
    instruction1()
    instruction2()
    instruction3()
    etc.
```

For example:

```{code-cell}
a_list = [0, 1, 2, 'three', 'four']

for item in a_list:
    print("The current item is:", item)

print("done.")
```

## 💪 Exercise 4

In section [](python_while.md), we took some measurements in metres that we needed to convert to millimetres.

```{code-cell}
meters = [0.329, 0.009, 0.210, 0.726, 0.686, 0.912, 0.285, 0.833, 0.334, 0.165]
```

Repeat this example, but using a `for` loop instead of a `while` loop.

```{code-cell}
:tags: [hide-cell]

# Create an empty list of the same measurements in millimetres, which we will
# fill up using a for loop.
millimeters = []

# Multiply each element of meters by 1000 and append it to the millimeters list.
for one_measurement in meters:
    millimeters.append(one_measurement * 1000)

# Done.
millimeters
```

:::{tip} `for` vs `while`
Note how the solution of this exercise is much clearer using `for` than `while`. We don't need to initialize an index at 0 before starting the loop, and we don't need to manually increment the index at the end of each loop. Therefore, in this case, using a `for` loop is less error-prone than using a `while` loop.

Generally:
- We use a `for` loop when we know the number of iterations in advance (in the case above, this is the length of the list);
- We use a `while` loop when we don't know in advance when the loop will stop (e.g., if the stop condition is the result of a calculation).
:::


## Looping using **for** and **range**

A range is a series of values created by specifying an (optional) initial value, a final value, and an (optional) increment. For example, `range(0, 9, 2)` creates a series of values from 0 (inclusive) to 9 (exclusive) by steps of 2. Thus, the series includes 0, 2, 4, 6, and 8. Note the similarity between expressing a range and a [slice](python_lists_slicing.md).

A range makes an ideal counter, and it is often used with `for` to repeat a code block a given number of times:

```{code-cell}
for i in range(5):  # Repeat the following code block 5 times
    print("The variable i is:", i)

print("done.")
```

In this example, the `range` function creates a sequence of values from 0 (inclusive) to 5 (exclusive), and `i` takes each of these values sequentially.

Here are different syntaxes for creating ranges:

- `range(end)`
- `range(begin, end)`
- `range(begin, end, step)`

with some examples:

```{code-cell}
# Count from 5 to 9
for i in range(5, 10):
    print("The variable i is:", i)
```

```{code-cell}
# Count from 0 to 8 by steps of 2
for i in range(0, 10, 2):
    print("The variable i is:", i)
```

```{code-cell}
# Count from 5 to 9 by steps of 2
for i in range(5, 10, 2):
    print("The variable i is:", i)
```


## 💪 Exercise 5

A therapist measures a patient's maximal shoulder flexion angle three times. Write a program that creates a list of these three measurements based on user input, as shown in the following example:

:::{admonition} Example of program output
```none
Enter max shoulder flexion (deg) [measurement 1]: <User enters 119>
Enter max shoulder flexion (deg) [measurement 2]: <User enters 124>
Enter max shoulder flexion (deg) [measurement 3]: <User enters 123>
Max shoulder flexion: [119.0, 124.0, 123.0]
```
:::


#todo put solution elsewhere

Solution:

```
# Initialize an empty list of measurements
measurements = []

# Ask the values
for i in range(3):
    str_value = input(
        f"Enter max shoulder flexion (deg) [measurement {i + 1}]: "
    )
    measurements.append(float(str_value))

# Print the result
print("Max shoulder flexion:", measurements)
```


## 💪 Exercise 6

Redo [](python_while_exercise1.md), this time using a `for` loop instead of a `while` loop:

Using an instrumented walkway, we recorded the following positions of heel strike, first for the right heel, then for the left heel, then for the right heel, and so on according to {numref}`fig_instrumented_walkway`.

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write a program that creates a list named `step_lengths` which contains the length of every step. The first step length should be `y[1] - y[0]`, the second should be `y[2] - y[1]`, and so on. In this specific example, we recorded nine steps, but your code should work on any number of steps.

```{code-cell}
:tags: [hide-cell]

# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

# Initialize an empty list to put the results of our calculations
step_lengths = []

# Count the number of steps in this set of data
n_steps = len(y) - 1

# Calculate the step lengths
for i in range(n_steps):
    step_lengths.append(y[i + 1] - y[i])

# Done!
step_lengths
```


## 💪 Exercise 7

Someone pushes a carriage using a dynamometer as shown in {numref}`fig_carriage_dynamometer`. The push force is measured in newtons every tenth of a second, over five seconds.

```{figure}
:label: fig_carriage_dynamometer
:width: 5in
![](_static/images/fig_carriage_dynamometer.png)

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

At the same time, a speed sensor reports the carriage speed in m/s, also every tenth of a second.

```{code-cell}
carriage_speed = [
    1.05, 1.08, 1.04, 1.09, 1.04, 1.06, 1.04, 1.05, 1.05, 1.05, 1.04,
    1.01, 1.09, 1.09, 1.05, 1.01, 1.06, 1.03, 1.08, 1.08, 1.09, 1.00,
    1.00, 1.00, 1.01, 1.05, 1.06, 1.03, 1.07, 1.02, 1.03, 1.07, 1.07,
    1.02, 1.04, 1.06, 1.00, 1.01, 1.00, 1.04, 1.08, 1.00, 1.02, 1.06,
    1.03, 1.06, 1.05, 1.01, 1.04, 1.00,
]
```

Write a function `calculate_power` that calculates power using the formula *power = force × speed*:

```
def calculate_power(force, speed):
    """
    Calculate the power based on force and speed.

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
```

and use it to calculate the power developed by the person to push the carriage.

```{code-cell}
:tags: [hide-cell]

def calculate_power(force, speed):
    power = []  # Initialize the output list
    
    for i in range(len(force)):
        power.append(force[i] * speed[i])

    return power

# Test the function with the supplied data
calculate_power(push_force, carriage_speed)
```


## 💪 Exercise 8


Knowing that:

```{math}
\text{speed}(t) = \left( {\text{position}(t+1) - \text{position}(t-1)} \right) * \dfrac{\text{sampling frequency}}{2}
```

write this function:

```
def calculate_speed(position, sampling_frequency):
    """
    Calculate speed based on position.

    Parameters
    ----------
    position : list[float]
        A list of positions in metres.
    sampling_frequency : float
        The frequency at which the positions were measured in Hz.

    Returns
    -------
    list[float]
        A list of speeds in m/s. This list is the same size as `position`.
        Since speed cannot be calculated for the first and last times, values
        of zero are returned for these times.
    
    """
```

and test it with the following position values that were sampled at 100 Hz:

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

:::{tip}
It will be impossible to calculate speed for the first sample because it would require the position before the first sample. It will also be impossible to calculate speed for the last sample because it would require the position after the last sample. Simply fill the first and last samples of the speed with zero as shown in {numref}`fig_padding_speed_with_zero`.
:::

```{figure}
:label: fig_padding_speed_with_zero
:width: 6in

![](_static/images/fig_padding_speed_with_zero.png)

Padding the first and last indexes of `speed` with zeros.
```


```{code-cell}
:tags: [hide-cell]
def calculate_speed(position, sampling_frequency):
    speed = [0]  # First element

    # Calculate speed for every element but first and last
    for i in range(1, len(position) - 1):
        speed.append((position[i+1] - position[i-1]) * sampling_frequency / 2)

    speed.append(0)  # Last element
    return speed

# Test this function
calculate_speed(list_of_positions, 100)
```

## Modifying a list while looping

We learned how to loop through every element of a list:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for element in the_list:
    print(element)
```

Let's see if looping through the list element allows us to not only read the list but also modify it. In this example, we want to multiply every element of `the_list` by 100:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for element in the_list:
    element = element * 100

print(f"After: {the_list}")
```

Well, it didn't work, but why? Although it is not intuitive, the line `element = element * 100` in this code means:

> "Calculate `element` times 100, and put the result in a new variable that we'll call `element`".
 
In other words, at each iteration, the name `element` is overwritten and does not refer to the list anymore. Therefore, the list is not modified.

Instead of looping trough the list elements, we could loop through the list **indexes** using a range from 0 to the end of the list:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for i in range(len(the_list)):
    the_list[i] = the_list[i] * 100

print(f"After: {the_list}")
```

It worked because at every iteration, we explicitly write to the ith element of `the_list`.


## Looping a list using **for** and **enumerate**

We learned two methods to [loop through a list](python_for_writing_list.md): looping through the list elements, which is the simplest, and looping through the list indices, which allows modifying the list.

The convenient `enumerate` function offers both advantages. When used to loop a list, it returns both the element and its index:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

for i_element, element in enumerate(the_list):
    print("The element index is", i_element)
    print("The element is", element)

```

::::{note}
This is the first time we see a function that has two return values. In reality, `enumerate` returns the tuple (`i_element`, `element`). The following code is equivalent:

```
the_list = [10, 20, 30, 40]

for one_element_tuple in enumerate(the_list):
    i_element = one_element_tuple[0]
    element = one_element_tuple[1]
    
    print("The element index is", i_element)
    print("The element is", element)

```

However, Python allows unpacking a tuple's contents into multiple variables simultaneously:

```
example_tuple = (1, 2, 3)
value1, value2, value3 = example_tuple
```

This is why the line

```
for i_element, element in enumerate(the_list):
```

works, and is much cleaner.

::::

Now, let's try [modifying a list](python_for_writing_list.md) using `enumerate`:

```{code-cell} ipython3
the_list = [10, 20, 30, 40]

print(f"Before: {the_list}")

for i_element, element in enumerate(the_list):
    the_list[i_element] = element * 100

print(f"After: {the_list}")
```

It worked, and it is indeed a cleaner code.


