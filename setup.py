import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="atdate",
    version="0.0.1-dev9",
    author="Przemysław Pietras",
    author_email="przemyslawp94@gmail.com",
    description="Simple linux at command string parser",
    keywords='at date datetime parse',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/destag/at-date",
    packages=setuptools.find_packages(exclude=['test']),
    install_requires=[
        'lark-parser >= 0.6.3',
        'python-dateutil >= 2.7.3'
    ],
    tests_require=[
        'pytest',
        'freezegun'
    ],
    test_suite='test',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
