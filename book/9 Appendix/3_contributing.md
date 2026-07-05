# Contributing

There is no need to be a developer to contribute to this project. Here are some ways to help:

## As a user (or potential user)

- [Install Kinetics Toolkit](../1%20Getting%20Started/2_getting_started_installing.md), browse the [documentation](https://kineticstoolkit.uqam.ca), try it and check how it fits your workflow;
- Talk about it in your networks;
- Share your success, make suggestions, propose ideas, on the [discussions forum](https://github.com/felixchenier/kineticstoolkit/discussions);
- Report bugs on the [issue tracker](https://github.com/felixchenier/kineticstoolkit/issues);
- Consider [citing it](1_citing.md) in your work;

## As an instructor

- Browse the [documentation](https://kineticstoolkit.uqam.ca);
- Make suggestions and propose ideas on the documentation, on the [discussions forum](https://github.com/felixchenier/kineticstoolkit/discussions).

## As a developer

- [Clone the latest master branch](dev_installing_from_github.md) and start playing with the unstable stuff;
- Make suggestions for improvements, new features, etc. on the [discussions forum](https://github.com/felixchenier/kineticstoolkit/discussions);
- Develop new code or improve the existing one, after reading the development rules below.

## Development rules

### Rule 1: Code of conduct

Please make sure to adhere to our [code of conduct](4_code_of_conduct.md).

### Rule 2: Consider writing documentation instead of code

Before even starting to develop a new function, one should ask this important question: **Should this feature really be developed, or should I write a tutorial instead?**

We remind that Kinetics Toolkit aims to provide tools for the user to achieve their needs in biomechanical research. Often, the best way to control our data is by learning how to do it instead of using a function performs it for us. In that view, any new feature should start with a [discussion](https://github.com/felixchenier/kineticstoolkit/discussions).

- To develop documentation, please contribute to the [kineticstoolkit_doc](https://github.com/felixchenier/kineticstoolkit_doc) repository, that versions this website's code.
- Otherwise, to develop code, then continue with this guide.

### Rule 3: For new features, consider writing an extension

Extensions are a good way to write and share features that may be too specific to be included in the code distribution os Kinetics Toolkit, or to develop and test new features.

### Rule 4: Contributing code to the core library

Before contributing code to the core library, please start a [discussion](https://github.com/felixchenier/kineticstoolkit/discussions) to avoid misunderstanding or disappointment before even starting to code. Everybody's efforts should converge toward an efficient direction. Once we agree on the feature being developed, use the usual method of forking, writing, testing, and writing a pull request that is described [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/getting-started/about-collaborative-development-models).

Before creating a pull request, please ensure that:

- The new code respects the [coding style](dev_coding_style.md).
- Your new code is tested using proper unit tests.

To ensure that this is the case, run `ktk.dev.run_tests()`. You should get no error.


## Coding style

### Standard Python conventions

Coding style is [black](https://black.readthedocs.io/en/stable) with 79-character lines. Docstrings style is [Numpy Docstring](https://numpydoc.readthedocs.io/en/latest/format.html).

### Naming conventions

The following PEP8 conventions are used:

- All code, comments and documentation are in **English**.
- **Function names** are active (begin by a verb), and are in snake_case (lowercase words separated by underscores):
    - close()
    - calculate_power()
    - detect_cycles()
- **Variable names** are passive, and are also in snake_case:
    - forces
    - detected_markers
- **Class names** are passive, and are in CapitalCase (Capital first letters):
    - TimeSeries
    - Player
- **Constants** are passive, and are in UPPER_SNAKE (uppercase words separated by underscores):
    - CALIBRATION_MATRIX
    - WHEEL_RADIUS

In addition, the following convention is used:

- For strings that are used as identifiers (e.g., keys, signal names), **strings contents** are in CapitalCase:
    - contents['Forces'], kinematics.data['UpperArmR']
    - dataframe.columns = ['SolidTire', 'InflatableTire']

### Type hints

Kinetics Toolkit is type-hinted using python 3.10 annotations.


