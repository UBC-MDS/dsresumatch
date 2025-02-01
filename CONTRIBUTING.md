# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

## Types of Contributions

### Report Bugs

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it.

### Write Documentation

You can never have enough documentation! Please feel free to contribute to any
part of the documentation, such as the official docs, docstrings, or even
on the web in blog posts, articles, and such.

### Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

## Get Started!

Ready to contribute? Here's how to set up `dsresumatch` for local development.

1. Download a copy of `dsresumatch` locally. This can be done either by cloning the repository or downloading the a `.ZIP` of the files on the repository.

2. Initialize a new environment:
    ```bash
    conda create -n new_env python=3.11
    ```

    And activate it:
    ```bash
    conda activate new_env
    ```

3. Ensure Poetry is installed. If not, you can install it by following the instructions on the [Poetry website](https://python-poetry.org/docs/)

4. Navigate to the folder that was downloaded in Step 1, and install `dsresumatch` using `poetry`:

    ```bash
    poetry install
    ```

5. Use `git` (or similar) to create a branch for local development and make your changes:

    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```

6. When you're done making changes, check that your changes conform to any code formatting requirements and pass any tests.

7. Commit your changes and open a pull request.

## Run tests

1. Please note that we need to have dummy.pdf and empty.pdf files in the tests folder for tests to pass

2. Run the following command for tests: 

    ```bash
    pytest tests/
    ```
    
## Branch Naming Conventions

To keep the workflow clean and organized, please follow these branch naming conventions when contributing to this project:

 • docs\: Use this prefix for branches that involve documentation updates or changes.
        Example: docs\update-readme
 • fix\: Use this prefix for branches that fix bugs or issues in the codebase.
        Example: fix\functionName
 • feature\: Use this prefix for branches that add new features, scripts, or major changes to the codebase.
        Example: feature\add-functionName

## Pull Request Guidelines

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include additional tests if appropriate.
2. If the pull request adds functionality, the docs should be updated.
3. The pull request should work for all currently supported operating systems and versions of Python.
4. New code should follow the tidyverse [style guide](http://style.tidyverse.org) or PEP8 [style guide](https://www.python.org/dev/peps/pep-0008/).

## Code of Conduct

Please note that the `dsresumatch` project is released with a
Code of Conduct. By contributing to this project you agree to abide by its terms.
