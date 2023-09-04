import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aa-py-xl-convert",
    author="Rudolf Byker",
    author_email="rudolfbyker@gmail.com",
    description="Convert Excel files from `.xlsb` to `.xlsx`.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AutoActuary/aa-py-xl-convert",
    packages=setuptools.find_packages(exclude=["test"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    use_scm_version={
        "write_to": "aa_py_xl_convert/version.py",
    },
    setup_requires=[
        "setuptools_scm",
    ],
    install_requires=[
        "locate>=1.1.1,==1.*",
        "retry>=0.9.2,==0.9.*",
    ],
    package_data={
        "": [
            "py.typed",
            "save_as_xlsx.vbs",
        ],
    },
)
