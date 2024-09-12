from setuptools import setup, find_packages

setup(
    name="logging_wrapper",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "logging",
    ],
    author="Aviv Illoz",
    author_email="avivilloz@gmail.com",
    description=(
        "A simple and flexible logging utility for Python projects, providing "
        "easy setup and customizable logging configurations."
    ),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/avivilloz/logging_wrapper",
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
