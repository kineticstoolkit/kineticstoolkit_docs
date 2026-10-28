# PART II. GOING FURTHER WITH KINETICS TOOLKIT

Although the combination of Python, {{matplotlib}}, {{numpy}} and {{pandas}} is very powerful for data processing in general, many common operations in biomechanical analysis are still complex to realize using these barebone tools.

Kinetics Toolkit (KTK) is a package that provides useful and targeted tools to biomechanics scientists, so that they do not need to program every common operation from scratch.


## Importing KTK

You can import the `kineticstoolkit` module using two methods:

- Standard: `import kineticstoolkit as ktk`
- Lab mode: `import kineticstoolkit.lab as ktk`

Lab mode is a convenience tool that sets some visualization defaults for a more enjoyable data processing session in IPython-based environments such as Spyder. Both modes are functionally equivalent; differences between both are completely cosmetic. All tutorials in this book use lab mode. See {{ktk_change_defaults}} for more information.
