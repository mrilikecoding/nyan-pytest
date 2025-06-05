# Developing Pytest Plugins

This document provides an overview of how to develop pytest plugins, with a focus on creating custom test reporters.

## Pytest Plugin Architecture

Pytest has a powerful plugin system based on the `pluggy` library. Plugins can extend pytest's functionality by implementing hooks that pytest calls during different phases of test execution.

### Key Components

1. **Hooks**: Functions that plugins can implement to modify or extend pytest's behavior
2. **Hookspecs**: Declarations of hooks that can be implemented
3. **Hookimpls**: Implementations of hooks provided by plugins
4. **Plugin Manager**: Responsible for registering and calling plugin hooks

## Creating a Custom Test Reporter

A test reporter in pytest is a plugin that receives test results and displays them in a specific format. Here's how to create one:

### 1. Hook Implementation

Key hooks for reporters:

- `pytest_configure`: Called at plugin registration time
- `pytest_collection_finish`: Called after test collection is complete
- `pytest_runtest_logreport`: Called for each test when a report is ready
- `pytest_terminal_summary`: Called at the end to provide a summary

### 2. Plugin Registration

There are two main ways to register a pytest plugin:

#### a. Using Entry Points

In `pyproject.toml`:
```toml
[project.entry-points."pytest11"]
plugin_name = "package.module"
```

#### b. Using `conftest.py`

For local plugins, you can define hooks directly in a `conftest.py` file in your project.

### 3. Implementing a Reporter

A custom reporter typically:

1. Tracks test statistics
2. Provides real-time feedback during test execution
3. Displays a summary at the end

## Existing Reporter Examples

### Built-in Reporters

1. **Default Terminal Reporter**: Implemented in `_pytest/terminal.py`
   - Shows test progress with symbols
   - Provides a summary at the end

2. **Progress Reporter**: Activated with `--progress`
   - Shows a progress bar

### Community Reporter Examples

1. **pytest-emoji**: Displays emoji instead of letters for test results
2. **pytest-sugar**: Provides a progress bar with colored output
3. **pytest-instafail**: Shows failures instantly
4. **pytest-html**: Generates HTML reports

## Example: Simple Custom Reporter

```python
class SimpleReporter:
    def __init__(self, config):
        self.config = config
        self.stats = {"passed": 0, "failed": 0, "skipped": 0}
        
    @hookimpl
    def pytest_runtest_logreport(self, report):
        if report.when == "call":  # Only count the test result after it's called
            self.stats[report.outcome] += 1
            print(f"{report.nodeid}: {report.outcome}")
            
    @hookimpl
    def pytest_terminal_summary(self):
        print("\nTest Summary:")
        for outcome, count in self.stats.items():
            print(f"{outcome.capitalize()}: {count}")
```

## Animation in Terminal Reporters

For animated or graphical reporters like Nyan Cat:

1. **Terminal Control**: Use ANSI escape codes for colors and cursor control
2. **Frame Rendering**: Clear and redraw the display for each update
3. **Progress Calculation**: Track test completion and update visuals accordingly
4. **Terminal Size**: Adjust output based on terminal dimensions
5. **Fallback Handling**: Provide graceful degradation for environments without color support

## Best Practices for Plugin Development

1. **Hooks Priority**: Use `trylast=True` or other priority hints when order matters
2. **Configuration**: Use `pytest_addoption` to add configuration options
3. **Compatibility**: Ensure your plugin works with a range of pytest versions
4. **Documentation**: Clearly document what your plugin does and how to use it
5. **Testing**: Write tests for your plugin using pytest's own testing utilities

## Resources

- [Official pytest documentation on writing plugins](https://docs.pytest.org/en/stable/how-to/writing_plugins.html)
- [Pytest hook reference](https://docs.pytest.org/en/stable/reference/reference.html#hook-reference)
- [Pluggy documentation](https://pluggy.readthedocs.io/en/latest/)
- [pytest-dev GitHub organization](https://github.com/pytest-dev) (many plugin examples)