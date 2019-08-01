from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

from carbonium.version import __version__

setup(
    name="carbonium",
    version=__version__,
    url="https://github.com/pietrogiuffrida/carbonium/",
    author="Pietro Giuffrida",
    author_email="pietro.giuffri@gmail.com",
    license="MIT",
    packages=["carbonium"],
    zip_safe=False,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    description="Manage a list of names with several "
    "properties and (overlapping) order criteria",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
