---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Importing DataFrames

Pandas provides several ways to read data from different formats. Here, we show some of the most important.

## Importing from other types

If the data is already available in Python, but is in another data type, there is a good chance that it can be converted to a DataFrame simply by using the {{pd_dataframe}} constructor.

### Nested list → DataFrame

To import a list of lists, with optional column names:

```{code-cell} ipython3
import pandas as pd
import numpy as np

some_list = [
    [1, 5, 9],
    [2, 6, 10],
    [3, 7, 11],
    [4, 8, 12]
]

pd.DataFrame(some_list, columns=["x", "y", "z"])
```

### NumPy array → DataFrame

Very similarly to nested lists, here is how to import a bidimensional arrays, with optional column names:

```{code-cell} ipython3
some_array = np.array(
    [
        [1, 5, 9],
        [2, 6, 10],
        [3, 7, 11],
        [4, 8, 12]
    ]
)

pd.DataFrame(some_array, columns=["x", "y", "z"])
```


### List of dictionaries → DataFrame

From a list of dictionaries where each dictionary has similar keys (dictionary key become columns):

```{code-cell} ipython3
some_list = [
    {"x": 1, "y": 5, "z": 9},
    {"x": 2, "y": 6, "z": 10},
    {"x": 3, "y": 7, "z": 11},
    {"x": 4, "y": 8, "z": 12},
]

pd.DataFrame(some_list)
```

This import method is very practical because it allows constructing and expanding the dictionary list during data processing, and then converting easily to a DataFrame at the end. Here is an example data processing loop that showcases this concept:

```{code-cell} ipython3
:tags: [remove-input]
source = pd.read_csv("results.csv")
def calculate_peak_force(i):
    return source["PeakForce"][i]
def calculate_step_length(i):
    return source["StepLength"][i]
```

```{code-cell} ipython3
n_cycles = 5  # Total number of cycles to analyze
results = []   # Empty list of results

# Analyse the cycles and append the results to the results list
for i_cycle in range(n_cycles):
    results.append(
        {
            "PeakForce": calculate_peak_force(i_cycle),
            "StepLength": calculate_step_length(i_cycle)
        }
    )

# Convert to a DataFrame
pd.DataFrame(results)
```


## Importing from other software

Pandas as impressive list of functions that read files or even the clipboard, such as {{pd_read_csv}}, {{pd_read_excel}}, and {{pd_read_clipboard}}. Many others exist and can be found on {{pandas}}' website.

### CSV file → DataFrame

Suppose you have a CSV file with this contents:

```{code-cell} ipython3
:tags: [remove-input]
source = pd.read_csv("results.csv")
!cat "results.csv"
```

You can import it directly using {{pd_read_csv}}:

```{code-cell} ipython3
pd.read_csv("results.csv")
```

In this case, we may want the Cycle column to specify the DataFrame index instead:

```{code-cell} ipython3
pd.read_csv("results.csv", index_col="Cycle")
```

Note that some csv files separate columns with other delimiters than commas (`,`) such as semicolons (`;`) or tabs (`\t`). This can be specified using the `delimiter` argument of []() {{pd_read_csv}}. There are many, many other options to this functions, such as skipping headers, defining alternate column names, etc.

### Excel file → DataFrame

Similarly to CSV files, you can load an Excel file using {{pd_read_excel}}. 

Suppose you have the Excel file of [](#fig_results_excel).

```{figure} fig_results_excel
:label: fig_results_excel
:width: 300px
Some results in an Excel file
```

You can import it directly using {{pd_read_excel}}:

```{code-cell} ipython3
pd.read_excel("results.xlsx")
```

You may want the Cycle column to specify the DataFrame index instead:

```{code-cell} ipython3
pd.read_excel("results.xlsx", index_col="Cycle")
```


### Clipboard → DataFrame

Suppose you open the data of [](#fig_results_excel) in Excel or any other table editor.

Simply select the data and copy it in the clipboard using "Edit → Copy". You can then create a DataFrame directly from the clipboard using {{pd_read_clipboard}}:

```python
pd.read_clipboard()
```

```{code-cell} ipython3
:tags: [remove-input]
pd.read_excel("results.xlsx")
```

You may want the Cycle column to specify the DataFrame index instead:

```python
pd.read_clipboard(index_col="Cycle")
```

```{code-cell} ipython3
:tags: [remove-input]
pd.read_excel("results.xlsx", index_col="Cycle")
```
