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


# Importing data as a DataFrame

Pandas provides several ways to read data from different formats. Here, we show some of the most important.

## List/Array → DataFrame

To import any bidimensional array or equivalent list, with optional column names:

```{code-cell} ipython3
import pandas as pd
import numpy as np

some_list = [
    [920.6690625, 0.459204164],
    [929.039714, 0.405744469],
    [983.9531716, 0.426812137],
    [927.0143403, 0.480908568],
    [905.6627709, 0.435169206]
]

pd.DataFrame(some_list, columns=["PeakForce", "StepLength"])
```

## Dictionary of lists/arrays → DataFrame

From a dictionary of lists/arrays where each dictionary key becomes a column:

```{code-cell} ipython3
some_dict = {
    "PeakForce": [920.6690625, 929.039714 , 983.9531716, 927.0143403, 905.6627709],
    "StepLength": [0.45920416, 0.40574447, 0.42681214, 0.48090857, 0.43516921],
}

pd.DataFrame(some_dict)
```

## List of dictionaries → DataFrame

From a list of dictionaries where each dictionary key becomes a column:

```{code-cell} ipython3
some_list = [
    {"PeakForce": 920.6690625, "StepLength": 0.459204164},
    {"PeakForce": 929.0397140, "StepLength": 0.405744469},
    {"PeakForce": 983.9531716, "StepLength": 0.426812137},
    {"PeakForce": 927.0143403, "StepLength": 0.480908568},
    {"PeakForce": 905.6627709, "StepLength": 0.435169206},
]

pd.DataFrame(some_list)
```

This import method has a very practical use case, which is constructing and expanding the list during data processing. Here is an example of code that could have constructed this list:

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


## CSV file → DataFrame

Pandas also has an impressive list of functions that read files or even the clipboard, such as {{pd_read_csv}}, {{pd_read_excel}}, and {{pd_read_clipboard}}. Many others exist and can be found on {{pandas}}' website.

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

Note that some csv files separate columns with other delimiters than commas (`,`) such as semicolons (`;`) or tabs (`\t`). This can be specified using the `delimiter` argument of []() {{pd_read_csv}}. There are many, many other options to this functions, such as skipping headers, defining alternate column names, etc.

## Excel file → DataFrame

Similarly to CSV files, you can load an Excel file using {{pd_read_excel}}. 

Suppose you have the Excel file of [](#fig_results_excel).

```{figure} fig_results_excel
:label: fig_results_excel
:width: 300px
Some results in an Excel file
```

You can import it directly using {{pd_read_excel}} (you need to install the optional `openpyxl` package):

```{code-cell} ipython3
pd.read_excel("results.xlsx")
```


## Clipboard → DataFrame

Suppose you open the data of [](#fig_results_excel) in Excel or any other table editor.

Simply select the data and copy it in the clipboard using "Edit → Copy". You can then create a DataFrame directly from the clipboard using {{pd_read_clipboard}}:

```python
pd.read_clipboard()
```

```{code-cell} ipython3
:tags: [remove-input]
pd.read_excel("results.xlsx")
```
