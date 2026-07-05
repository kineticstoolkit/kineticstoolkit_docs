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



# Adding, renaming, removing events

This section shows how to use these methods for event management:
- {{ktk_timeseries_add_event}}
- {{ktk_timeseries_count_events}}
- {{ktk_timeseries_rename_event}}
- {{ktk_timeseries_remove_event}}
- {{ktk_timeseries_remove_duplicate_events}}
- {{ktk_timeseries_trim_events}}
- {{ktk_timeseries_ui_edit_events}}

We will use this TimeSeries that contains [cyclic kinetic data in wheelchair propulsion](../../5%20Appendix/dataset_kinetics_wheelchair_propulsion.md):

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("kinetics_wheelchair_propulsion.ktk.zip"))
ts.plot()
```

## Adding events

We already know how to manually add events using {{ktk_timeseries_add_event}}:

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

## Counting the number of occurrences of an event

Each event is defined by its name, and if it is repeated multiple times, by an occurrence. To count these occurrences, we use {{ktk_timeseries_count_events}}:

```{code-cell} ipython3
print(ts.count_events('sync'), "occurrences of event 'sync'")
print(ts.count_events('push'), "occurrences of event 'push'")
print(ts.count_events('recovery'), "occurrences of event 'recovery'")
```

## Renaming events

Renaming events is performed using {{ktk_timeseries_rename_event}}:

```{code-cell} ipython3
ts = ts.rename_event("push", "lastpush", occurrence=4)
ts = ts.rename_event("recovery", "lastrecovery", occurrence=4)

ts.plot()
```

## Removing events

To remove an occurrence of an event, we use {{ktk_timeseries_remove_event}}. For instance, to remove the second push cycle:

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

Note the superposition of occurrences on the first events. To remove the duplicate events, we use {{ktk_timeseries_remove_duplicate_events}}:

```{code-cell} ipython3
ts = ts.remove_duplicate_events()
ts.plot()
```

## Trimming events

For some reasons, it may happen that a TimeSeries have events outside its time array. Let's simulate this situation:

```{code-cell} ipython3
ts = ts.add_event(-3.0, "before")
ts = ts.add_event(-1.0, "before")
ts = ts.add_event(23.0, "after")
ts = ts.add_event(25.0, "after")

ts.plot()
```

To remove any event that is outside the TimeSeries' time array, we use {{ktk_timeseries_trim_events}}:

```{code-cell} ipython3
ts = ts.trim_events()
ts.plot()
```

## Editing events interactively

Finally, it is possible to edit the events interactively, using {{ktk_timeseries_ui_edit_events}}. This allows to add, remove and move events by clicking on a figure.

:::{note}
Matplotlib must be interactive. See section [](../../1%20Getting%20Started/3_getting_started_configuring_spyder.md) do help.
:::

```
ts = ts.ui_edit_events()
```

which creates the interactive windows shown in {numref}`fig_timeseries.ui_edit_events_1` and {numref}`fig_timeseries.ui_edit_events_2`.


:::{figure}
:label: fig_timeseries.ui_edit_events_1
:width: 7in
![timeseries.ui_edit_events](_static/images/fig_timeseries.ui_edit_events_1.png)

Interactive figure created by {{ktk_timeseries_ui_edit_events}}
:::

:::{figure}
:label: fig_timeseries.ui_edit_events_2
:width: 4in
![timeseries.ui_edit_events](_static/images/fig_timeseries.ui_edit_events_2.png)

Interactive menu created by {{ktk_timeseries_ui_edit_events}}
:::
