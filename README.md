# CSV Data Wrangling System 

The CSV Data Wrangling System is a Python library for transforming a delimited csv data file to fit a standardized schema by applying a sequence of column transformations defined in an external transfomation configuration JSON file. 

The code is structured using the Hexagonal Architecture pattern into the following main components:
**core**: In this the model of the Order entity is defined along with the business rules such as the data transformations and validations.
**adapters**: In this the implementation for intefacing with the csv files and the transformation configuration JSON file is defined.
**application**: This is coordinating the interactions between the **core** and the **adapters**

## Features

- Configurable transformations using an external configuration JSON file
- Handles CSV files with a large number of rows
- Collects invalid rows with error descriptions
- No external dependencies
- Decoupled Implementation
- Basic unit test

## Usage

- In **main.py**, Provide the path to the input & output csv files and to transformation configuration file.
  ```
  input_file = 'input.csv'
  output_file = 'output.csv'
  config_file = 'application/config.json'
  ```
- Configure transformations in the application/config.json file

## Suggested Enhancements
- Write more unit tests
- Provide the csv files & transformation configuration file input using the arguments or the configuration file instead of the hard-coding it in the code.
