# LOG

A simple and flexible logging utility for Python projects, providing easy setup and customizable logging configurations.

## Description:

This Python package offers a streamlined approach to setting up and managing logging in your projects. It provides two main functions:
- `setup_logging`: This function initializes the logging system with customizable options:
    - Creates a log directory if it doesn't exist
    - Sets up a log file with a specified name
    - Configures logging level, format, and file mode
- `get_logger`: A utility function to easily obtain a logger instance for any module or component in your project.

Key Features:
- Simple API with sensible defaults for quick setup
- Customizable log directory and file naming
- Configurable logging level and format
- Appends to existing log files by default, preserving previous logs
- Compatible with Python's built-in logging module for easy integration and extension

This package is ideal for developers who want a quick and reliable way to add logging to their Python projects without the complexity of manual logging setup. It's suitable for applications of all sizes, from small scripts to large-scale projects, providing a consistent logging approach across different modules and components.
Whether you're debugging, monitoring application behavior, or maintaining audit trails, this logging utility simplifies the process of capturing and managing log data in your Python applications.

## How to install:

Run the following command in your python venv:

```
pip install git+https://github.com/avivilloz/log.git@main#egg=log
```

Or add the following line to your project's `requirement.txt` file:

```
git+https://github.com/avivilloz/log.git@main#egg=log
```

And run the following command:

```
pip install -r requirements.txt
```

## How to use:

`setup.py`
```
from log import setup_logging

setup_logging()
```

`other.py`
```
from log import get_logger

LOG = get_logger(__name__)
LOG.info("Logging")
```