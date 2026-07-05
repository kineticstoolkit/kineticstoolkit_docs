# Installing Python and Kinetics Toolkit

This section shows you how to install Python, its main scientific packages such as NumPy, Matplotlib, and the Kinetics Toolkit package.


## Step 1 - Install a conda distribution[^pip]

Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Miniforge](https://conda-forge.org/download).

[^pip]: All packages can be installed using pip using `pip install kineticstoolkit`. However, we recommend using Conda because it facilitates the management of virtual environments and integrates easily with the Spyder IDE that we also recommend.


## Step 2 - Install Python and selected scientific packages

These commands create the `ktk` environment. We recommend installing in such a separate environment; this way, when you will mess up (we all do), you can simply delete and recreate the environment.

On Windows, launch `Anaconda Prompt` (if you installed Miniconda) or `Miniforge Prompt` (if you installed Miniforge). On macOS and Linux, launch a terminal. Then type:

```
conda create -n ktk -c conda-forge kineticstoolkit spyder-kernels
```

Press `y` to confirm and wait until the installation completes.
