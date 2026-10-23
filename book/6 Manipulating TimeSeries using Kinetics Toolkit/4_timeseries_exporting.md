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

# Exporting TimeSeries

Like for importing TimeSeries, there are several methods to export TimeSeries to other variables or files. The most important methods are shown in [](#fig_exporting_timeseries).

::::{figure}
:label: fig_exporting_timeseries
```mermaid
flowchart LR
    step_1@{ shape: text, label: "KTK TimeSeries" }
    step_2[".data[]<br>.time[]"]
    step_3@{ shape: text, label: "NumPy Array" }
    step_4[".to_dataframe()"]
    step_5@{ shape: text, label: "Pandas DataFrame" }
    step_6["ktk.write_c3d()"]
    step_7[("c3d file")]
    step_8["ktk.save()"]
    step_9[("json file<br>json.zip file<br>ktk.zip file")]
    step_10[".to_csv()"]
    step_11[".to_excel()"]
    step_12[".to_clipboard()"]
    step_13[("csv file")]
    step_14[("Excel file")]
    step_15@{ shape: text, label: "clipboard" }
    step_16[".to_markdown()"]
    step_17[".to_latex()"]
    step_18@{ shape: text, label: "..." }
    step_19@{ shape: doc, label: "Markdown table" }
    step_20@{ shape: doc, label: "LaTeX table" }

    step_1 --> step_4
    step_1 --> step_2
    step_2 --> step_3
    step_4 --> step_5
    step_1 --> step_6
    step_6 --> step_7
    step_1 --> step_8
    step_8 --> step_9
    step_5 --> step_10
    step_5 --> step_11
    step_5 --> step_12
    step_10 --> step_13
    step_11 --> step_14
    step_12 --> step_15
    step_5 --> step_16
    step_5 --> step_17
    step_5 --> step_18
    step_16 --> step_19
    step_17 --> step_20
```

Exporting TimeSeries
::::