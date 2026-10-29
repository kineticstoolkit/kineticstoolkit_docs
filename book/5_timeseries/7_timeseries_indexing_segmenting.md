---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Indexing and segmenting TimeSeries

This section shows how to use these methods for indexing TimeSeries:


|                                          |                                           |
| ---------------------------------------- | ----------------------------------------- |
| {{ktk_timeseries_get_index_at_time}}     | {{ktk_timeseries_get_index_at_event}}     |
| {{ktk_timeseries_get_index_before_time}} | {{ktk_timeseries_get_index_before_event}} |
| {{ktk_timeseries_get_index_after_time}}  | {{ktk_timeseries_get_index_after_event}}  |


and these methods for segmenting TimeSeries:


|                                           |                                         |                                          |
| ----------------------------------------- | --------------------------------------- | ---------------------------------------- |
| {{ktk_timeseries_get_ts_before_index}}    | {{ktk_timeseries_get_ts_before_time}}   | {{ktk_timeseries_get_ts_before_event}}   |
| {{ktk_timeseries_get_ts_after_index}}     | {{ktk_timeseries_get_ts_after_time}}    | {{ktk_timeseries_get_ts_after_event}}    |
| {{ktk_timeseries_get_ts_between_indexes}} | {{ktk_timeseries_get_ts_between_times}} | {{ktk_timeseries_get_ts_between_events}} |


We will use kinetic data from wheelchair propulsion:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```


## Indexing TimeSeries

Despite this title, we do not directly index or slice a TimeSeries. Instead, we address its time or data arrays, as we do for any NumPy array. For instance, to get the time and force data at the 100th sample of the TimeSeries, we would do:

```{code-cell}
print("Time is", ts.time[99])
print("Force is", ts.data["Forces"][99])
```

We may however want to know which index corresponds to a given time. To this effect, we can use {{ktk_timeseries_get_index_at_time}}, {{ktk_timeseries_get_index_before_time}} and {{ktk_timeseries_get_index_after_time}}:

```{code-cell}
print("The index that is nearest to 15 seconds is:")
print(ts.get_index_at_time(15.0))

print("The index that is just before 15 seconds is:")
print(ts.get_index_before_time(15.0))

print("The index that is just after 15 seconds is:")
print(ts.get_index_after_time(15.0))
```

Or, we may want to know which index corresponds to a given event, using {{ktk_timeseries_get_index_at_event}}, {{ktk_timeseries_get_index_before_event}} and {{ktk_timeseries_get_index_after_event}}:

```{code-cell}
print("The index that is nearest to 2nd push is:")
print(ts.get_index_at_event("push", occurrence=1))

print("The index that is just before 2nd push is:")
print(ts.get_index_before_event("push", occurrence=1))

print("The index that is just after 2nd push is:")
print(ts.get_index_after_event("push", occurrence=1))
```

The `get_index_before_...` and `get_index_after_...` methods have a parameter `inclusive` that selects if the selection is inclusive (`<=`, `>=`) or exclusive (`<`, `>`). [](#tbl_get_index) shows the different use cases.

:::{table} Getting TimeSeries index
:label: tbl_get_index

| Method                                                    | Returns                                |
| --------------------------------------------------------- | -------------------------------------- |
| get_index_before_time(t, inclusive=False)                 | index for nearest time $<$ t           |
| get_index_before_time(t, inclusive=True)                  | index for nearest time $<=$ t          |
| get_index_after_time(t, inclusive=False)                  | index for nearest time $>$ t           |
| get_index_after_time(t, inclusive=True)                   | index for nearest time $>=$ t          |
| get_index_before_event(name, occurrence, inclusive=False) | index for nearest time $<$ event time  |
| get_index_before_event(name, occurrence, inclusive=True)  | index for nearest time $<=$ event time |
| get_index_after_event(name, occurrence, inclusive=False)  | index for nearest time $>$ event time  |
| get_index_after_event(name, occurrence, inclusive=True)   | index for nearest time $>=$ event time |

:::

## 💪 Exercise 1

Using the following data:

```{code-cell} ipython3
ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

Write code that counts the number of pushes and recoveries, and that generates the following lists:

```
push_times  # list[float]: List of times corresponding to each push event
recovery_times  # list[float]: List of times corresponding to each recovery event
```

:::{dropdown} Tip
First create empty lists for `push_times` and `recovery_times`, and then, in a loop, add the time that corresponds to each occurrence of a push and a recovery.
:::


:::{dropdown} Solution
```{code-cell} ipython3
# Create empty lists
push_times = []
recovery_times = []

# Count the number of pushes/recoveries
n_pushes = ts.count_events("push")
n_recoveries = ts.count_events("recovery")

# Find the push times
for i_push in range(n_pushes):
    index = ts.get_index_at_event("push", occurrence=i_push) 
    push_times.append(ts.time[index])

# Find the recovery times
for i_recovery in range(n_recoveries):
    index = ts.get_index_at_event("recovery", occurrence=i_recovery)
    recovery_times.append(ts.time[index])

# Print it!
print("Push times:", push_times)
print("Recovery times:", recovery_times)
```
:::


## Segmenting TimeSeries

Instead of accessing `time` and `data` using indexes, we can also segment TimeSeries, which means extracting a new, smaller TimeSeries from an original TimeSeries. Segmenting TimeSeries is done using one of its many `get_ts_...` methods.

In the TimeSeries above, there is a synchronization event called "sync", which happened at a given time and index:

```{code-cell} ipython3
ts.get_index_at_event("sync")
```

```{code-cell} ipython3
ts.time[1049]
```

Here is how we can get a new TimeSeries without data prior the sync event.

### Using indexes

According to [](#tbl_get_ts_using_index), we would do:

```{code-cell} ipython3
new_ts = ts.get_ts_after_index(1049)
new_ts.plot()
```

:::{table} Segmenting TimeSeries using index
:label: tbl_get_ts_using_index

| Method                                                  | Returns                      |
| ------------------------------------------------------- | ---------------------------- |
| get_ts_before_index(i, inclusive=False)                 | ts for index $<$ i           |
| get_ts_before_index(i, inclusive=True)                  | ts for index $<=$ i          |
| get_ts_after_index(i, inclusive=False)                  | ts for index $>$ i           |
| get_ts_after_index(i, inclusive=True)                   | ts for index $>=$ i          |
| get_ts_between_indexes(i1, i2, inclusive=False)         | ts for i1 $<$ index $<$ i2   |
| get_ts_between_indexes(i1, i2, inclusive=True)          | ts for i1 $<=$ index $<=$ i2 |
| get_ts_between_indexes(i1, i2, inclusive=[True, False]) | ts for i1 $<=$ index $<$ i2  |
| get_ts_between_indexes(i1, i2, inclusive=[False, True]) | ts for i1 $<$ index $<=$ i2  |
:::

### Using time

According to [](#tbl_get_ts_using_time), we would do:

```{code-cell} ipython3
new_ts = ts.get_ts_after_time(4.37)
new_ts.plot()
```

:::{table} Segmenting TimeSeries using time
:label: tbl_get_ts_using_time

| Method                                                | Returns                  |
| ----------------------------------------------------- | ------------------------ |
| get_ts_before_time(t, inclusive=False)                | ts for time $<$ t        |
| get_ts_before_time(t, inclusive=True)                 | ts for time $<=$ t       |
| get_ts_after_time(t, inclusive=False)                 | ts for time $>$ t        |
| get_ts_after_time(t, inclusive=True)                  | ts for time $>=$ t       |
| get_ts_between_times(t1, t2, inclusive=False)         | ts for t1 $<$ time $<$ t2   |
| get_ts_between_times(t1, t2, inclusive=True)          | ts for t1 $<=$ time $<=$ t2 |
| get_ts_between_times(t1, t2, inclusive=[True, False]) | ts for t1 $<=$ time $<$ t2  |
| get_ts_between_times(t1, t2, inclusive=[False, True]) | ts for t1 $<$ time $<=$ t2  |
:::


### Using events

According to [](#tbl_get_ts_using_events), we would do:

```{code-cell} ipython3
new_ts = ts.get_ts_after_event("sync")
new_ts.plot()
```


:::{table} Segmenting TimeSeries using events
:label: tbl_get_ts_using_events

| Method                                                                                 | Returns                                   |
| -------------------------------------------------------------------------------------- | ----------------------------------------- |
| get_ts_before_event(name, occurrence, inclusive=False)                                 | ts before event, excluding the event      |
| get_ts_before_event(name, occurrence, inclusive=True)                                  | ts before event, including the event      |
| get_ts_after_event(name, occurrence, inclusive=False)                                  | ts after event, excluding the event       |
| get_ts_after_event(name, occurrence, inclusive=True)                                   | ts after event, including the event       |
| get_ts_between_events(name1, name2, occurrence1, occurrence2, inclusive=False)         | ts between events, excluding the events   |
| get_ts_between_events(name1, name2, occurrence1, occurrence2, inclusive=True)          | ts between events, including the events   |
| get_ts_between_events(name1, name2, occurrence1, occurrence2, inclusive=[True, False]) | ts between events, including only event 1 |
| get_ts_between_events(name1, name2, occurrence1, occurrence2, inclusive=[False, True]) | ts between events, including only event 2 |
:::



These methods are very helpful to analyze only specific sections of a TimeSeries. For instance, to analyze only the first four pushes and get rid of any other data:

```{code-cell} ipython3
# Extract the four pushes
first_four_pushes = ts.get_ts_between_events("push", "push", 0, 4, inclusive=True)

# Remove the events outside the resulting TimeSeries
first_four_pushes = first_four_pushes.trim_events()

# Plot the result
first_four_pushes.plot()
```

Note that different combinations of `inclusive` lead to different results:

```{code-cell} ipython3
:tags: [remove-input]
plt.subplot(2, 2, 1)
ts1 = ts.get_ts_between_events("push", "push", 0, 4, inclusive=False)
ts1 = ts1.trim_events()
ts1.plot(legend=False)
plt.xlabel("Inclusive = False")

plt.subplot(2, 2, 2)
ts2 = ts.get_ts_between_events("push", "push", 0, 4, inclusive=True)
ts2 = ts2.trim_events()
ts2.plot(legend=False)
plt.xlabel("Inclusive = True")

plt.subplot(2, 2, 3)
ts4 = ts.get_ts_between_events("push", "push", 0, 4, inclusive=[True, False])
ts4 = ts4.trim_events()
ts4.plot(legend=False)
plt.xlabel("Inclusive = [True, False]")

plt.subplot(2, 2, 4)
ts3 = ts.get_ts_between_events("push", "push", 0, 4, inclusive=[False, True])
ts3 = ts3.trim_events()
ts3.plot(legend=False)
plt.xlabel("Inclusive = [False, True]")

plt.tight_layout()
```

## 💪 Exercise 2

Using this dataset:

```{code-cell} ipython3
ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

Write a code that generates a list of three floats named `peak_Mz`, that includes the peak moment (`Moments[:, 2]`) during each of the three first pushes.

:::{dropdown} Solution
```{code-cell} ipython3
import numpy as np

# Init the list
peak_Mz = []

# Fill the list
for i_push in range(3):
    # Extract a new TimeSeries that only spans this push
    sub_ts = ts.get_ts_between_events("push", "recovery", i_push, i_push)

    # Calculate the peak moment on this new TimeSeries and happen it to
    # the list
    peak_Mz.append(np.max(sub_ts.data["Moments"][:, 2]))

# Print it!
print(peak_Mz)
```
:::
