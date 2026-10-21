# Introduction to Pandas

{{pandas}} is a huge and very popular package that is particularly useful for working with series and tabular data. As such, it provides the {{pd_series}} type and the {{pd_dataframe}} type, the latter representing 2d data organized in lines columns and lines. By nature, Pandas is very efficient to exchange data between Python and other software that process tables such as Excel, R, Jasp, etc.

```{figure} fig_pandas_logo.png
:label: fig_pandas_logo
:width: 300px
The Pandas logo
```

This book does not pretend to cover even a microscopic part of the vast possibilities offered by Pandas. It mainly focuses on using Pandas DataFrames as an intermediary container to import and export data between different softwares, Python, and the [Kinetics Toolkit package](../6%20Manipulating%20TimeSeries%20using%20Kinetics%20Toolkit/1_ktk_intro.md).


## Importing Pandas

Usually, Pandas is imported in the `pd` namespace:

```python
import pandas as pd
```
