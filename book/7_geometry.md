# Chapter 7 - 3D Geometry: points, vectors, and transforms

This chapter introduces rigid body basics such as the notions of points, vectors, and homogeneous transforms, how to navigate between local and global coordinates, and how to extract rotation angles from a series of rigid transforms. Such knowledge will be highly beneficial to fully understand kinematic analyses.

The following sections are an introduction or reminder of the basic elements of rigid body geometry. They cover the definitions of bodies, coordinate systems, and coordinates such as points, vectors, and transforms. We follow the nomenclature conventions of Craig, J., 1987. Introduction to robotics: Mechanics and control, in the context of rigid body biomechanics. 

While these notions largely come from the robotics field, they will be approached in the scope of rigid body biomechanics. We will use the posture in {numref}`fig_geometry_intro` for most examples. While this is a bidimensional example, we will treat it as a conventional 3D problem, but with all medio-lateral (z axis) coordinates being set to zero.


:::{figure}
:label:fig_geometry_intro
:width: 3in
![](_static/images/geometry_intro.png)

The posture used for the 3D geometry chapter.
:::


