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


# Manipulating events

This section shows how to use these methods for event manipulation:


|                                   |                                            |
| --------------------------------- | ------------------------------------------ |
| {{ktk_timeseries_add_event}}      | {{ktk_timeseries_remove_event}}            |
| {{ktk_timeseries_count_events}}   | {{ktk_timeseries_remove_duplicate_events}} |
| {{ktk_timeseries_rename_event}}   | {{ktk_timeseries_trim_events}}             |
| {{ktk_timeseries_ui_edit_events}} |                                            |


We will use this TimeSeries that contains cyclic kinetic data in wheelchair propulsion:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion.ktk.zip"))
ts.plot()
```

## Adding events

To add events, simply use {{ktk_timeseries_add_event}}:

```{code-cell} ipython3
ts = ts.add_event(4.37, "sync")
ts = ts.add_event(8.56, "push")
ts = ts.add_event(9.93, "recovery")
ts = ts.add_event(10.50, "push")
ts = ts.add_event(11.12, "recovery")
ts = ts.add_event(11.78, "push")
ts = ts.add_event(12.33, "recovery")
ts = ts.add_event(13.39, "push")
ts = ts.add_event(13.88, "recovery")
ts = ts.add_event(14.86, "push")
ts = ts.add_event(15.30, "recovery")

ts.plot()
```

You can also add events interactively using {{ktk_timeseries_ui_edit_events}} (see []() [below](#ui_edit_events)).


## Counting the number of occurrences of an event

Each event is defined by its name, and if it is repeated multiple times, by an occurrence. To count these occurrences, use {{ktk_timeseries_count_events}}:

```{code-cell} ipython3
print(ts.count_events('sync'), "occurrences of event 'sync'")
print(ts.count_events('push'), "occurrences of event 'push'")
print(ts.count_events('recovery'), "occurrences of event 'recovery'")
```

## Renaming events

To rename events, use {{ktk_timeseries_rename_event}}:

```{code-cell} ipython3
ts = ts.rename_event("push", "lastpush", occurrence=4)
ts = ts.rename_event("recovery", "lastrecovery", occurrence=4)

ts.plot()
```

## Removing events

To remove an occurrence of an event, use {{ktk_timeseries_remove_event}}. For instance, to remove the second push cycle:

```{code-cell} ipython3
ts = ts.remove_event("push", occurrence=1)
ts = ts.remove_event("recovery", occurrence=1)

ts.plot()
```

## Removing duplicate events

It may happen that events get duplicated in a TimeSeries. For instance, we may have added some events twice:

```{code-cell} ipython3
ts = ts.add_event(4.37, "sync")
ts = ts.add_event(8.56, "push")
ts = ts.add_event(9.93, "recovery")
ts = ts.add_event(10.50, "push")
ts = ts.add_event(11.12, "recovery")
ts = ts.add_event(11.78, "push")
ts = ts.add_event(12.33, "recovery")

ts.plot()
```

Note the superposition of occurrences on the first events. To remove the duplicate events, use {{ktk_timeseries_remove_duplicate_events}}:

```{code-cell} ipython3
ts = ts.remove_duplicate_events()
ts.plot()
```

## Trimming events

For some reasons (e.g., we extracted data from a larger TimeSeries), a TimeSeries could have events before or after its data. Let's simulate this situation:

```{code-cell} ipython3
ts = ts.add_event(-3.0, "before")
ts = ts.add_event(-1.0, "before")
ts = ts.add_event(23.0, "after")
ts = ts.add_event(25.0, "after")

ts.plot()
```

To remove these events, use {{ktk_timeseries_trim_events}}:

```{code-cell} ipython3
ts = ts.trim_events()
ts.plot()
```


(ui_edit_events)=
## Editing events interactively

Finally, events can be edited interactively using {{ktk_timeseries_ui_edit_events}}.

:::{note}
Matplotlib must be interactive. See section [](../0_introduction/3_getting_started_installing_spyder.md) do help.
:::


```
ts = ts.ui_edit_events()
```

This creates the interactive windows shown in [](#fig_timeseries.ui_edit_events_1) and [](#fig_timeseries.ui_edit_events_2).


```{figure} fig_timeseries.ui_edit_events_1.png
:label: fig_timeseries.ui_edit_events_1
:width: 700px
Interactive figure created by {{ktk_timeseries_ui_edit_events}}
```

```{figure} fig_timeseries.ui_edit_events_2.png
:label: fig_timeseries.ui_edit_events_2
:width: 300px
Interactive menu created by {{ktk_timeseries_ui_edit_events}}
```
