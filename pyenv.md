# pyenv

Use different Python version.
Followed [this](https://realpython.com/intro-to-pyenv/) guide to install and learn:

## Install new versions

```bash
# List avaiable versions
pyenv install --list

# Install a given version
pyenv install <python-version>

# Install with regex
pyenv install --list | <regex>
```

## Check which versions are installed

```bash
ls ~/.pyenv/versions

# OR

pyenv versions
```

## Remove an installed version

```bash
rm -rf ~/.pyenv/versions/<version to be removed>
```

## Neat stuff


```bash
# Creates a `.python-version` file in current working directory
# Contains the given Python version
pyenv local <version>
```
