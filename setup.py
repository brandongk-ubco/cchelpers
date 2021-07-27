import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh.readlines() if line.strip()]

setuptools.setup(name="cchelpers",
                 version=os.environ.get("RELEASE_VERSION", "alpha"),
                 author="Brandon Graham-Knight",
                 author_email="brandongk@alumni.ubc.ca",
                 description="Helpers for working in Compute Canada.",
                 license="MIT",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url="https://github.com/brandongk-ubco/cchelpers",
                 packages=setuptools.find_packages(),
                 install_requires=requirements,
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ],
                 python_requires='>=3.7',
                 include_package_data=True)
