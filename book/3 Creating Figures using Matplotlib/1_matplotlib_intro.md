---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.4
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---


# Introduction to Matplotlib

Matplotlib is a standard for producing high-quality and interactive figures. The pyplot module is highly similar to Matlab's plotting functions, and offers an easy-to-understand, yet very powerful way to produce figures.

:::{figure}
:label: matplotlib_logo
:width: 4in
![](../../_static/images/matplotlib_logo.png)

Matplotlib logo
:::


Matplotlib can generate a wide variety of plots. Here are different examples that are relevant to biomechanics, reproduced from the {{matplotlib}} website:



|              {{plt_plot}}               |              {{plt_scatter}}               | 
|:---------------------------------------:|:------------------------------------------:|
| ![](../../_static/images/matplotlib_plot.jpg) | ![](../../_static/images/matplotlib_scatter.jpg) |

|              {{plt_fill_between}}               |              {{plt_imshow}}               |
|:-----------------------------------------------:|:-----------------------------------------:|
| ![](../../_static/images/matplotlib_fill_between.jpg) | ![](../../_static/images/matplotlib_imshow.jpg) |

|              {{plt_errorbar}}               |              {{plt_bar}}               | 
|:-------------------------------------------:|:--------------------------------------:|
| ![](../../_static/images/matplotlib_errorbar.jpg) | ![](../../_static/images/matplotlib_bar.jpg) |

This chapter focuses solely on line plots using {{plt_plot}}. However, after learning this type of plot and [](../4%20Manipulating%20Arrays%20using%20Numpy/1_numpy_intro.md), any other type of plot will become relatively easy to draw just by reading their documentation.


## Importing **pyplot**

