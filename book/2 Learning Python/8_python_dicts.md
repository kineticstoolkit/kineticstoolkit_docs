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

The last container type that any Python programmer should know is the dictionary (`dict`). A dictionary is a container, like a list or a tuple. However, whereas lists and tuples store elements in a sequential way that we address using indices or slices, dictionaries store elements non-sequentially using keys. This section introduces how to create, read, and modify dictionaries.


## Creating dictionaries

A dictionary is created using curly braces `{}` and colons `:`, using a "key: value" syntax:

```{code-cell} ipython3
empty_dict = {}
dict_of_integers = {1: 11, 2: 22, 5: 55}
```

Here, we used integers for both the keys and values, but in reality:
- the key can be of many types such as integers, strings, tuples, etc.
- the value can be of any type.

```{code-cell} ipython3
dict_of_anything = {
    1: "String for integer key 1",            # key = int, value = str
    2.0: "String for integer key 2",          # key = float, value = str
    "three": "String for string key 'three'", # key = str, value = str
    "some_int_value": 10,                     # key = str, value = int
    "some_float_value": 10.0,                 # key = str, value = float
    "some_list": [1, 3, 5, 7],                # key = str, value = list
    "some_nested_dict": {                     # key = str, value = dict
        "a": "A",
        "b": "B",
    },
}
```


:::{tip}
As for lists, you can add optional type annotations to clarify the contents of a dictionary. For instance, all these instructions produce an empty dictionary, but those with type annotation indicate the structure of the dictionary as it grows.

```{code-cell} ipython3
# We don't know what this dict will contain
some_dict = {}

# This dict will contain string keys and integer values
some_dict : dict[str, int] = {}

# This nested dict will contain string outer keys, int inner keys, and float values.
some_dict : dict[str, dict[int, float]] = {}
```

:::


## Reading an element of a dictionary

To read a dictionary item, use brackets `[]`, as you would index a [list](7_python_lists.md):

```{code-cell} ipython3
some_dict = {
    "one": 1.0,
    "two": 2.0,
}

some_dict["one"]
```

Use the `in` keyword to test if the dictionary contains a certain key:

```{code-cell} ipython3
print("one" in some_dict)
print("three" in some_dict)
```


## 💪 Exercise 1

You affix an inclinometer on a person's arm and you ask them to reach different positions in the sagittal plane as shown in [](fig_shoulder_flexion_inclinometer). Each position is reached twice.

```{figure} fig_shoulder_flexion_inclinometer
:label: fig_shoulder_flexion_inclinometer
:width: 700px

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

Write code that creates a new dictionary named `flexion` from variable `incline`, which is the shoulder flexion angle for each repetition of TargetA, TargetB and TargetC. This new dictionary (`flexion`) will have the following form:

```python
{
    "TargetA_Repetition1": flexion angle,
    "TargetB_Repetition1": flexion angle,
    "TargetC_Repetition1": flexion angle,
    "TargetA_Repetition2": flexion angle,
    "TargetB_Repetition2": flexion angle,
    "TargetC_Repetition2": flexion angle,
}
```

The flexion angle is calculated as the incline in the target position, minus the incline at the reference position.

::::{dropdown} Solution
```{code-cell} ipython3
# Create the dictionary
flexion = {
    "TargetA_Repetition1": incline["TargetA_Repetition1"] - incline["Reference"],
    "TargetB_Repetition1": incline["TargetB_Repetition1"] - incline["Reference"],
    "TargetC_Repetition1": incline["TargetC_Repetition1"] - incline["Reference"],
    "TargetA_Repetition2": incline["TargetA_Repetition2"] - incline["Reference"],
    "TargetB_Repetition2": incline["TargetB_Repetition2"] - incline["Reference"],
    "TargetC_Repetition2": incline["TargetC_Repetition2"] - incline["Reference"],
}

# Show the result
flexion
```
::::


## Writing an element of a dictionary

To change the value of an existing element, use brackets as you would change one element of a [list](7_python_lists.md):

```{code-cell} ipython3
some_dict["two"] = 2222

some_dict
```


## Adding and removing elements

Accessing a dictionary using a key that is not part of the dictionary results in a KeyError:

```{code-cell} ipython3
:tags: [raises-exception]
some_dict["three"]
```

However, assigning a value to an inexistant key **adds** this key. This is how we add new items to a dictionary:

```{code-cell} ipython3
some_dict["three"] = 3.0

some_dict
```

To remove an item from a dictionary, use the `pop` method, which as for [lists](7_python_lists.md) returns the value being deleted, and removes this item from the dictionary.

```{code-cell} ipython3
print(f"before: {some_dict}")

removed_item = some_dict.pop("three")

print(f"removed: {removed_item}")
print(f"after: {some_dict}")
```



## 💪 Exercise 2

Here is a dictionary that represents different characteristics of a research project participant:

```{code-cell} ipython3
characteristics = {
    "ID": 101,
    "Sex": "F",
    "Height": 1.45,
    "Weight": 56.0,
}
```

Write code that adds the participant's age (27 years old) to this dictionary.

::::{dropdown} Solution
```{code-cell} ipython3
characteristics["Age"] = 27

characteristics
```
::::


## 💪 Exercise 3

Add the participant's BMI to the previous exercise's dictionary.

$$
\text{BMI} = \text{Weight}/\text{Height}^2
$$

::::{dropdown} Solution
```{code-cell} ipython3
characteristics["BMI"] = (
    characteristics["Weight"]
    / (characteristics["Height"] ** 2)
)

characteristics
```
::::

