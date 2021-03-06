import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name="cchelpers",
                 version=os.environ.get("RELEASE_VERSION", "alpha"),
                 author="Brandon Graham-Knight",
                 author_email="brandongk@alumni.ubc.ca",
                 description="Helpers for working in Compute Canada.",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/brandongk-ubco/cchelpers",
                 packages=['cchelpers'],
                 install_requires=[],
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.7',
                 include_package_data=True)
