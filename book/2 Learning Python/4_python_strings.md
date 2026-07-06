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

# Strings

In the previous section, we introduced two types of variables that express numbers: `int` and `float`. To express letters, words, and sentences, we use the `string` type. This section explains different methods to create strings, and how to combine strings and numbers.


## Single and double quotes

A string is created by enclosing characters between quotes. Python does not make a difference between single-quotes `'` and double-quotes `"`. Therefore, the following strings are equivalent:

```{code-cell}
s1 = "Hello world!"
s2 = 'Hello world!'
```

Normally, we use double-quotes if the string contains apostrophes `'`; conversely, we use single-quotes if the string contains double-quotes `"`. For instance, both these strings are correctly defined:

```{code-cell}
s3 = "It's time for lunch."
s4 = 'I would not call it "results"...'
```

but the following ones generate syntax errors, because the apostrophe or double-quote closes the string before reaching the ending delimiter:

```{code-cell}
:tags: [raises-exception]
s5 = 'It's time for lunch'
s6 = "I would not call it "results"..."
```


## 💪 Exercise 1

Write a line of code that creates the variable `some_string` so that:

```python
print(some_string)
```

gives:

```
I won't have difficulty solving this problem.
```

::::{dropdown} Solution
```{code-cell} ipython3
some_string = "I won't have difficulty solving this problem."
print(some_string)
```
::::

## 💪 Exercise 2

Write a line of code that creates the variable `some_string` so that:

```python
print(some_string)
```

gives:

```
Centre of mass of the "arm + forearm" segment.
```

::::{dropdown} Solution
```{code-cell} ipython3
some_string = 'Centre of mass of the "arm + forearm" segment.'
print(some_string)
```
::::



## Backslash

Inserting a backslash `\` in a string tells Python that the following character is a special character. It may be used to enter quotes, line breaks or backslashes in a string.

### Single and double-quotes

If a single string needs to include both apostrophes and double-quotes, then it is impossible to select a correct delimiter. Backslashing a quote character (`\'`, `\"`) tells Python that this really is a character, and not a delimiter. For instance:

```{code-cell} ipython3
example1 = "I didn't write \"E = mc2\", Einstein did."
example2 = 'I didn\'t write "E = mc2", Einstein did.'

print(example1)
print(example2)
```

### Line break: `\n`

Newline characters are inserted using `\n`:

```{code-cell} ipython3
example_string = "I ate your sandwich.\nIt tasted good."

print(example_string)
```

### Backslash: `\\`

To include a backslash in the string, we need to backslash it so that Python sees it as a character instead of a backslash command:

```{code-cell} ipython3
file_path = "C:\\Windows\\important_driver.dll"

print(file_path)
```


## Triple-quotes

Python provides another type of string delimiter: the triple-quote. Triple-quoted strings can integrate both single and double quotes:

```{code-cell}
s1 = """I didn't write "E = mc2", that's Einstein's thing."""

print(s1)
```

They also don't need `\n` for line breaks, we simply do literal line breaks.

```{code-cell} ipython3
s2 = """I ate your sandwich.
It tasted good."""

print(s2)
```

The most common use for triple-quotes are docstrings, which will be seen later in [](5_python_functions.md).


## 💪 Exercise 3

Write a line of code that creates the variable `some_string` so that:

```python
print(some_string)
```

gives:

```
I received this strange message:
"ValueError('C:\temp unfound')"
```

::::{dropdown} Solution
Some alternatives:
```{code-cell} ipython3
some_string = "I received this strange message:\n\"ValueError('C:\\temp unfound')\""

some_string = 'I received this strange message:\n"ValueError(\'C:\\temp unfound\')"'

some_string = '''I received this strange message:
"ValueError('C:\\temp unfound')"'''

print(some_string)
```
::::


## Creating long strings

Normally, we want to avoid very long code lines. It is common practice to limit the width of a line to 80 characters.

Following this limit may be difficult when creating long strings. To achieve this, we can split a long string on multiple lines, by enclosing multiple sub-strings between parentheses.

```{code-cell} ipython3
long_string = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do "
    "eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim "
    "ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut "
    "aliquip ex ea commodo consequat."
)

print(long_string)
```


## Including variables in strings using f-strings

We often use strings to report results:

```
"The calculated ankle moment is 100.1 Nm."
```

A good method to include the value of a variable into a string is to use an f-string (for *formatted string*), which are defined by prefixing the string with the letter `f`. With f-strings, Python evaluates the result of any instruction placed between curly braces `{}`:

```{code-cell} ipython3
ankle_moment = 100.1

the_string = (
    f"The calculated ankle moment is {ankle_moment} Nm."
)

print(the_string)
```

When an f-string contains a float, we can print it to a given precision, using `:.xf` just after the expression in braces, where `x` is the number of digits after the decimal point:

```{code-cell}
print(f"The calculated ankle moment is {ankle_moment:.0f} Nm.")
print(f"The calculated ankle moment is {ankle_moment:.2f} Nm.")
print(f"The calculated ankle moment is {ankle_moment:.5f} Nm.")
```


## 💪 Exercise 4

Using this variable:

```{code-cell}
force = 150
```

write a line of code that creates the variable `some_string` so that:

```python
print(some_string)
```

gives:

```
Measured force: 150 N
```

::::{dropdown} Solution
```{code-cell} ipython3
some_string = f"Measured force: {force} N"
print(some_string)
```
::::


## 💪 Exercise 5

Using these two variables:

```{code-cell}
force = 150
moment = 34
```

write a line of code that creates the variable `some_string` so that:

```python
print(some_string)
```

gives:

```
Measured force: 150 N
Measured moment: 34 Nm
```

::::{dropdown} Solution
```{code-cell} ipython3
some_string = f"Measured force: {force} N\nMeasured moment: {moment} Nm"
print(some_string)
```
::::


## 💪 Exercise 6

Using these two variables:

```{code-cell}
force = 150
moment = 34
```

write a line of code that creates the variable `some_string` so that:

```python
print(some_string)
```

gives:

```
We calculated a total force of 150 newton, while the calculated moment was 34 newton-meter.
```

and limit the width of your code lines to 80 characters.

::::{dropdown} Solution
```{code-cell} ipython3
some_string = (
    f"We calculated a total force of {force} newton, "
    f"while the calculated moment was {moment} newton-meter."
)
print(some_string)
```
::::


## User input

We can create strings interactively from user input:

```
the_string = input()
```

This allows the user to type some text right in the console. We can also provide some indication to the user:

```
the_string = input("Please enter your name: ")
```

Note that the input function always creates a string. If you want the user to input a float, then you need to convert the string to a float:

```
height = float(input("What is the participant's height in meters? "))
```

Or if we need the user to enter an integer:

```
i_cycle = int(input("Which gait cycle do we keep? "))
```
