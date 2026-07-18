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


# Python basics

This section covers the very basics of Python: how to perform arithmetic operations between variables and constants, how to print information on the console, and how to document code using comments.


## Arithmetic operations

Any arithmetic operation is performed simply by writing its equation using arithmetic operators such as `+`, `-`, `*`, `/` and `**` (exponent), and parentheses `()` to indicate operation priority.

```python
# Addition

4 + 3

# Subtraction

4 - 3

# Multiplication

4 * 3

# Division

4 / 3

# Exponent

4 ** 2

# Root: we can exponentiate to the inverse. For example, to calculate
# the square root of a number, we would write:

4 ** (1 / 2)
```


## 💪 Exercise 1

Type one line in the console that performs this operation:

$$\left( \frac{3+5}{6-4} \right)^2$$

::::{dropdown} Solution
```{code-cell} ipython3
((3 + 5) / (6 - 4)) ** 2
```
::::


## Printing to the console

To print anything to the console, use the `print` function:

```{code-cell} ipython3
print(1 + 2)
print(3 + 4)
```

The `print` function works with any content, be it numbers or words:

```{code-cell} ipython3
print("Hello world")
```


:::{important}
Python is case-sensitive. This means that `a` is not the same as `A`. Consequently,

```python
Print("Hello world")
```

or

```python
PRINT("Hello world")
```

would result in an error because neither `Print` or `PRINT` exists. However,

```python
print("Hello world")
```

works.
:::

## Comments

Programs with only a few lines of code are generally easy to understand. As they grow in complexity, we need to document them, usually with comments.

Any text that follows `#` is a comment and is not executed by Python. Usually, we use comments to explain the objective of a section of code. Here are two examples of completely equivalent code, with the second using comments.

**Without comments**

```{code-cell}
print("Here is a calculation")
print(10 + 5)
```


**With comments**

```{code-cell} ipython3
# Demonstrate comments

print("Here is a calculation")  # Print some text
print(10 + 5)  # Print the result of an addition
```


## Variables

Variables are memory space to store values. For example, here are two variables, `a` and `b`, that store numbers:

```{code-cell} ipython3
a = 4
b = 3
```

Referencing a variable reads its value:

```{code-cell} ipython3
a + 1  # Since a = 4, Python calculates 4 + 1
```

```{code-cell} ipython3
a + b  # Since a = 4 and b = 3, Python calculates 4 + 3
```

To assign the result of an operation to a new variable:

```{code-cell} ipython3
c = a + b

c
```

Keep in mind that in the last example, we did not instruct Python that `c` must always be equal to `a + b`. This is not how a sequential programming language such as Python works. Instead, we instructed Python, at this very instant, to calculate the result of `a + b` and to store it in a new variable named `c`. This sequential nature is illustrated in this example:

```{code-cell} ipython3
c = c + 1  # Since c is now 7, Python calculates 7 + 1

c
```

:::{tip}
The example above can be written in a shorter form using the increment `+=` operator. Such shorthand exists for every arithmetical operation:

```python
a += b      # equivalent to a = a + b
a -= b      # equivalent to a = a - b
a *= b      # equivalent to a = a * b
a /= b      # equivalent to a = a / b
```
:::


## Choosing good variable names

It is generally a good idea to use words rather than letters for variable names. For example, this code:

```python
velocity = distance / duration
```

is clearer than:

```python
v = d / t
```

In addition, the [standard Python coding style](https://pep8.org/) recommends to use all lower case for variables, and to generally separate multiple words by underscores (`_`), e.g., `power`, `mean_power`, `peak_power`.


## 💪 Exercise 2

A sprinter runs through two timing gates spaced by 50 m as shown in {numref}`fig_exercise_timing_gates`. Each timing gate records the time (in seconds) when the sprinter passes through it.

:::{figure} fig_exercise_timing_gates
:label: fig_exercise_timing_gates
:width: 400px
Two timing gates separated by 50 meters.
:::

Given the following program:

```{code-cell} ipython3
time_gate1 = 1.3  # in seconds
time_gate2 = 6.7  # in seconds
distance_gates12 = 50.0  # in meters
```

Continue this program so that it calculates and prints the mean velocity of the sprinter between gates 1 and 2.

::::{dropdown} Solution
```{code-cell} ipython3
print(distance_gates12 / (time_gate2 - time_gate1))
```
::::

## 💪 Exercise 3

A sprinter runs a given distance $x$ to the East, then a given distance $y$ to the North (in km), as pictured in {numref}`fig_exercise_pythagore`. Use the Pythagorean theorem to complete the following program so that it prints the distance $d$ between her starting point and her final destination.

:::{figure} fig_exercise_pythagore
:label: fig_exercise_pythagore
:width: 300px
Distance between the starting point and final destination.
:::

```{code-cell} ipython3
x = 2.5  # in meters
y = 0.7  # in meters
```

::::{dropdown} Solution
```{code-cell} ipython3
d = (x**2 + y**2) ** (1 / 2)  # square root of (x^2 + y^2)

print(d)
```
::::

## Constants

Although many programming languages have different constructs for variables (values that can change) and constants (values that could not change), Python does not include the concept of a constant. Constants are saved as variables, and we simply *agree* that we will not modify them by using a **convention**:
- use `CAPITAL_CASE` for constants;
- use `lower_case` for standard variables.

For example:

```{code-cell} ipython3
GRAVITATIONAL_CONSTANT = 9.81

mass = 82  # kg
acceleration = 1.6  # m/s2
print(f"Ground reaction force = {mass * (acceleration + GRAVITATIONAL_CONSTANT)} N")
```

Regarding constants, we also recommend using these conventions:

**No magic constants**: We could have simply written 9.81 in the print call above. Instead, we defined the gravity using a name, and we used that name in the equation. We generally want to avoid "magical" constants dispersed around the code: we call them "magical" because after time, we tend to not remember what these values are for, other than making the function work "magically". Using named constants is a good way to auto-document code.

**Top of the file**: Define all the constants once and at a same obvious place, which is the top of the file.
