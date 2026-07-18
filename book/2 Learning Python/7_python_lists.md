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

You take three measurements of a given quantity (for instance, the height of a person). We could assign three variables for it (`height1`, `height2`, and `height3`) and write some code that processes it:

```python
# Calculate the mean height
height = (height1 + height2 + height3) / 3
```

But what if we take hundreds of even thousands of measurements? It will be impossible to write clean code that processes so many variables. Python provides powerful constructs to contain large numbers of values in a structured way, the most common being the list, the tuple and the dictionary. This section introduces the list and the tuple.


## Creating lists and tuples

Both lists and tuples are an ordered collection of values. The main  difference is that a list can be modified after being created, while a tuple cannot. Choosing between a list or a tuple is often philosophical:
- We normally use a tuple to express one variable that requires several values. A 2D point is a good example: it is defined by its two coordinates `(x, y)`, and it would be illogical to append a third value to it since it would not be a 2D point anymore.
- We normally use a list to express an expandable list of values. A series of measurements `[x0, x1, x1, x2, x3]` is a good example. We may add or remove measurements from a list.

A tuple is created using parentheses `()`:

```{code-cell} ipython3
coordinates = (1.0, 5.2)
```

A list is created using square brackets `[]`:

```{code-cell} ipython3
list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Lists and tuples can contain any variable type:

```{code-cell} ipython3
list_of_anything = [
    "hello",            # string
    0,                  # int
    4.5,                # float
]
```

:::{tip}
You learned in section [](5_python_functions.md) how to add type annotations to function arguments. You can also add type annotations to variables. Such annotations are totally optional, but they tend to add clarity to your code as it grows.

```{code-cell} ipython3
# No type annotation
list1 = [1, 2, 3, 4]

# This list contains only integers
list2 : list[int] = [1, 2, 3, 4]

# This list contains both integers and strings
list3 : list[int|str] = [1, 2, 3, "four"]
```

On a first look, the annotations above look futile since we already see the contents of the list. But in many situations, you will construct an empty list that will grow later in the code. Type annotations are a great way to remember the structure of these lists.

```{code-cell} ipython3
# We don't know what this list will contain
list1 = []

# This list will contain only integers
list2 : list[int] = []

# This list will contain both integers and strings
list3 : list[int|str] = []
```

:::


Use the `len` function to get the number of elements in a list:

```{code-cell} ipython3
some_list = [1, 2, 3, 4]

len(some_list)
```


## Reading one element of a list/tuple using an index

Every element of a list/tuple is accessible using an index placed between square brackets `[]`. The first element is at index 0, the second at index 1, etc.:

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

The same applies to tuples:

```{code-cell} ipython3
coordinates = (0.1, 0.2)

x = coordinates[0]
y = coordinates[1]

print(f"x = {x};  y = {y}")
```


### Negative indexing

You can access a list element using its position starting from the end rather than from the beginning, using negative indexing. The last element is available at index -1:

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
If the index is calculated using a [division](python_arithmetics.md), then the result is a float and not an integer, even if the result is round. This statement would generate an error:

```{code-cell} ipython3
:tags: [raises-exception]

twice_the_index = 6

list_of_strings[twice_the_index / 2]
```

It is generally a good idea to explicitly convert the result of a calculation to an integer, which corrects this error:

```{code-cell} ipython3
twice_the_index = 6

list_of_strings[int(twice_the_index / 2)]
```

::::

## 💪 Exercise 1

Using an instrumented walkway, you measured the longitudinal distance between the heel and the origin for each heel strike. This distance was saved in a list named `y`, where each element corresponds to one heel strike, as shown in [](fig_instrumented_walkway).

```{figure} fig_instrumented_walkway
:label: fig_instrumented_walkway
:width: 700px
Heel coordinates obtained via an instrumented walkway.
```

You want to calculate the step length, which is the distance between one heel strike and the next one by the opposite foot, for this `y` list:

```{code-cell} ipython3
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

Write and test this function:

```python
def calculate_step_length(y: list[float], step: int) -> float:
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y
        A list of every heel strike's y coordinates for a given recording.
    step
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    The requested step length.
    """
```

::::{dropdown} Solution
```{code-cell} ipython3
def calculate_step_length(y: list[float], step: int) -> float:
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y
        A list of every heel strike's y coordinates for a given recording.
    step
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    The requested step length.
    """
    return y[step + 1] - y[step]

# Test it
print(f"First step:  {calculate_step_length(y, 0): .2f} meters")
print(f"Second step: {calculate_step_length(y, 1): .2f} meters")
print(f"Third step:  {calculate_step_length(y, 2): .2f} meters")
```
::::

## 💪 Exercise 2

You are happy with the function `calculate_step_length` you wrote in the previous exercise, but sometimes you encounter an IndexError:

```{code-cell} ipython3
:tags: [raises-exception]
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]

calculate_step_length(y, 9)
```

**Question 1)** Explain why this call produces an IndexError.

::::{dropdown} Solution
This happens because to calculate a step length, two consecutive heel strikes are needed. To calculate the length of step 9, heel strikes 9 and 10 are needed. However, the last element of `y` is at index 9.

One way to avoid this error is to check that the list will not be indexed out of its range, before calculating the step length.
::::

**Question 2)** Modify your function so that instead of producing this error, it simply returns 0.

::::{dropdown} Solution
```{code-cell} ipython3
def calculate_step_length(y: list[float], step: int) -> float:
    """
    Calculate the step length of a given step.

    Parameters
    ----------
    y
        A list of every heel strike's y coordinates for a given recording.
    step
        The index of the step we want to calculate, the first step being 0.

    Returns
    -------
    The requested step length.
    """

    if step + 1 < len(y):
        return y[step + 1] - y[step]
    else:
        return 0.0


# Test it
print(f"First step:  {calculate_step_length(y, 0): .2f} meters")
print(f"Second step: {calculate_step_length(y, 1): .2f} meters")
print(f"Third step:  {calculate_step_length(y, 2): .2f} meters")
print(f"Tenth step:  {calculate_step_length(y, 10): .2f} meters")
```
::::


:::{tip}
Although in this example, we asked you to return 0.0 for invalid data, a better practice would be to return {{np_nan}}, which will be seen in section [](../4%20Manipulating%20Arrays/4_numpy_inf_nan.md).
:::


## Nested lists

Since container variables such as lists and tuples may contain any variable type, then a list can contain lists. In other terms, inner lists are **nested** into an outer lists.

```{code-cell} python3
list_of_lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
```

As you can expect, nested lists are strongly related to matrices, which will be seen in section [](../4%20Manipulating%20Arrays/2_numpy_ndarray.md).

To access a specific element of a nested list, we start by indexing the outer list, then the inner list. For example, to access element 4 of `list_of_lists`, we first access the second inner of `list_of_list`:

```{code-cell} ipython3
temp = list_of_lists[1]  # Second element of list_of_lists

temp
```

then we access the first element of this result:

```{code-cell} ipython3
temp[0]  # First element of the second element of list_of_lists
```

or in just one line:

```{code-cell} ipython3
list_of_lists[1][0]
```

where `list_of_lists[1]` returns the list `[4, 5, 6]`, and `[0]` indexes this new list.



## Reading many elements of a list/tuple using a slice

You now how to read one element in a list or tuple using an integer between brackets `[]`. Sometimes, we need to read many elements at once. This is done using slicing.

### Slicing syntax

The syntax for slicing is similar to indexing, the main difference being the use of a colon operator `:` inside the brackets. From this example list:

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
```

we can extract a list that contains the elements at indexes 2, 3, 4, 5, and 6 using:

```{code-cell}
list_of_strings[2:7]  # From index 2 (inclusive) to index 7 (exclusive)
```

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

To get every element from index 2 up to the end (no upper bound), we simply omit the "up to" index:

```{code-cell}
# From index 2 (inclusive)
list_of_strings[2:]
```

Similarly, to get every elements up to index 8 (no lower bound), we omit the "from" index:

```{code-cell}
# Up to index 8 (exclusive)
list_of_strings[:8]
```

This also works with variable increments:

```{code-cell}
# From index 2 (inclusive) up to the end, by steps of 2
list_of_strings[2::2]
```


## 💪 Exercise 3

Here is a list:

```{code-cell} ipython3
list_of_strings = ["zero", "one", "two", "three", "four", "five"]
```

Write one line of code that creates this list out of `list_of_strings`:

```python
["one", "two", "three"]
```

::::{dropdown} Solution
```{code-cell} ipython3
list_of_strings[1:4]
```
::::


## 💪 Exercise 4

Here is a list:

```{code-cell} ipython3
list_of_strings = ["zero", "one", "two", "three", "four", "five"]
```

Write one line of code that creates this list out of `list_of_strings`:

```python
["five", "four", "three", "two", "one", "zero"]
```


::::{dropdown} Solution
```{code-cell} ipython3
list_of_strings[5::-1]
```

We could also use negative indexing to start from the end (-1), up to the beginning (no index), by steps of -1:

```{code-cell} ipython3
list_of_strings[-1::-1]
```
::::


## 💪 Exercise 5

Let's get back to the y coordinates measured using an instrumented walkway in Exercise 1 (Fig. [](fig_instrumented_walkway)). For a given participant, you recorded:

```{code-cell}
# y-coordinates of each heel strike, in meters
y = [0.13, 0.72, 1.29, 1.93, 2.55, 3.12, 3.71, 4.34, 4.95, 5.56]
```

You know that the first element of `y` corresponds to the y-coordinate of the right heel. Write a 2-line code that separates `y` into two lists:
- `y_right`, which contains the y-coordinates of all heel strikes for the right heel
- `y_left`, which contains the y-coordinates of all heel strikes for the left heel

::::{dropdown} Solution
```{code-cell} ipython3
y_right = y[0::2]
y_left = y[1::2]

# Print the results
print(f"Right foot: {y_right}")
print(f"Left foot: {y_left}")
```
::::


::::{tip}
You learned how to index and slice lists. The same behaviour applies to strings! You can extract one or many characters from a string by indexing or slicing it.

```{code-cell} ipython3
string = "This is a sample string that we will index and slice"
```

Read the first character:

```{code-cell} ipython3
string[0]
```

Read the last character:

```{code-cell} ipython3
string[-1]
```

Read the 10 first characters:

```{code-cell} ipython3
string[:10]
```

Read the 10 last characters:

```{code-cell} ipython3
string[-10:]
```

Reverse the string:

```{code-cell} ipython3
string[-1::-1]
```
::::



## Modifying lists

You know how to read a list by indexing or slicing it. Now you will learn how to write to a list.


### Modifying one element of a list using an index

We modify an element of a list the same way we read it, by indexing the list with an integer:

```{code-cell} ipython3
one_list = [1, 2, 3]

# Write 10 to index 0 of one_list
one_list[0] = 10

one_list
```


### Modifying many elements of a list using a slice

Similarly, we modify multiple elements simultaneously using a slice:

```{code-cell} ipython3
one_list = [1, 2, 3]

# Write 10 and 20 to index 0 and 1 of one_list
one_list[0:2] = [10, 20]

one_list
```


### Adding one element to a list

To append a new element to a list, use the list's `append` method, which takes the new element as an argument.

:::{note}
A **function** is a subprogram that can process arguments and return a result (Section [](5_python_functions.md)).

```python
output = function(variable)
```

A **method** is a special type of function that is only available for a given variable type. It is called from the variable instance, using the dot `.` operator:

```python
output = variable.method()
```

Methods sometimes modify the variable, which is the case with `append` and `extend`.

:::

```{code-cell} ipython3
one_list = [1, 2, 3]
print(f"before: {one_list}")

one_list.append(4)
print(f"after: {one_list}")
```


### Adding many elements to a list

To append multiple elements at once, use the lists' `extend` method, which takes a list of new elements as an argument.

```{code-cell} ipython3
one_list = [1, 2, 3]
print(f"before: {one_list}")

one_list.extend([4, 5])
print(f"after: {one_list}")
```


### Removing an element from a list

Use the list's `pop` method:

```{code-cell} ipython3
one_list = [1, 2, 3]
print(f"before: {one_list}")

removed_element = one_list.pop(0)

print(f"removed: {removed_element}")
print(f"after: {one_list}")
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

After verification, you realize that for the very first measurement, the instrument was not calibrated correctly and added 5 degrees to the actual angle values. Write a one-line code that corrects this measurement.

::::{dropdown} Solution
```{code-cell} ipython3
max_flexion[0][0] -= 5

# This line would be equivalent:
# max_flexion[0][0] = max_flexion[0][0] - 5

max_flexion
```
::::


## 💪 Exercise 7

Here is the progression of a person's maximal flexion angle of the shoulder during a 4-month stretching program, with the outer list corresponding to the month, and the inner lists containing 10 consecutive measurements performed during each month.

```{code-cell} ipython3
max_flexion = [
    [ 93.5,  91.2,  94. ,  93.6,  98. ,  95.9,  96. ,  97. ,  99. , 103.2],
    [104.1, 105.2, 106.4, 104.6, 106. , 105.1, 108.3, 109.8, 112.2, 111.8],
    [114.9, 111.1, 112.5, 117.4, 116.8, 119.3, 118.3, 117.9, 120.8, 120.9],
    [122.3, 123.6, 123.6, 127.6, 125.4, 127. , 130.3, 129.7, 128.7, 131.2],
]
```

Write code that creates a single, flat (not nested) list containing all 40 consecutive measurements.

::::{dropdown} Solution
```{code-cell} ipython3
one_list = max_flexion[0]
one_list.extend(max_flexion[1])
one_list.extend(max_flexion[2])
one_list.extend(max_flexion[3])

one_list
```
::::


