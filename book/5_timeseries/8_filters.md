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


# Filtering and derivating TimeSeries

Most recorded data needs to be filtered at some point. This section introduces the most common frequency-domain and time-domain filters in biomechanical analysis, and show how to apply them directly on TimeSeries using the {{ktk_filters}} module and its functions:


|                        |                        |
| ---------------------- | ---------------------- |
| {{ktk_filters_butter}} | {{ktk_filters_smooth}} |
| {{ktk_filters_deriv}}  | {{ktk_filters_savgol}} |
| {{ktk_filters_median}} |                        |

We will use this example noisy data:
```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts_noisy = ktk.load(ktk.doc.download("filters_noisy_signals.ktk.zip"))

ts_noisy.plot();
```


## Removing frequencies using a Butterworth filter

The Butterworth filter may be the most used filter in biomechanics. It removes ranges of frequencies from the signal's frequency spectrum. Normally, we first identify the frequency range of our data, so that we can remove any signal frequencies outside this range. In KTK, we remove these frequencies using {{ktk_filters_butter}}.


### Low-pass filter

The default setting for {{ktk_filters_butter}} is to apply a low-pass, no-lag filter of order 2. For a cut-off frequency of 20 Hz:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, fc=20)
ts_filtered.plot()
```

You are encouraged to experiment with different cut-off frequencies to observe its effect on the results. In the figure above, 20 Hz was probably correct for the sine wave, but it filtered out the most dynamic components, most notably in the square and pulse signals.

### High-pass filter

The inverse operation is the high-pass filter. To observe what we removed from the original signal in the figure above:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, btype="highpass", fc=20)
ts_filtered.plot()
```

Only the transitions were kept; all the stable parts of the signal were removed.

### Band-pass filter

A band-pass filter is the combination of a low-pass filter and high-pass filter. It is commonly used in electromyography processing, to filter both high-frequency noise and low-frequency movement artifact.

To remove frequencies out of the 10 and 80 Hz band:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, btype="bandpass", fc=[10, 80])
ts_filtered.plot()
```


## 💪 Exercise

Using this signal from a surface EMG electrode on the biceps brachii:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

filename = ktk.doc.download("emg_biceps_brachii.ktk.zip")
emg = ktk.load(filename)
emg.plot()
```

Write code that generates new data named "Envelope" in the TimeSeries, which corresponds to the envelope of this signal. Follow these three steps:
1. Filter the TimeSeries with a band-pass Butterworth filter from 20 Hz to 500 Hz to reject high-frequency noise and body movement artifacts.

:::{dropdown} Solution
```{code-cell} ipython3
filtered_emg = ktk.filters.butter(emg, btype="bandpass", fc=[20, 500])
filtered_emg.plot()
```

2. Rectify the filtered TimeSeries by replacing every data point with its absolute value. You may use {{np_abs}}.

:::{dropdown} Solution
```{code-cell} ipython3
filtered_emg.data["BicepsBrachiiR"] = np.abs(filtered_emg.data["BicepsBrachiiR"])
filtered_emg.plot()
```
:::

3. Filter the rectified TimeSeries with a low-pass Butterworth filter with a cut-off frequency of 10 Hz.

:::{dropdown} Solution
```{code-cell} ipython3
filtered_emg = ktk.filters.butter(filtered_emg, fc=10)

# Here we add the envelope to the original signal, so that we can plot
# both curves at the same time.
filtered_emg = filtered_emg.rename_data("BicepsBrachiiR", "Envelope")
emg = emg.merge(filtered_emg)

# Plot the result
emg.plot()
```
:::



## Smoothing using a moving average

The moving average is an excellent filter to remove noise with a specific time pattern. A classic example is the day-to-day evaluation of a process that is sensitive to weekends (for example, the number of workers who enter a building). A moving average with a window length of 7 days is ideal to evaluate the general trend of this signal without considering intra-week fluctuations. Let's first load some noisy data:

```{code-cell} ipython3
ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

ts.plot(["clean", "periodic_noise"], '.-')
```

This signal contains periodic noise with a period of five seconds. To smooth it with a 5-second moving average using {{ktk_filters_smooth}}:

```{code-cell} ipython3
filtered = ktk.filters.smooth(ts, window_length=5)
```

This gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered = filtered.get_subset("periodic_noise")
filtered.rename_data("periodic_noise", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "periodic_noise", "filtered"], '.-')
```

As expected, the 5-sample period noise was completely removed. However, the signal was also slightly averaged and it lost some dynamics.


## Smoothing using a Savitzky-Golay filter


The Savitzky-Golay filter is a generalization of the moving average. Instead of taking the mean of the n points of a moving window, the Savitzky-Golay filter fits a polynomial of a given order over each window. A moving average is therefore a particular case of the Savitzky-Golay filter with a polynomial of order 0.

It is a powerful filter for data that is heavily quantized, particularly if we want to derive these data. Let's plot some heavily quantized data:

```{code-cell} ipython3
ts.plot(["clean", "quantized"], ".-")
```

To smooth it with a second-order Savitzky-Golay filter with a window length of 7, using {{ktk_filters_savgol}}:

```{code-cell} ipython3
filtered = ktk.filters.savgol(ts, poly_order=2, window_length=7)
```

This gives the blue curve below, which is much smoother that the quantized one, except for the very long plateau at 10 seconds.

```{code-cell} ipython3
:tags: [remove-input]
filtered = filtered.get_subset("quantized")
filtered.rename_data("quantized", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "quantized", "filtered"], '.-')
```

## Deriving a TimeSeries

To derive a TimeSeries, use {{ktk_filters_deriv}}. For example, to derive the clean signal:

```{code-cell} ipython3
clean = ts.get_subset("clean")
derived = ktk.filters.deriv(clean)

plt.subplot(2, 1, 1)
clean.plot()
plt.title("Source")

plt.subplot(2, 1, 2)
derived.plot()
plt.title("Derived")

plt.tight_layout()
```

This works well for signals that are not noisy. For noisy signals, we usually filter the signals before deriving. However, heavily quantized signals are often difficult to derive even when filtered, because they contain lots of plateaus that, once derived, are transformed into series of spikes. For instance, let's repeat the derivation above with a quantized signal:

```{code-cell} ipython3
quantized = ts.get_subset("quantized")
derived = ktk.filters.deriv(quantized)

plt.subplot(2, 1, 1)
quantized.plot()
plt.title("Source")

plt.subplot(2, 1, 2)
derived.plot()
plt.title("Derived")

plt.tight_layout()
```


Instead of deriving the signal directly, we could filter it using a Savitzky-Golay and derivate the fitted polynomial instead. This generally results in much better results. Using a 2nd-order Savitzky-Golay filter with a window length of 7:

```{code-cell} ipython3
quantized = ts.get_subset("quantized")
derived = ktk.filters.savgol(
    quantized, poly_order=2, window_length=7, deriv=1
)

plt.subplot(2, 1, 1)
quantized.plot()
plt.title("Source")

plt.subplot(2, 1, 2)
derived.plot()
plt.title("Derived")

plt.tight_layout()
```

The derivative of the highly-quantized signal is indeed similar to the derivative of the clean signal.


## Removing artefacts using a median filter

Sometimes, a TimeSeries contains some bad measurements that really stand out from other data. If such artefacts are impossible to remove at the source and there are not too many of them, then the median filter is a simple way to filter them out. For example, using a median filter with a window length of 3 gives, for each point, the average of the two points that are the closest together.

```{code-cell} ipython3
artefacts = ts.get_subset("artefacts")
filtered = ktk.filters.median(artefacts, window_length=3)

# Plot both
filtered = filtered.rename_data("artefacts", "filtered")
artefacts.merge(filtered).plot()
```

Most artefacts were removed, but not the ones at 30 and 31 seconds. This is because there were two consecutive artefacts, and as such the median filter considers that at these times, the clean signal is the artefact. A filter with a larger window length could be used, at the expense of more signal loss.

```{code-cell} ipython3
artefacts = ts.get_subset("artefacts")
filtered = ktk.filters.median(artefacts, window_length=5)

# Plot both
filtered = filtered.rename_data("artefacts", "filtered")
artefacts.merge(filtered).plot()
```
