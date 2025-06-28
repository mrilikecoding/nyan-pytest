# Nyan Pytest

A delightful [nyan-cat](https://www.youtube.com/watch?v=2yJgwwDcgV8i) inspired pytest plugin that displays test results with a colorful nyan cat animation and rainbow trail.

```
====================================================================≈≈≈≈≈≈╭━━━━━━━━━━━━╮
====================================================================≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮
====================================================================≈≈≈≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)
====================================================================≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯
====================================================================≈≈≈≈≈≈╰━━━━━━━━━━━━╯
====================================================================≈≈≈≈≈≈  ╰┛ ╰┛ ╰┛ ╰┛

Tests: 42/50 ✅ 38 ❌ 3 ⏭️ 1
```

_Nyan cat flying through your test results with a beautiful rainbow trail!_

## IFYKYK

> Nyan Cat has always existed to bring happiness to people everywhere.

_PRGuitarman - creator of NyanCat_

> Everybody... Everybody... Everybody wants to be a CAT!

_The Aristocats_

Inspired by the original [Nyan Cat](https://knowyourmeme.com/memes/nyan-cat). This one's for the ktties.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- 🌈 **Animated rainbow trail** that grows with test progress
- 🐱 **Adorable nyan cat** with paw animations
- 📊 **Real-time test statistics** (passed, failed, skipped)
- 🎨 **Full color support** with ANSI escape codes
- 🖥️ **Terminal compatibility** for both interactive and non-interactive environments
- ⚡ **Performance optimized** for smooth animations

## Installation

```bash
pip install nyan-pytest
```

## Usage

### Basic Usage

Run pytest with nyan cat alongside standard output:

```bash
pytest --nyan
```

Use only nyan cat (cleaner output):

```bash
pytest --nyan-only
```

### Demo Mode

Want to see nyan cat in action? Try the simulation mode:

```bash
# Quick demo with 20 simulated tests
pytest --nyan-sim 20

# Epic demo with 100 tests
pytest --nyan-sim 100

# Fast animation demo
pytest --nyan-sim 30 --nyan-speed 2

# Moderate speed
pytest --nyan-sim 30 --nyan-speed 15

# Slow, relaxing animation
pytest --nyan-sim 30 --nyan-speed 50
```

## Command Line Options

| Option           | Description                                              |
| ---------------- | -------------------------------------------------------- |
| `--nyan`         | Enable nyan cat reporter alongside default pytest output |
| `--nyan-only`    | Use only nyan cat reporter (no standard pytest output)   |
| `--nyan-sim N`   | Simulate N tests to demo the animation                   |
| `--nyan-speed N` | Animation speed (1=fastest, 6=default, 100=slowest)      |

## What You'll See

When running tests, you'll see:

```
≈≈≈≈≈≈╭━━━━━━━━━━━━╮
≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮
≈≈≈≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)
≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯
≈≈≈≈≈≈╰━━━━━━━━━━━━╯
≈≈≈≈≈≈  ╰┛ ╰┛ ╰┛ ╰┛

Tests: 15/20 ✅ 12 ❌ 2 ⏭️ 1
```

- **Rainbow trail** (`≈` characters) grows as tests complete
- **Animated poptart-cat body** with hearts (♥) and sprinkles (\*)
- **Lil paws** that animate during test execution
- **Live statistics** showing progress and results
- More delightful enhancements to come! Performance is always a priority.

### Speed Guide

| Speed Range | Best For              | Description                                       |
| ----------- | --------------------- | ------------------------------------------------- |
| 1-3         | Fast unit tests       | Quick visual feedback, minimal distraction        |
| 4-8         | Regular development   | Good balance of visibility and speed (default: 6) |
| 10-25       | Watching tests run    | Comfortable viewing during test execution         |
| 30-60       | Relaxed development   | Slow, enjoyable animation for longer test suites  |
| 70-100      | Demos & presentations | Very slow, perfect for showing off to colleagues! |

## Performance Impact

**TL;DR: The delight factor far outweighs the modest performance cost!**

Nyan cat adds visual joy to your testing workflow with minimal impact on development productivity. Benchmarks show the animation overhead is essentially **constant (~2.3 seconds)** regardless of test count:

### Benchmark Results

| Test Count | Standard | Nyan Cat | Overhead | % Slower |
| ---------- | -------- | -------- | -------- | -------- |
| 10 tests   | 0.18s    | 2.41s    | +2.23s   | +1225%   |
| 100 tests  | 1.26s    | 3.52s    | +2.27s   | +181%    |
| 1000 tests | 11.97s   | 14.31s   | +2.33s   | +20%     |

### Key Insights

**Animation overhead is constant** - The ~2.3 second cost doesn't scale with test count  
**Scales beautifully** - Larger test suites see proportionally less impact  
**Negligible in practice** - 2-3 seconds is nothing compared to typical development workflows

### Benchmark It Yourself

See if this would be worth it for your application tests.

```bash

# Compare with your actual test suite
time pytest your_tests/ --nyan-only
time pytest your_tests/ -q  # Standard output
```

**Bottom line:** Unless you're running thousands of ultra-fast unit tests in tight development loops, nyan cat's constant ~2.3s overhead becomes increasingly negligible as your test suite grows. The joy, motivation, and visual feedback it provides make it a net positive for virtually any development workflow. **Adoption is strongly encouraged!** 🎉

### When to Use Nyan Cat

**Perfect for:**

- **Dev workflows** - Makes test-watching enjoyable
- **Medium to large test suites** - Reasonable overhead
- **Demo environments** - Bring delight

**Why the overhead is worth it:**

- **Visual progress feedback** - Clear, delightful indication of test execution
- **Fun is good** - Brings smiles to code reviews, standups, and demos
- **Context matters** - 2.3s is negligible compared to compile times, network calls, or CI overhead

## Development

### Quick Start

For development:

```bash

git clone https://github.com/mrilikecoding/nyan-pytest

cd nyan-pytest

# Setup dependencies
make setup

# Run tests
make test-nyan

# Check code quality
make lint

# Try the demo
make demo
```

### Makefile Commands

This project includes a comprehensive Makefile for development:

```bash
# Show all available commands
make help

# Run tests with nyan cat
make test-nyan

# Demo with configurable test count
make party TESTS=50

# Performance benchmarking with configurable params
make performance TESTS=100 SPEED=6

# Development setup
make setup
```

### Available Make Commands

| Command                                | Description                                        |
| -------------------------------------- | -------------------------------------------------- |
| `make help`                            | Show all available commands                        |
| `make setup`                           | Install dev dependencies                           |
| `make test-nyan`                       | Run tests with nyan output                         |
| `make demo`                            | Demo with 20 simulated tests                       |
| `make party [TESTS=N]`                 | Configurable demo (default: 100 tests)             |
| `make performance [TESTS=N] [SPEED=N]` | Performance testing (defaults: 100 tests, speed 6) |
| `make lint`                            | Check code quality                                 |
| `make format`                          | Format code with black and ruff                    |
| `make build`                           | Build package                                      |
| `make clean`                           | Clean build artifacts                              |

## Examples

### Running Your Test Suite

```bash
# Standard pytest with nyan enhancement
pytest tests/ --nyan -v

# Clean nyan-only output
pytest tests/ --nyan-only

# Verbose mode with test details
pytest tests/ --nyan -v -s
```

### Performance Testing

```bash
# Configurable performance testing
make performance TESTS=50 SPEED=10    # 50 tests at speed 10
make performance TESTS=1000           # 1000 tests at default speed 6
make performance                      # Default: 100 tests, speed 6
```

### Demo Modes

```bash
# Standard 20-test demo
make demo

# Custom party mode with configurable test count
make party TESTS=50        # 50-test party
make party TESTS=200       # Epic 200-test party! 🎉
make party                 # Default 100-test party
```

### Benchmark It Yourself

```bash
# Run the performance comparison tool
make performance TESTS=100

# Test different scales
make performance TESTS=10    # Small suite
make performance TESTS=1000  # Large suite

# Compare with your actual test suite
time pytest your_tests/ --nyan-only
time pytest your_tests/ -q  # Standard output
```

## 🔧 Requirements

- Python 3.8+
- pytest 6.0.0+
- Terminal with ANSI color support (most modern terminals)

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Run the full test suite: `make full-check`
5. Submit a pull request

## License

MIT License - see LICENSE file for details.
