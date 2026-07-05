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

# Functions

Programming always consists in dividing complex problems into simpler ones. To this end, all programming languages provide a way to group code into bundles named functions.

A function is a subprogram that optionally takes some input, performs a given list of operations on it, and optionally returns the result as an output. The following sections will introduce how to define and document functions in Python.


## Function syntax

Functions are defined using this syntax:

```
def function_name(arg1, arg2):
    operation1()
    operation2()
    operation3()
    return the_result
```

This reads as "Define the function `function_name`, which takes `arg1`, `arg2` as inputs. This function will process these inputs and return `the_result` as an output.

:::{note}
- The inputs of a function are called **arguments** or **parameters**. Both terms are used interchangeably.
- The output of a function is called a **return value**.
:::

:::{note}
There is no minimal or maximal limit in the number of arguments. We could very well have a function with five arguments:

```
def function_name(arg1, arg2, arg3, arg4, arg5):
```
:::

Here is an example of a function that prints its arguments' values and their sum to the console and that returns nothing:

```{code-cell}
def print_sum(arg1, arg2):
    print("Hi!")
    print(f"The first variable is {arg1}.")
    print(f"The second variable is {arg2}.")
    print(f"The sum of both variables is {arg1 + arg2}.")
```

The first line of the function definition is called the **function signature**. It defines how to use the function. By reading the signature of `print_sum`, we know that the function is named `print_sum` and that it expects two arguments.

Note the colon `:` that terminates the function signature. A colon indicates that the following indented lines are a code block, which is simply a series of lines that belong to a same group. In the case of a function, this code block is the **function implementation**. These are the lines to be executed when the function is called. In Python, code blocks are delimited by their indentation. Every line of a code block must be indented with the same number of spaces.

:::{tip}
Since indentation is so important in Python, practically all Python editors include keyboard shortcuts to indent or outdent code blocks. In Spyder, select a group of lines, then press `Tab` to indent these lines altogether, or `Shift+Tab` to outdent.
:::


Once a function is defined (using the `def` keyword), it can be called as many times as needed:

```{code-cell}
print_sum(1, 4)
print_sum(3, 10)
```

:::{tip} Function naming
Usually, function names start with an active verb that tells what action is performed. Usually in Python, function names are written in `lower_case` style, with words separated by underscores.
:::


## Argument names

In this `print_sum` example, we used `arg1` and `arg2` as argument names:

```
def print_sum(arg1, arg2):
    print("Hi!")
    print(f"The first variable is {arg1}.")
    print(f"The second variable is {arg2}.")
    print(f"The sum of both variables is {arg1 + arg2}.")
```

Virtually any other name would work as well. For instance, we could use `first` and `second`, as long as we also use these names in the implementation:

```
def print_sum(first, second):
    print("Hi!")
    print(f"The first variable is {first}.")
    print(f"The second variable is {second}.")
    print(f"The sum of both variables is {first + second}.")
```

:::{tip} Clear argument names
It is important to use clear names for function arguments. Argument names are selected using the same best practices as standard [variable](python_variables.md) names.
:::


## 💪 Exercise 1

Create a function named `print_info()` that, when it is called using:

```
print_info(1, "Catherina", "Smith", 20, 1.5, 50.2)
```
    
prints this:

    =============
    Participant 1: Catherina Smith
    20 years old
    Height: 1.5 m
    Weight: 50.2 kg
    BMI: 22.31
    =============

Then try your function. Use clear names for your function's arguments.

:::{note}
The body mass index (BMI) is calculated using $\text{weight}/\text{height}^2$.
:::

::::{dropdown} Solution
```{code-cell}
def print_info(i_participant, first_name, last_name, age, height, weight):

    print("=============")
    print(f"Participant {i_participant}: {first_name} {last_name}")
    print(f"{age} years old")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {weight / (height ** 2):.2f}")
    print("=============")

print_info(1, "Catherina", "Smith", 20, 1.5, 50.2)
```
::::

## Return values

Most functions do not print results in the console. Instead, they calculate something and return the result as an output. This is done using the `return` statement. Although the following function is not that useful, it illustrates how it works:

```{code-cell}
# Define a function
def calculate_sum(arg1, arg2):
    result = arg1 + arg2
    return result

# Call the function with some values
print(calculate_sum(2, 6))
```

The function `calculate_sum()` is called with arguments 2 and 6. It executes, and then returns 8. As a result, the `print()` function prints 8.

As a second example:

```{code-cell}
print(calculate_sum(calculate_sum(2, 6), 5))
```

The inner function calls `calculate_sum()` with arguments 2 and 6. The function executes and returns 8. Then, the outer function calls `calculate_sum()` with arguments 8 and 5. The function executes again and this time returns 13. As a result, the `print()` function prints 13.


## 💪 Exercise 2

Write a function called `calculate_bmi` that takes a person's height and weight as arguments, and that returns the body mass index, knowing that $\text{BMI} = \text{weight}/\text{height}^2$.

```{code-cell}
:tags: [hide-cell]

def calculate_bmi(height, weight):
    return weight / (height ** 2)


# Let's test the function:
print(calculate_bmi(1.5, 50.2))
```


## 💪 Exercise 3

Based on the function `print_info` that you created [previously](python_functions_arguments_exercise.md), write a function named `format_info` that returns a string so that:

```
print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))
```
    
prints this:

    =============
    Participant 1: Catherina Smith
    20 years old
    Height: 1.5 m
    Weight: 50.2 kg
    BMI: 22.31
    =============

:::{tip}
You may want to return section [](4_python_strings.md) for a refresher on how to include [line breaks in strings](python_strings_long_strings.md), how to create [long strings](python_strings_long_strings.md), and how to [add variables in strings](python_strings_fstrings.md).
:::

```{code-cell} ipython3
:tags: [hide-cell]

def calculate_bmi(height, weight):
    return weight / (height ** 2)


def format_info(i_participant, first_name, last_name, age, height, weight):

    output = (
        "=============\n"
        f"Participant {i_participant}: {first_name} {last_name}\n"
        f"{age} years old\n"
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {calculate_bmi(height, weight):.2f}\n"
        "============="
    )
    return output


print(format_info(1, "Catherina", "Smith", 20, 1.5, 50.2))
```


## Docstrings

Although our solutions to the previous exercises do work, they could be much more documented. Keep in mind that code is written once, often by only one programmer, but it is read many times after, often by other people. An undocumented function is usually clear to the programmer while it is being written, but will it be months later?

Docstrings are the most important way to document functions. A docstring is  a **string** that **doc**uments a function. While being optional, it is helpful in any code other than very simple scripts. A standard docstring is a [triple-quote string](python_strings_triple_quotes.md) placed just below the function signature. Minimally, a docstring clearly indicates:

1. What the function does;
2. What are the types and contents of every expected parameter;
3. What are the type and contents of the return value, if any.

Here is what a good docstring looks like:

```{code-cell} ipython3
def format_info(i_participant, first_name, last_name, age, height, weight):
    """
    Format the provided information into a human-readable string.

    Parameters
    ----------
    i_participant : int
        Identifier for the participant
    first_name : str
        First name (given name) of the participant
    last_name : str
        Last name (surname) of the participant
    age : float
        Age of the participant, in years
    height : float
        Height of the participant, in meters
    weight : float
        Weight of the participant, in kg

    Returns
    -------
    str
        A human-readable string based on the provided information.

    """
    output = (
        "=============\n"
        f"Participant {i_participant}: {first_name} {last_name}\n"
        f"{age} years old\n"
        f"Height: {height} m\n"
        f"Weight: {weight} kg\n"
        f"BMI: {weight / (height ** 2):.2f}\n"
        "============="
    )
    return output
```

:::{note}
The style used for this docstring is [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html). There is no requirement to follow this specific style over another one, but since it is used by most major Python packages in numerical analysis (NumPy, Pandas, Matplotlib, SciPy), then we also follow this style.
:::

As you notice in the example above, there are more lines of documentation than lines of code. This is not unusual, and this is not a bad practice. After all, a well-documented, simple code is much better than an undocumented, complex code!

Since they are so ubiquitous, docstrings can be read without having to open the function's source code. Try executing the last function definition, then:

- Type `format_info` in Spyder's help browser. The docstring appears, all well-formatted, as pictured in {numref}`fig_python_function_spyder_help`.

```{figure}
:label: fig_python_function_spyder_help
:width: 5in
![](_static/images/fig_python_function_spyder_help.png)

Reading a docstring in Spyder's help pane.
```

- Or type `help(format_info)` in the console:

```{code-cell} ipython3
help(format_info)
```


## Type annotations

In addition to docstrings, type annotations (also called type hints) are increasingly popular to document the types of a function's parameters and return value.

:::{tip} Docstring vs type annotations
Always write a good docstring in the first place. Type annotations are much more optional, and at this point, knowing about type annotations is important mainly to read Python packages documentation.
:::

Type annotation allows documenting the types directly in the function signature instead of the docstring. They use `:` to document parameter types, and `->` to document return value types (see the `->` as a right-arrow):

```
def format_info(
    i_participant: int,
    first_name: str,
    last_name: str,
    age: float,
    height: float,
    weight: float
) -> str:
    """
    Format the provided information into a human-readable string.

    Parameters
    ----------
    i_participant
        Identifier for the participant
    first_name
        First name (given name) of the participant
    last_name
        Last name (surname) of the participant
    age
        Age of the participant, in years
    height
        Height of the participant, in meters
    weight
        Weight of the participant, in kg

    Returns
    -------
    str
        A human-readable string based on the provided information.

    """
```


## Positional and keyword arguments

Up to now, we called functions using an ordered list of arguments: each argument was assigned using its position. For instance, in this function:

```{code-cell} ipython3
def print_full_name(first_name, last_name):
    """Print the full name of a person."""
    print(f"{first_name} {last_name}")
```

We know that the first argument should be the first name, followed by the last name. This is known as **positional arguments**. We would call this function using:

```{code-cell} ipython3
print_full_name("Catherina", "Smith")
```


In Python, it is also possible to call functions using **keyword arguments**. To do so, we directly assign values to the argument names using `=` signs. This can make the code still clearer:

```{code-cell} ipython3
print_full_name(first_name="Catherina", last_name="Smith")
```

Note that keyword arguments can be assigned in any order:

```{code-cell} ipython3
print_full_name(last_name="Smith", first_name="Catherina")
```

For very simple functions, using keyword arguments is not that useful. However, some functions may have lots of arguments, with many of them being optional. For example, let's look at the signature of Pandas' {{pd_read_csv}} function (we will use Pandas later), in {numref}`fig_pandas_read_csv_signature`.

````{figure}
:label: fig_pandas_read_csv_signature
:width: 6in
![](_static/images/fig_pandas_read_csv_signature.png)

Signature of pandas.read_csv.
````


It has an awful lot of arguments, most of them being optional. In this case, it makes no sense to remember their order: using keyword arguments is much preferred.

:::{tip}
We can use both positional and keyword arguments in a same function call. We begin with the positional arguments, which are being assigned based on their order, and end with the keyword arguments:

```
pandas.read_csv(filename, delimiter=',')
```
:::

:::{note}
In some function signatures, you may sometimes see these symbols: `/` and `*`.
- Any argument that comes before a `/` symbol must be a positional argument.
- Any argument that comes after a `*` symbol must be a keyword argument.
:::


## Default values

In {{pd_read_csv}}, the only mandatory argument is `filepath_or_buffer`, which is the name of the csv file ({numref}`fig_pandas_read_csv_signature`). Every other argument has a default value, and exists only to modify the default behaviour of the function.

Let's examine this concept with a simpler function. We define the following function that calculates the ground reaction force based on the acceleration and mass of a person's center of mass:

```{code-cell} ipython3
GRAVITATIONAL_CONSTANT = 9.81  # m/s2


def calculate_reaction_force(mass, acceleration):
    """
    Calculate the vertical reaction force based on the mass and acceleration.

    Parameters
    ----------
    mass : float
        Mass of the person in kg.
    acceleration : float
        Acceleration of the center of mass of the person, in m/s2.

    Returns
    -------
    float
        The ground reaction force, in N.

    """
    return (mass * acceleration) + (mass * GRAVITATIONAL_CONSTANT)


# Test the function
print(calculate_reaction_force(mass=60, acceleration=3.5))
```

:::{tip} Constants
Note these conventions used for GRAVITATIONAL_CONSTANT:

**No magic constants**: Instead of writing plainly 9.81 in the function's return statement, we defined the gravity using a name, and we used that name in the equation. We generally want to avoid "magical" constants dispersed around the code: we call them "magical" because after time, we tend to not remember what these values are for, other than making the function work "magically". Using named constants is a good way to auto-document the code.

**Top of the file**: It is common practice to define all the constants once and at a same obvious place, which is the top of the file.

**CAPITAL_CASE**: In Python, a constant is simply a variable that we agree to never modify. To emphasize that it should never be modified, it is common practice to user CAPITAL_CASE to define constants, whereas we use lower_case to define standard variables.
:::

Although this function works very well as is, we may want to generalize it for different gravitational constants, to simulate a similar task in a different gravity. In this case, the gravitational constant could become a parameter of the function:

```{code-cell} ipython3
def calculate_reaction_force(mass, acceleration, gravitational_constant):
    """
    Calculate the ground reaction force based on the mass and acceleration.

    Parameters
    ----------
    mass : float
        Mass of the person in kg.
    acceleration : float
        Acceleration of the center of mass of the person, in m/s2.
    gravitational_constant : float
        Gravitational constant, in m/s2.

    Returns
    -------
    float
        The ground reaction force, in N.

    """
    return (mass * acceleration) + (mass * gravitational_constant)


# Test the function:
print(
    calculate_reaction_force(
        mass=60, acceleration=3.5, gravitational_constant=9.81
    )
)

print(
    calculate_reaction_force(
        mass=60, acceleration=3.5, gravitational_constant=5.2
    )
)
```

However, since most of the time, the gravitational constant really is 9.81 m/s², the function would be clearer with a default value for `gravitational_constant`. This is done by using an equal `=` sign in the signature:

```{code-cell} ipython3
def calculate_reaction_force(mass, acceleration, gravitational_constant=9.81):
    """
    Calculate the ground reaction force based on the mass and acceleration.

    Parameters
    ----------
    mass : float
        Mass of the person in kg.
    acceleration : float
        Acceleration of the center of mass of the person, in m/s2.
    gravitational_constant : float
        Gravitational constant, in m/s2. Default is 9.81.

    Returns
    -------
    float
        The ground reaction force, in N.

    """
    return (mass * acceleration) + (mass * gravitational_constant)
```

Now, on Earth at sea level, the function works exactly as the original one, without having to specify a gravitational constant:

```{code-cell} ipython3
print(calculate_reaction_force(mass=60, acceleration=3.5))
```

but it also adds the possibility to use other gravitational constants, using the same function:

```{code-cell} ipython3
print(
    calculate_reaction_force(
        mass=60, acceleration=3.5, gravitational_constant=5.2
    )
)
```


## 💪 Exercise 4

Let's repeat the [timing gate exercise](python_basics_exercise1.md), but this time using a proper function.

A sprinter runs through two timing gates spaced by 50 m as shown in {numref}`fig_exercise_timing_gates`. Each timing gate records the time (in seconds) at which the sprinter passes through it.

Write a function named `calculate_speed` that takes two mandatory arguments, which are the time of each timing gate, and that returns the mean velocity of the sprinter between gates 1 and 2, so that calling:

```
print(calculate_speed(1.3, 6.7))
```

prints a value of 9.2593.

In addition, this function should accommodate alternate distances between the timing gates, specified by an optional argument named `distance_gates12`:

```
calculate_speed(1.3, 6.7, distance_gates12=75)
```

Do not forget to include a docstring to your function.


```{code-cell} ipython3
:tags: [hide-cell]

def calculate_speed(time_gate1, time_gate2, distance_gates12=50):
    """
    Calculate the average velocity between two timing gates.

    Parameters
    ----------
    time_gate1, time_gate2 : float
        Time at which the athlete passed through the gate, in seconds.
    distance_gates12 : float
        Optional. Distance between both timing gates, in meters. Default is 50.

    Returns
    -------
    float
        The velocity, in m/s.

    """

    return distance_gates12 / (time_gate2 - time_gate1)


# Test the function:
print(calculate_speed(1.3, 6.7))
print(calculate_speed(1.3, 6.7, distance_gates12=75))
```

