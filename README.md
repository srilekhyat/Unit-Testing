# Unit-Testing
Unit Testing in Python using pytest and unittest and in C++ using Google Test (GTest) for user-defined Range class


## Unit Testing
Unit testing is a software testing method by which individual units of source code are put under various tests to determine whether they are fit for use (Source). It determines and ascertains the quality of your code.


## Pytest
pytest is a framework that makes building simple and scalable tests easy.

### Installing pytest
`pip install -U pytest`

### Running Tests
Running the command `pytest` will run all files of the form test_filename.py or filename_test.py in the current directory and its subdirectories.


## Unittest
The unittest unit testing framework supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

### Installing unittest
unittest is built into Python's standard library

### Running Tests
`import unittest `

`python -m unittest <Filename>.py`


## Google Test
It is Unit Testing Framework by Google based on the xUnit Architecture and it used in C++

### Installation
We can download GTest from the [GitHub repository of the same name](https://github.com/google/googletest).

#### Steps:
- 1. `git clone https://github.com/google/googletest`