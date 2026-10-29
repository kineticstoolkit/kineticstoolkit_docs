# Chapter 5 - Working with TimeSeries

In biomechanics, we often process data that is a function of time, e.g., electromyography, point trajectories, force series, etc. When we analyze only a few data points and the sampling frequency is constant, using NumPy is usually sufficient.

However, things can get more complicated with:
- data of different natures (e.g., marker trajectories, EMG, measured forces, calculated forces);
- unsynchronized instruments
- different or inconstant sampling frequencies;
- missing data;
- noisy data;
- etc.

For these reasons, KTK provides a new type of variable: the {{ktk_timeseries}}. This chapter will learn you how to work with TimeSeries, including importing/exporting TimeSeries data, segmenting series using events, resampling and synchronizing data, filtering noisy data, working with cyclic data, and more.

