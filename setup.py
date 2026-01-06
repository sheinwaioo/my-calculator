from setuptools import setup, find_packages

setup(
    name="calculator-app",
    version="0.1.0",
    package_dir={"": "."},
    packages=find_packages(where="."),
)
