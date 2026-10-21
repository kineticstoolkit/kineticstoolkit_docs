# Reading/writing JSON files

#todo talk about jason first, then zipped json, then ktk.zip

Contrarily to Matlab's MAT file, Python does not come with a single standard way to save data. To ease saving and sharing data, Kinetics Toolkit provides two functions to load and save in its own ktk.zip format:

- {{ktk_save}}
- {{ktk_load}}

These functions are straightforward. To save a variable:

```
ktk.save(filename, variable)
```

To load a variable:

```
variable = ktk.load(filename)
```


## File format and supported types

The `ktk.zip` file format is built to be as portable and simple as possible. It is a standard zip file that contains two JSON files:

- `metadata.json`: File metadata such as the save date, the computer's operating system, the version of the ktk.zip format, etc.
- `data.json`: The data. Data types that are not natively supported by the JSON file format (e.g., NumPy arrays, Pandas DataFrames, Kinetics Toolkit's TimeSeries) are converted to supported objects, and reconverted back on loading.

The `ktk.zip` file format supports any combination of the following types:

| Already supported by JSON          | Extended for Kinetics Toolkit |
| ---------------------------------- | ----------------------------- |
| dict containing any supported type | numpy.ndarray                   |
| list containing any supported type | pandas.DataFrame              |
| str                                | pandas.Series                 |
| int                                | kineticstoolkit.TimeSeries    |
| float                              |                               |
| True, False, None                  |                               |

Tuples can also be saved but are loaded back as lists.

## Reading a ktk.zip file in Matlab

Here are how to load a ktk.zip file in Matlab, using four instructions.

```
% Create a temporary folder to unzip to
mkdir('temp');
unzip(filename, 'temp');

% Load the file contents
data = jsondecode(fileread('temp/data.json'));
metadata = jsondecode(fileread('temp/metadata.json'));
```

Since types differ between JSON and Matlab, then some conversion will happen. Refer to [Matlab's documentation](https://www.mathworks.com/help/matlab/ref/jsondecode.html) to know how a variable type will be interpreted by Matlab.
