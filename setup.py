from setuptools import find_packages, setup

MAJOR = 0
MINOR = 0
MICRO = 1
VERSION = "%d.%d.%d" % (MAJOR, MINOR, MICRO)

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="puts",
    version=VERSION,
    author="Mark He Huang",
    author_email="mark.h.huang@gmail.com",
    description="Python High-level Lazy Toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MarkHershey/puts",
    license="MIT",
    # package_dir=({"pylazy": "pylazy"}),
    packages=find_packages(include=["puts", "puts.*"]),
    install_requires=["colorlog>=4.1.0", "numpy"],
    extras_require={"dev": ["pytest", "tox", "wheel"]},
    keywords=[
        "utilities",
        "toolkits",
        "toolbox",
        "logger",
    ],
    # Classifiers ref: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Framework :: tox",
        "Framework :: Pytest",
    ],
    python_requires=">=3.6",
)