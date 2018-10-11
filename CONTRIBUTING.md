# Contributing to at-date

First off, thank you for considering contributing to **at-date**. We want to make contributing to this project as easy and transparent as possible.

## Our Development Process

The source code and issue tracker are hosted on GitHub. For automated testing and deployment we use Travis-CI. Test coverage is monitored with Codecov. We merge PR using **squash and merge** option.

## Pull Requests

We actively welcome your pull requests.

1. Fork the repo and create your branch from master.
2. Install `pipenv` with:
    ```bash
    pip install pipenv
    ```
3. Install dependencies with:
    ```bash
    pipenv sync --dev
    ```
4. If your change needs more dependencies, install it with:
    ```bash
    pipenv install <package_name>
    ```
5. Make code changes.
6. If you've added code that should be tested, add tests.
7. Add or change docstrings if needed.
8. Run tests with:
    ```bash
    pipenv run pytest
    ```
9. Commit changes. Use [this guide](https://chris.beams.io/posts/git-commit/) for commit message.
10. Issue that pull request!

## Code Style

Every contributor must follow the [PEP8](https://www.python.org/dev/peps/pep-0008/) code style.

### Docstrings

Always add docstrings to public callables. Below you can see our styleguide:

```python
def foo(param1, param2):
    """Short description.

    Longer description
    if needed.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        int: Sum of param1 and length of param2.

    Raises:
        ValueError: If arguments have wrong types.

    """
    return param1 + len(param2)

```

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
