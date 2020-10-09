import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atdate",
    version="0.0.1-dev11",
    author="Przemysław Pietras",
    author_email="przemyslawp94@gmail.com",
    description="Simple linux at command string parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "atdate",
        "at",
        "date",
        "datetime",
        "time",
        "parse",
        "parser",
    ],
    url="https://github.com/destag/at-date",
    license="MIT License",
    packages=setuptools.find_packages(exclude=["test", "docs"]),
    install_requires=[
        "lark-parser >= 0.6.3",
        "python-dateutil >= 2.7.3",
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)
