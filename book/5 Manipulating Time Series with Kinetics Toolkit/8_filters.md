# Filtering TimeSeries

Most recorded data needs to be filtered at some point. This section introduces the most common frequency-domain and time-domain filters in biomechanical analysis, and show how to apply them directly on TimeSeries.



## Removing frequencies using a Butterworth filter

The Butterworth filter may be the most used filter in biomechanics. It removes ranges of frequencies from the signal's frequency spectrum. Normally, we first identify the frequency range of our data, so that we can remove any signal frequencies outside this range.

Let's start by loading some noisy data.

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts_noisy = ktk.load(ktk.doc.download("filters_noisy_signals.ktk.zip"))

ts_noisy.plot();
```

### Low-pass filter

The default setting for {{ktk_filters_butter}} is to apply a low-pass, no-lag filter of order 2. To filter with a cut-off frequency of 20 Hz:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, fc=20)
ts_filtered.plot()
```

You are encouraged to experiment with different cut-off frequencies to observe its effect on the results. In the figure above, we observed that while 20 Hz was probably correct for the sine wave, it still filtered out the most dynamic components, most notably in the square and pulse signals.

### High-pass filter

The inverse operation is the high-pass filter. Let's observe what we removed from the original signal in the figure above:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, btype="highpass", fc=20)
ts_filtered.plot()
```

Only the transitions were kept; all the stable parts of the signal were removed.

### Band-pass filter

We can combine both low-pass and high-pass in a band-pass filter. This type of filter is commonly used in processing of electromyography, to filter both high-frequency noise and low-frequency movement artifact.

To remove frequencies between 10 and 80 Hz:

```{code-cell} ipython3
ts_filtered = ktk.filters.butter(ts_noisy, btype="bandpass", fc=[10, 80])
ts_filtered.plot()
```


## 💪 Exercise

Using this [dataset](../../5%20Appendix/dataset_emg.md) with one surface EMG electrode on the biceps brachii:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import numpy as np

filename = ktk.doc.download("emg_biceps_brachii.ktk.zip")
emg = ktk.load(filename)
emg.plot()
```

Write code that generates new data named "Envelope" in the TimeSeries, which corresponds to the envelope of this signal. Follow these three steps:
1. Filter the TimeSeries with a band-pass Butterworth filter from 20 Hz to 500 Hz to reject high-frequency noise and body movement artifacts.

```{code-cell} ipython3
:tags: [hide-cell]

filtered_emg = ktk.filters.butter(emg, btype="bandpass", fc=[20, 500])
filtered_emg.plot()
```

2. Rectify the filtered TimeSeries by replacing every data point with its absolute value. You may use {{np_abs}}.

```{code-cell} ipython3
:tags: [hide-cell]

filtered_emg.data["BicepsBrachiiR"] = np.abs(filtered_emg.data["BicepsBrachiiR"])
filtered_emg.plot()
```

3. Filter the rectified TimeSeries with a low-pass Butterworth filter with a cut-off frequency of 10 Hz.

```{code-cell} ipython3
:tags: [hide-cell]

filtered_emg = ktk.filters.butter(filtered_emg, fc=10)

# Add the filtered signal as Envelope in the original TimeSeries
# There are many ways to do this, here is a robust one:
filtered_emg = filtered_emg.rename_data("BicepsBrachiiR", "Envelope")
emg = emg.merge(filtered_emg)

# Plot the result
emg.plot()
```



## Smoothing using a moving average

The moving average is an excellent filter to remove noise that is related to a specific time pattern. A classic example is the day-to-day evaluation of a process that is sensitive to weekends (for example, the number of workers who enter a building). A moving average with a window length of 7 days is ideal to evaluate the general trend of this signal without considering intra-week fluctuations. Let's first load some noisy data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk
import matplotlib.pyplot as plt

ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

ts.plot(["clean", "periodic_noise"], '.-')
```

This signal contains periodic noise with a period of five seconds. Using {{ktk_filters_smooth}} to create a 5-second moving average filter:

```{code-cell} ipython3
filtered = ktk.filters.smooth(ts, window_length=5)
```

gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("periodic_noise", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "periodic_noise", "filtered"], '.-')
```

As expected, the 5-sample period noise was completely removed. The signal was, however, also averaged and we therefore lost some dynamics in the signal.


## Smoothing using a Savitzky-Golay filter


The Savitzky-Golay filter is a generalization of the moving average. Instead of taking the mean of the n points of a moving window, the Savitzky-Golay filter fits a polynomial of a given order over each window. A moving average is therefore a particular case of the Savitzky-Golay filter with a polynomial of order 0.

It is a powerful filter for data that is heavily quantized, particularly if we want to derive these data. Let's plot some heavily quantized data:

```{code-cell} ipython3
ts.plot(["clean", "quantized"], ".-")
```

Using {{ktk_filters_savgol}} to smooth this signal using a second-order Savitzky-Golay filter with a window length of 7:

```{code-cell} ipython3
filtered = ktk.filters.savgol(ts, poly_order=2, window_length=7)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("quantized", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "quantized", "filtered"], '.-')
```

## Deriving a TimeSeries

Heavily quantized signals are often difficult to derive because they contain lots of plateaus that, once derived, are transformed into series of spikes. For instance, let's see how deriving a quantized signal works without filtering, using {{ktk_filters_deriv}}:

```{code-cell} ipython3
derived = ktk.filters.deriv(ts)

derived.plot(["clean", "quantized"], ".-")
```

We can also derive a signal using a Savitzky-Golay filter using {{ktk_filters_savgol}}, which consists of deriving the polynomial that is fitted over the moving window. Using a 2nd-order Savitzky-Golay filter with a window length of 7:

```{code-cell} ipython3
derived_savgol = ktk.filters.savgol(
    ts, poly_order=2, window_length=7, deriv=1
)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
derived.rename_data("clean", "derivative of the clean signal", in_place=True)
derived.rename_data("quantized", "derived from quantized signal, without filtering", in_place=True)
derived_savgol.rename_data("quantized", "derived from quantized signal, using savgol", in_place=True)
derived_savgol.resample(derived.time, in_place=True)
derived.merge(derived_savgol).plot(
    [
        "derivative of the clean signal",
        "derived from quantized signal, without filtering",
        "derived from quantized signal, using savgol",
    ],
    '.-'
)
```

As observed, the derivative of the highly-quantized signal is similar to the derivative of the clean signal.


## Removing artefacts using a median filter

Sometimes, a TimeSeries contains some bad measurements that really stand out from other data. If such artefacts are impossible to remove at the source and there are not many of them, then the median filter is a simple way to filter them out.

Let's first load some noisy data:

```{code-cell} ipython3
import kineticstoolkit.lab as ktk

ts = ktk.load(ktk.doc.download("filters_types_of_noise.ktk.zip"))

ts.plot(["clean", "artefacts"], ".-")
```

Using a median filter with a window length of 3 gives, for each point, the average of the two points that are the closest together.

```{code-cell} ipython3
filtered = ktk.filters.median(ts, window_length=3)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("artefacts", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "artefacts", "filtered"], '.-')
```

Most artefacts were removed, but not the ones at 30 and 31 seconds. This is because there were two consecutive artefacts, and as such the median filter considers that at these times, the clean signal is the artefact. A filter with a larger window length could be used, at the expense of more signal loss.

```{code-cell} ipython3
filtered = ktk.filters.median(ts, window_length=5)
```

which gives the blue curve below:

```{code-cell} ipython3
:tags: [remove-input]
filtered.rename_data("artefacts", "filtered", in_place=True)
ts.merge(filtered).plot(["clean", "artefacts", "filtered"], '.-')
```

