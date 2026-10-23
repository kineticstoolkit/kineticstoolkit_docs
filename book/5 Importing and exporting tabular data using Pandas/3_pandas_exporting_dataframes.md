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


# Exporting a DataFrame

Here are some of the most import methods to export a {{pd_dataframe}} to another type or to a file.

## DataFrame → List/Array

To export a DataFrame to an array:

```{code-cell} ipython3
import pandas as pd

df = pd.DataFrame(
    [
        [920.6690625, 0.459204164],
        [929.039714, 0.405744469],
        [983.9531716, 0.426812137],
        [927.0143403, 0.480908568],
        [905.6627709, 0.435169206],
    ],
    columns=["PeakForce", "StepLength"]
)

df.to_numpy()
```

And to a list:

```{code-cell} ipython3
df.to_numpy().tolist()
```

## DataFrame → CSV file

In addition of its impressive list of read functions such as {{pd_read_csv}}, {{pd_read_excel}}, and {{pd_read_clipboard}}, Pandas also has their "to" counterpart.

```python
df.to_csv("filename.csv")
```

## DataFrame → Excel file

```python
df.to_excel("filename.xlsx")
```

## DataFrame → Clipboard

```python
df.to_clipboard()
```

## DataFrame → Markdown

For publication in Markdown (you need to install the optional `tabulate` package):

```{code-cell} ipython3
print(df.to_markdown())
```

## DataFrame → LaTeX

For publication in LaTeX:

```{code-cell} ipython3
print(df.to_latex())
```
