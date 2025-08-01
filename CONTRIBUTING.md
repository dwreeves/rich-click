# Contributing

Contributions and suggestions for new features are welcome, as are bug reports!
Please create a new [issue](https://github.com/ewels/rich-click/issues)
or better still, dive right in with a pull-request.

## Local setup

Requirements:

- `uv` https://docs.astral.sh/uv/getting-started/installation/

```shell
uv python pin 3.13
uv venv .venv
source .venv/bin/activate
uv sync --extra dev
pre-commit install
```

## Pre-commit

Our pre-commit hooks contain the following hooks:

- [Prettier](https://prettier.io/): formats our markdown and yaml files nicely.
- no relative imports: prevents you from using relative imports.
- [iSort](https://pycqa.github.io/isort/): will automatically sort the imports alphabetically.
- [black](https://black.readthedocs.io/): will automatically format your code to be according to standardized python format.
- [flake8](https://flake8.pycqa.org/): will do linting checks to make sure all your code is correctly styled and used.
- [mypy](http://mypy-lang.org/): static type checker which verifies you are not using objects incorrectly.

As mentioned, some of these tools automatically fix your code while other only highlight potential issues.
Sometimes it will be enough to try to commit a second time and it will pass, while other times it may require
manual changes to your code.

In rare cases it may be difficult or undesirable to change to code to pass the linting rules.
If this happens, it's ok to add a flake8 `# noqa` or mypy `# type: ignore` comment to skip that line.
For details of how to do this, please see the [flake8 docs](https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html#in-line-ignoring-errors)
and [mypy docs](https://mypy.readthedocs.io/en/stable/common_issues.html#spurious-errors-and-locally-silencing-the-checker).

## Credits

This package was written by Phil Ewels ([@ewels](http://github.com/ewels/)),
based on initial code by Will McGugan ([@willmcgugan](https://github.com/willmcgugan)).

rich-click is co-maintained by Daniel Reeves ([@dwreeves](http://github.com/dwreeves/)).

Furthermore, these contributors helped make the package what it is today:

- [@BrutalSimplicity](https://github.com/BrutalSimplicity)
- [@harens](http://github.com/harens/)
- [@fridex](http://github.com/fridex/)
- [@pawamoy](http://github.com/pawamoy/)
- [@jorrick](http://github.com/harens/)

See the full list of contributors [here](https://github.com/ewels/rich-click/graphs/contributors).
