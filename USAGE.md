# Using nyan-pytest

This document explains how to install and use the nyan-pytest plugin.

## Installation

### From PyPI (once published)

```bash
pip install nyan-pytest
```

### Development Installation

To install the plugin in development mode from the local repository:

```bash
# Clone the repository
git clone https://github.com/yourusername/nyan-pytest.git
cd nyan-pytest

# Install in development mode
pip install -e .
```

## Usage

### Basic Usage

Run pytest with the `--nyan` option:

```bash
pytest --nyan
```

This will show the Nyan Cat reporter alongside the default pytest reporter.

### Nyan-Only Mode

To use only the Nyan Cat reporter (disable the default reporter):

```bash
pytest --nyan --nyan-only
```

### Run the Example Tests

```bash
cd nyan-pytest
pytest tests/test_example.py --nyan
```

## Integration with Other Pytest Features

The Nyan Cat reporter works with other pytest features like:

- Verbose mode: `pytest --nyan -v`
- Test selection: `pytest --nyan tests/test_specific.py::test_function`
- Keyword filtering: `pytest --nyan -k "keyword"`

## Tips for Best Experience

1. Use a terminal with ANSI color support
2. Increase terminal height for better visualization
3. Use a monospace font to ensure proper alignment
4. If you're using a dark terminal theme, the colors will look best