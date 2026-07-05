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

# Lists and tuples

Suppose that we take three measurements of a given quantity (for instance, the height of a person). We could assign three variables for it (`height1`, `height2`, and `height3`) and write some code that processes it:

```
# Calculate the mean height
height = (height1 + height2 + height3) / 3
```

But what if we take hundreds of even thousands of measurements? At some point, it will be impossible to write clean code that processes so many variables.

Python provides powerful constructs to contain large numbers of values in a structured way, the most common being the list, the tuple and the dictionary. This section introduces the list and the tuple.


## Creating lists and tuples

As implied by its name, a list is an ordered collection of values. A tuple is also an ordered collection of values, but it cannot be modified after being created while a list can. Choosing between a list or a tuple is often philosophical:
- We normally use a tuple to express a constant using a group of variables. The coordinates of a 2D point (x, y) is a good example. Once a 2D point is defined by its two coordinates (x, y), there is no use to append a third value to it.
- We normally use a list to express an expandable list of values. A series of measurements \[x0, x1, x1, x2, x3\] is a good example. We may add or remove measurements from a list.

:::{important}
We usually use lists more often than tuples in data processing because they are more flexible. Therefore, from now on, we will focus on lists. This being said, **everything on this page also applies to tuples**.
:::

A tuple is created using parentheses `()`:

```{code-cell} ipython3
coordinates = (1.0, 5.2)
```

A list is created using square brackets `[]`:

```{code-cell} ipython3
empty_list = []
list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Lists can contain any kind of variable, even other lists or any other container type such as dictionaries:

```{code-cell} ipython3
list_of_anything = [
    "hello",            # string
    0,                  # int
    4.5,                # float
    (2 + 3j),           # complex
    False,              # bool
    [1, 2, 3],          # list
    {"key": "value"},   # dict
]
```

:::{note}
The `{"key": "value"}` syntax is a dictionary, that will be seen in section [](9_python_dicts.md).
:::

We can get the length of a list (i.e., the number of elements it contains) using the `len` function:

```{code-cell} ipython3
len(list_of_anything)
```


## Indexing a list

Every element of a list is accessible using an index. The first element is at index 0, the second at index 1, etc.

:::{note}
Zero-based addressing (first index is 0) is common in generic programming languages such as C, C++, Java, Go, PHP, Ruby, and Rust. Being a generic programming language itself, Python also uses zero-addressing. Other languages that are usually more aimed to mathematics, such as Matlab, R, Julia, and Mathematica, use one-based addressing (first index is 1). No convention is inherently better than another, but for non-programmers, it may take a bit of time to adapt to zero-based addressing.
:::

We index a list using square brackets `[]`:

```{code-cell} ipython3
list_of_strings = [
    "first element",
    "second element",
    "third element",
    "fourth element",
    "fifth element",
    "sixth element",
    "seventh element",
    "eighth element",
    "ninth element",
    "last element",
]

list_of_strings[0]
```

```{code-cell} ipython3
list_of_strings[1]
```

::::{tip}

Until you get used to zero-based addressing, you may sometimes get this error:

```
# Get the last element
list_of_strings[10]
```

Results in:

```
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
Cell In[3], line 2
      1 # Get the last element
----> 2 list_of_strings[10]

IndexError: list index out of range
```

In this case, this error happened because while the list is indeed 10-element long, the last element is at index 9, not 10.

::::

### Negative indexing

We can address a list from its last element, using negative indexing. The last element is available at index -1:

```{code-cell} ipython3
list_of_strings[-1]
```

the previous at index -2, etc.:

```{code-cell} ipython3
list_of_strings[-2]
```

### Indexing using a variable

In the examples above, we indexed a list using a literal constant. We can also index it using a variable:
```{code-cell} ipython3
i = 3
list_of_strings[i]
```

In any case, the variable must be an integer. Indeed, a list element could not be halfway between two elements.

::::{tip}
If the index is calculated using a [division](python_arithmetics.md), then the result is a float, not an integer. In this case, this statement would generate an error:

```
some_value = 6
some_string = list_of_strings[some_value / 2]
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[6], line 2
      1 some_value = 6
----> 2 list_of_strings[some_value / 2]

TypeError: list indices must be integers or slices, not float
```

This code would correct this error:

```
some_value = 6
some_string = list_of_strings[int(some_value / 2)]
```

::::

## Nested lists

As seen in section [](python_lists_creating.md), lists can be nested, which means that a list can contain another list. To access a specific element of the inner list, we start by indexing the outer list, then the inner list. For example, to access the first element of the second list of `list_of_lists`:

```{code-cell} ipython3
list_of_lists = [
    [1, 2, 3],
    ["one", "two", "three"],  # <--- "one"
    [1, 2, 3, 4, 5],
]
```

we first access the second list of `list_of_list`:

```{code-cell} ipython3
temp = list_of_lists[1]  # Second element of list_of_lists

temp
```

then we access the first element of this result:

```{code-cell} ipython3
temp[0]  # First element of the second element of list_of_lists
```

or on one line:

```{code-cell} ipython3
list_of_lists[1][0]
```

where `list_of_lists[1]` returns the list `['one', 'two', 'three']`, and `[0]` indexes this new list.


## 💪 Exercise 1

We measured some spatial parameters of gait using an instrumented walkway. This instrumented walkway stores the longitudinal distance between the origin and each heel strike in a list `y`, where each element corresponds to one heel strike, as shown in {numref}`fig_instrumented_walkway`.

```{figure}
:label: fig_instrumented_walkway
:width: 7in
![](_static/images/fig_instrumented_walkway.png)

Foot coordinates obtained via an instrumented walkway.
```

We want to calculate the step length, which is the distance between one heel strike and the next one by the opposite foot. For a given participant, we recorded this `y` list:

```{code-cell} ipython3
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write and test this function:

```
def calculate_step_length(y, step):
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y : list[float]
        A list of every heel strike's y coordinates for a given recording.
    step : int
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    float
        The requested step length.
    """
```

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_step_length(y, step):
    return y[step + 1] - y[step]

# Test it
print(calculate_step_length(y, 0))
print(calculate_step_length(y, 1))
print(calculate_step_length(y, 2))
```

## 💪 Exercise 2

You are happy with the function `calculate_step_length` you wrote in the previous exercise, but sometimes you encountered an IndexError:

```{code-cell} ipython3
:tags: [remove-cell]
def calculate_step_length(y, step):
    return y[step + 1] - y[step]
```

```{code-cell} ipython3
:tags: [raises-exception]
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

calculate_step_length(y, 9)
```

**Question 1)** Explain why this call produces an IndexError.

#todo put solution elsewhere

Solution:

This happens because to calculate a step length, two consecutive heel strikes are needed. To calculate the length of step 9, heel strikes 9 and 10 are needed. However, the last element of `y` is at index 9.

One way to avoid this error is to check that the list will not be indexed out of its range, before calculating the step length.

**Question 2)** Modify your function so that instead of producing this error, it simply returns 0.

:::{tip} Invalid data
For this example, we ask you to return 0 for invalid data, but a better practice would be to return {{np_nan}}, which will be seen in section [](../4%20Manipulating%20Arrays%20with%20Numpy/4_numpy_inf_nan.md). Simply return 0 for now since we have not covered NumPy yet.
:::

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_step_length(y, step):
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y : list[float]
        A list of every heel strike's y coordinates for a given recording.
    step : int
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    float
        The requested step length, or 0 if this step could not be calculated.
    """
    if step + 1 < len(y):
        return y[step + 1] - y[step]
    else:
        return 0.0


# Test it
print(calculate_step_length(y, 0))
print(calculate_step_length(y, 1))
print(calculate_step_length(y, 2))
print(calculate_step_length(y, 9))
```

## Slicing lists

We already learned how to [index](python_lists_indexing.md) a list by using an integer within square brackets `[]` to extract one element from a list. Sometimes, we need to extract not only one element, but a sub-list containing multiple elements. For instance, we may want to retain a certain portion of a list and discard the rest. This is done using slicing.

:::{note}
Everything on this page also applies to tuples.
:::

### Slicing syntax

The syntax for slicing is similar to indexing, the main difference being the use of a colon operator `:` inside the brackets. To extract a single element from a list, such as the 3rd element (at index 2), we would use:

```{code-cell}
list_of_strings = [
    "string 0",
    "string 1",
    "string 2",
    "string 3",
    "string 4",
    "string 5",
    "string 6",
    "string 7",
    "string 8",
    "string 9",
]

list_of_strings[2]
```

To extract a list containing the elements at indexes 2, 3, 4, 5, and 6, we would instead use:

```{code-cell}
list_of_strings[2:7]  # From index 2 (inclusive) to index 7 (exclusive)
```

This means "return a list that includes elements from index 2 up to (**but excluding**) index 7".

:::{tip}
It can be counter-intuitive that the first index is inclusive while the second is not. Here is a logical way to remember it:
- The first index is the first element that we want.
- The second index is the first element that we don't want.
:::

### Slicing step

We can extract every other element using a third integer that specifies the step to use in navigating the list. For instance, to extract a list containing the elements at indexes 2, 4, and 6:

```{code-cell}
# From index 2 (inclusive) to index 7 (exclusive), by steps of 2
list_of_strings[2:7:2]
```

To navigate a list backward, we would use a step of -1. For instance, to extract a list containing elements at indexes 6, 5, 4, 3, and 2, we would use:

```{code-cell}
# From index 6 (inclusive) to index 1 (exclusive), by steps of -1
list_of_strings[6:1:-1]
```

:::{tip}
If this last example was harder to understand, let's reuse the previous tip.
- The first index is the first element that we want. This is index 6.
- The second index is the first element that we don't want. This is index 1.
:::

### Single bounds

We can slice a list using only one bound. For example, to get every element from index 2 up to the end, we simply omit the "up to" index:

```{code-cell}
# From index 2 (inclusive)
list_of_strings[2:]
```

Similarly:

```{code-cell}
# Up to index 8 (exclusive)
list_of_strings[:8]
```

means "return a list that containing the elements up to index 8 (exclusive)". This also works with variable increments:

```{code-cell}
# From index 2 (inclusive), by steps of 2
list_of_strings[2::2]
```


## 💪 Exercise 3

Here is a list:

```{code-cell} ipython3
list_of_strings = ["zero", "one", "two", "three", "four", "five"]
```

What would be the code to transform `list_of_strings` into:

```
["five", "four", "three", "two", "one", "zero"]
```

:::{tip}
You may want to review [negative indexing](python_lists_indexing.md) again.
:::

```{code-cell} ipython3
:tags: [hide-cell]

# We start at the last element of list_of_strings.
# We can use negative indexing to get this element: -1
# Therefore, the first number of the slice (start index) is -1.

# We will go backward through the list.
# Therefore, the third number of the slice (increment) is -1.

# We go through the entire list. There is no ending point.
# Therefore, there is no second number in the slice.

list_of_strings[-1::-1]
```


## 💪 Exercise 4

Let's get back to the spatial parameters of gait measured [previously](python_lists_indexing_exercise1.md). For a given participant, we recorded this `y`:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

If we know that the first element of `y` always corresponds to the y-coordinate of the right foot, write a 2-line code that separates `y` into two lists:
- `y_right`, which contains the y-coordinates of all heel strikes for the right foot
- `y_left`, which contains the y-coordinates of all heel strikes for the left foot

```{code-cell} ipython3
:tags: [hide-cell]

y_right = y[0::2]
y_left = y[1::2]

# Print the results
print(f"Right foot: {y_right}")
print(f"Left foot: {y_left}")
```


## Modifying lists

This section shows how to modify one or many elements of a list (using indexing and slicing), how to `extend` lists or `append` data to lists, and how to remove an element from a list using `pop`.

:::{important}
Since tuples are immutable, this page does not apply to tuples.
:::

### Modifying an element

We already know how to read one element of a list using [indexing](python_lists_indexing.md) and multiple elements using [slicing](python_lists_slicing.md):

```{code-cell} ipython3
a = [1, 2, 3]

# Read the first element (indexing)
print(a[0])

# Read the first and second elements (slicing)
print(a[0:2])
```

We can also use indexing and slicing to write elements of a list.

To modify a single element using indexing:

```{code-cell} ipython3
a = [1, 2, 3]
a[0] = 10

a
```

To modify multiple elements using slicing:

```{code-cell} ipython3
a = [1, 2, 3]

# Assign 20 and 30 from `b` in place of 1 and 2 in `a`
a[0:2] = [10, 20]

a
```

### Appending an element to a list

To append a new element to a list, we use the list's `append` method, which takes the new element as an argument.

:::{admonition} Function vs method
A [function](5_python_functions.md) is a subprogram that can process arguments and return a result.

```
output = function(variable)
```

A **method** is a special type of function that is only available for a given variable type. It is called using the variable itself, using the dot `.` operator:

```
output = variable.method()
```

Methods sometimes modify the variable itself, which is the case with `append` and `extend`.

:::

```{code-cell} ipython3
a = [1, 2, 3]
print("a before =", a)

a.append(4)

print("a after =", a)
```

### Extending a list

To append multiple elements at once, we instead use the lists' `extend` method, which takes a list of new elements as an argument.

```{code-cell} ipython3
a = [1, 2, 3]
print("a before =", a)

a.extend([4, 5])

print("a after =", a)
```

### Deleting an element from a list

To remove an element at a given index, we use the list's `pop` method, which returns the element being deleted and removes it from the list.

```{code-cell} ipython3
a = [1, 2, 3]

print(a.pop(0))  # Remove the first element
print(a)
```

## 💪 Exercise 5

Here is the progression of a person's maximal flexion angle of the shoulder during a 4-month stretching program, with the outer list corresponding to the month, and the inner lists containing 10 consecutive measurements performed during each month.

```{code-cell} ipython3
max_flexion = [
    [ 98.5,  91.2,  94. ,  93.6,  98. ,  95.9,  96. ,  97. ,  99. , 103.2],
    [104.1, 105.2, 106.4, 104.6, 106. , 105.1, 108.3, 109.8, 112.2, 111.8],
    [114.9, 111.1, 112.5, 117.4, 116.8, 119.3, 118.3, 117.9, 120.8, 120.9],
    [122.3, 123.6, 123.6, 127.6, 125.4, 127. , 130.3, 129.7, 128.7, 131.2],
]
```

After verification, you realize that for the very first measurement, the instrument was not calibrated correctly and added 5 degrees to the actual angle values. Write a one-line code that corrects this measurement.

```{code-cell} ipython3
:tags: [hide-cell]

max_flexion[0][0] -= 5

# This line would be equivalent:
# max_flexion[0][0] = max_flexion[0][0] - 5

max_flexion
```


## 💪 Exercise 6

Here is the progression of a person's maximal flexion angle of the shoulder during a 4-month stretching program, with the outer list corresponding to the month, and the inner lists containing 10 consecutive measurements performed during each month.

```{code-cell} ipython3
max_flexion = [
    [ 98.5,  91.2,  94. ,  93.6,  98. ,  95.9,  96. ,  97. ,  99. , 103.2],
    [104.1, 105.2, 106.4, 104.6, 106. , 105.1, 108.3, 109.8, 112.2, 111.8],
    [114.9, 111.1, 112.5, 117.4, 116.8, 119.3, 118.3, 117.9, 120.8, 120.9],
    [122.3, 123.6, 123.6, 127.6, 125.4, 127. , 130.3, 129.7, 128.7, 131.2],
]
```

Write code that creates one single, un-nested list containing all 40 consecutive measurements.

```{code-cell} ipython3
:tags: [hide-cell]

one_list = max_flexion[0]
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])

one_list
```


## Indexing and slicing strings

We learned how to index and slice lists. The exact same behaviour applies to strings: we can extract one or many characters from a string by slicing it:

```{code-cell} ipython3
string = "This is a sample string that we will index and slice"

# Get the first character
print(string[0])

# Get the last character
print(string[-1])

# Get the first 10 characters
print(string[:10])

# Get the last 10 characters
print(string[-10:])

# Get every other character
print(string[::2])
```

