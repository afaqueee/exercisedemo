import setuptools

setuptools.setup(
    name="housing_package",
    version="0.0.1",
    author="Anant Chandak",
    author_email="anant.chandak@tigeranalytics.com",
    description="Housing data package",
    long_description="A python package for housing data code",
    long_description_content_type="text/markdown",
    url="https://github.com/chandakanant/mle-training",
    project_urls={
        "Bug Tracker": "https://github.com/chandakanant/mle-training/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
