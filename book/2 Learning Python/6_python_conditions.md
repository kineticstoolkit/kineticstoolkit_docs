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

# Conditions and booleans

In the previous sections, we learned how to create functions to execute groups of arithmetic operations, to store variables and to print results. These examples had only one possible flow of executions.

This section shows how to build programs that are able to execute different instructions as a consequence of comparisons and conditions.


## Boolean and comparisons

Comparisons are performed using the operators `==`, `!=`, `>=`, `>`, `<=` and `<`, and always result in a variable of type boolean. We already know the following types of variable: `string`, `int`, `float` and `complex`. Boolean variables, `bool`, are the simplest: they can be either `True` or `False`.

```python
10 == 5  # False
10 != 5  # True
10 <= 5  # False
10 >= 5  # True
10 < 5   # False
10 > 5   # True
```

Obviously, comparing a constant with another constant has little sense. However, comparing variables with constants, or variables with other variables, is very common:

```{code-cell} ipython3
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
my_score > WORLD_RECORD
```

:::{important}
You may note that the equality comparison is a double-equal `==` instead of a single one `=`. This is to avoid confusion between a comparison:

```
a == 5
```
which returns `True` or `False`

and an assignment:

```
a = 5
```
which assigns the value of 5 to variable `a`.
:::

:::{tip}
Boolean values can be used in arithmetical operations: their numerical value is 0 for False, and 1 for True. For instance:

```
14 * True + 2 * False
```

14
:::


## Conditional code

Now that we know how to make comparisons, we can control the flow of the program as a result of these comparisons, using `if`:

```
if condition:
    perform_task1()
    perform_task2()
    perform_task3()
```

The `if` checks if a condition is met. The code block that follows the `if` statement is executed only if the condition evaluates to `True`.

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

```

This code did nothing, because the condition evaluated to `False`.

Using the `else` keyword, it is possible to execute one action if the condition is `True` and another action if the condition is `False`:

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

else:
    print("Nothing to see here.")

```

It is also possible to evaluate different conditions in a same `if` series, using `elif`, which stands for "else if":

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

elif my_score == WORLD_RECORD:
    print("I matched the world record!")

else:
    print("Nothing to see here.")

```

There may be more than one `elif` in a same series of comparisons:

```{code-cell}
WORLD_RECORD = 240
my_score = 236

# Verify if I broke the world record
if my_score > WORLD_RECORD:
    print("I broke the world record!")

elif my_score == WORLD_RECORD:
    print("I matched the world record!")

elif my_score > WORLD_RECORD - 5:
    print("I am near the world record!")

else:
    print("Nothing to see here.")

```


## 💪 Exercise 1

We have three timing gates. We want to know if an athlete has accelerated, decelerated, or kept a constant speed between gates 1-2 and gates 2-3.

Write a function with the following signature and docstring:

```
def compare_speed(time1, time2, time3, distance12, distance23):
    """
    Check if an athlete accelerated or decelerated based on timing gates.

    Parameters
    ----------
    time1, time2, time3 : float
        Time at which the athlete passed through timing gate 1, 2, 3,
        in seconds.
    distance12, distance23 : float
        Distance between timing gates 1 and 2; and between timing gates
        2 and 3.

    Returns
    -------
    str
        Returns "accelerated", "decelerated", or "kept constant" according
        to the calculation.

    """
```


```{code-cell} ipython3
:tags: [hide-cell]


def compare_speed(time1, time2, time3, distance12, distance23):
    """
    Check if an athlete accelerated or decelerated based on timing gates.

    Parameters
    ----------
    time1, time2, time3 : float
        Time at which the athlete passed through timing gate 1, 2, 3,
        in seconds.
    distance12, distance23 : float
        Distance between timing gates 1 and 2; and between timing gates
        2 and 3.

    Returns
    -------
    str
        Returns "accelerated", "decelerated", or "kept constant" according
        to the calculation.

    """
    speed1 = distance12 / (time2 - time1)
    speed2 = distance23 / (time3 - time2)

    if speed2 > speed1:
        return "accelerated"
    
    elif speed2 < speed1:
        return "decelerated"

    else:
        return "kept constant"


# Test the function:
print(compare_speed(1.0, 2.0, 3.0, 50, 50))
print(compare_speed(1.0, 2.0, 3.5, 50, 50))
print(compare_speed(1.0, 2.0, 2.5, 50, 50))

```



## Logical operators

We learned above how to generate boolean values (True, False) using comparison operators such as `>` (greater than) or `<=` (less or equal to). We can create more complex comparisons by combining and inverting the results of many comparisons, using the logical operators `not`, `or` and `and` as shown in {numref}`fig_logical_operators`.

```{figure}
:label: fig_logical_operators
:width: 3.5in
![](_static/images/fig_logical_operators.png)

Truth table of `not`, `or` and `and`.
```


```{code-cell}
def is_between(a, lower, upper):
    """Returns True if a is strictly between lower and upper."""
    return (a > lower) and (a < upper)


# Test the function
print(is_between(3, 2, 5))
print(is_between(10, 2, 5))
print(is_between(2, 2, 5))
```

:::{tip} Naming functions that return bools
For clarity, functions that return booleans often start with `is_`, `has_`, `contains_`, etc.
:::


## 💪 Exercise 2

Write a short code that checks the value of two integers named `dice1` and `dice2`, and that prints "You got double-six!", "You got one six!" or "You got no six." according to the dice values.

```{code-cell} ipython3
:tags: [hide-cell]

# Assign some values to dice1 and dice2
dice1 = 6
dice2 = 4

if (dice1 == 6) and (dice2 == 6):
    print("You got double-six!")
elif (dice1 == 6) or (dice2 == 6):
    print("You got one six!")
else:
    print("You got no six.")
```

