import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysdb",
    version="0.0.2",
    author="Syed Aasif",
    author_email="thesyedaasif@hotmail.com",
    description="A simple lightweight portable, embeddable database library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TheSyedAasif/pysdb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
)
