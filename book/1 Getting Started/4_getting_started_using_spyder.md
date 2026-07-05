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


# Using Spyder

For those who are familiar with Matlab, Spyder's interface should immediately look familiar. Spyder's standard look is shown in {numref}`fig_spyder_interface`.

#todo change the screenshot for a more modern version

:::{figure} fig_spyder_interface.png
:label: fig_spyder_interface
The three main panes of the standard Spyder interface.
:::

## Writing code in the console

Section A of {numref}`fig_spyder_interface` is the console. It executes one command at a time. It also shows the result of calculations. Try entering this simple calculation in the console:

```{code-cell} ipython3
:tags: [remove-output]
1 + 2
```

The console will show the results just below your command:

```{code-cell} ipython3
:tags: [remove-input]
1 + 2
```

You can also write multiple-line commands using CTRL+Enter. Both are executed, but only the result from the last command is printed:

```{code-cell} ipython3
1 + 2
3 + 4
```

To print the result of every command, we explicitly use the `print` command:

```{code-cell} ipython3
print("Hello world")
print("This is my first program")
```

## Writing code in a script

Section B of {numref}`fig_spyder_interface` is the script editor. It is simply a text editor that allows you to save code as a `.py` text file, to execute it all together later. You can execute a script by clicking on the "Run File" button ({numref}`fig_spyder_toolbar`).

As an exercise, create a file that prints "Hello World", save it as `hello_world.py`, and run it using the "Run File" button. You should see the text "Hello World" appear in the console.

:::{figure} fig_spyder_toolbar.png
:label: fig_spyder_toolbar
:width: 300px
"Run file", "Run current cell", "Run current cell and advance".
:::

## Code cell

When a script grows in length, it can be useful to run only one section at a time. A script can be split into cells using this sequence of characters that acts as a separator:

```python
# %%
```

You can also name cells by adding a title next to the separator:

```python
# %% Load results from previous acquisition

[...]

# %% Report these results in a local coordinate system

[...]

```

You can execute a cell by placing the cursor in that cell, then by clicking on the "Run current cell" or "Run current cell and advance" button ({numref}`fig_spyder_toolbar`).

## 💪 Exercise

Create a file named `exercise.py` that contains two cells. A first cell prints "Hello world", and a second cell prints "This is my first program". Run the cell of your choice using the toolbar icons.


## Getting help

Section C of {numref}`fig_spyder_interface` contains various panes. The help pane is particularly helpful to navigate the documentation of a given module or package. For example, to better understand how to use the Python `max` function, write `max` in the help pane.

:::{figure} fig_spyder_help_pane
:label: fig_spyder_help_pane
:width: 500px
Getting help on a function using Spyder's help pane.
:::

Note that you can also get help from the console, using the `help` function:

```{code-cell} ipython3
help(max)
```
