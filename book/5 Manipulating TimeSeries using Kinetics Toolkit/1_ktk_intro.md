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

# Introduction to Kinetics Toolkit

#todo Explain why ktk is well suited for biomechanics compared to barebones numpy and matplotlib.

You can import the `kineticstoolkit` module using two methods:

- Standard: `import kineticstoolkit as ktk`
- Lab mode: `import kineticstoolkit.lab as ktk`

Lab mode is a convenience tool that sets some defaults for a more enjoyable data processing session in IPython-based environments such as Spyder. It makes cosmetic changes to the representations (repr) of dictionaries, arrays, and warnings, and improves Matplotlib default colours and sizes for interactive biomechanics work. See {{ktk_change_defaults}} for more information. All tutorials in this book use this mode.

```
import kineticstoolkit.lab as ktk
```

is equivalent to:

```
import kineticstoolkit as ktk
ktk.change_defaults()
```

