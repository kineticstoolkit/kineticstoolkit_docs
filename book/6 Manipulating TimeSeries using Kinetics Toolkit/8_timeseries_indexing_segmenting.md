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

# Indexing and segmenting TimeSeries using time or events


## Indexing TimeSeries

This section shows how to use these methods for indexing TimeSeries:
- {{ktk_timeseries_get_index_at_time}}
- {{ktk_timeseries_get_index_before_time}}
- {{ktk_timeseries_get_index_after_time}}
- {{ktk_timeseries_get_index_at_event}}
- {{ktk_timeseries_get_index_before_event}}
- {{ktk_timeseries_get_index_after_event}}

For this section, we will continue to use [kinetic data from wheelchair propulsion](../../5%20Appendix/dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```


Despite the title of this section, we do not index or slice a TimeSeries. Instead, we address its time or data arrays, as for any NumPy array. For instance, to get the time and force data at the 100th sample of the TimeSeries, we would do:

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

The `get_index_before_...` and `get_index_after_...` methods have a parameter `inclusive` that selects if the selection is inclusive (`<=`, `>=`) or exclusive (`<`, `>`):

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


## 💪 Exercise

Using the following data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

Write a code that counts the number of pushes and recoveries, and that generates the following lists:

```
push_times  # list[float]: List of times corresponding to each push event
recovery_times  # list[float]: List of times corresponding to each recovery event
```


```{code-cell} ipython3
:tags: [hide-cell]

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


## Segmenting TimeSeries

This section shows how to use these methods to segment TimeSeries:

- {{ktk_timeseries_get_ts_before_index}}
- {{ktk_timeseries_get_ts_after_index}}
- {{ktk_timeseries_get_ts_between_indexes}}
- {{ktk_timeseries_get_ts_before_time}}
- {{ktk_timeseries_get_ts_after_time}}
- {{ktk_timeseries_get_ts_between_times}}
- {{ktk_timeseries_get_ts_before_event}}
- {{ktk_timeseries_get_ts_after_event}}
- {{ktk_timeseries_get_ts_between_events}}

All these methods do the same: they extract a new TimeSeries using a criterion based on index, time, or event. We will once again use [kinetic data of wheelchair propulsion](../../5%20Appendix/dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import matplotlib.pyplot as plt

import kineticstoolkit.lab as ktk

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

### Using indexes

If we know that the sync event happened at index 1049 (we could know it using `index = ts.get_index_at_event("sync")`), we can discard any data that happened before this index:

```{code-cell} ipython3
new_ts = ts.get_ts_after_index(1049)
new_ts.plot()
```

### Using time

If we know that the sync event happened at time 4.37 (we could know it using `time = ts.time[ts.get_index_at_event("sync")]`), we could do the same using time:

```{code-cell} ipython3
new_ts = ts.get_ts_after_time(4.37)
```

### Using events

Or, we could simply use the event itself:

```{code-cell} ipython3
new_ts = ts.get_ts_after_event("sync")
```

These methods are very helpful to analyze only specific sections of a TimeSeries. For instance, to analyze only the first four pushes and get rid of any other data, we would do:

```{code-cell} ipython3
# Extract the four pushes
first_four_pushes = ts.get_ts_between_events("push", "push", 0, 4, inclusive=True)

# Remove the events outside the resulting TimeSeries
first_four_pushes = first_four_pushes.trim_events()

# Plot the result
first_four_pushes.plot()
```

Note the use of `inclusive=True` in this example. This optional parameter indicates whether the "before", "after", or "between" term in the method name is inclusive (<=, >=) or strict (<, >). Different combinations lead to different results:

```{code-cell} ipython3
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
ts3 = ts.get_ts_between_events("push", "push", 0, 4, inclusive=[False, True])
ts3 = ts3.trim_events()
ts3.plot(legend=False)
plt.xlabel("Inclusive = [False, True]")

plt.subplot(2, 2, 4)
ts4 = ts.get_ts_between_events("push", "push", 0, 4, inclusive=[True, False])
ts4 = ts4.trim_events()
ts4.plot(legend=False)
plt.xlabel("Inclusive = [True, False]")

plt.tight_layout()
```

## 💪 Exercise

Using this dataset of [kinetic data during wheelchair propulsion](../../5%20Appendix/dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion_events.ktk.zip"))
ts.plot()
```

Write a code that generates a list of three floats named `peak_Mz`, that includes the peak moment (`Moments[:, 2]`) during each of the three first pushes.

```{code-cell} ipython3
:tags: [hide-cell]
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
