"""
Tools for Kinetics Toolkit's documentation

Author: Félix Chénier
"""

import matplotlib.pyplot as plt
import numpy as np


HIGHLIGHT_BLUE_0 = (0.8, 0.9, 1)
HIGHLIGHT_BLUE_1 = (0.5, 0.75, 1)
HIGHLIGHT_BLUE_2 = (0.2, 0.6, 1)



def draw_table(data, *, width=None, height=None, title=None, row_labels=None, col_labels=None):
    """
    Draw a table using Matplotlib and return the table object.
    
    Parameters
    ----------
    data:
        Tabular data to be printed
        
    width:
        Width of the figure, or None to adapt to the data.
        
    height:
        Height of the figure, or None to adapt to the data.

    title: str
        Figure title.
        
    Returns
    -------
    tbl
        The Matplotlib table object.
    
    """
    data = np.array(data)

    if width is None:
        width = data.shape[1]
        
    if height is None:
        height = data.shape[0]/2
    
    plt.gcf().set_size_inches(width, height)
    ax = plt.gca()
    
    tbl = plt.table(data, loc="center", rowLabels=row_labels, colLabels=col_labels)

    if title is not None:
        plt.title(title)
    tbl.scale(1, 1.5)
    plt.axis(False)
    plt.tight_layout()
    return tbl
