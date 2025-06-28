# Makefile for nyan-pytest development

.PHONY: help setup install test test-nyan test-verbose demo demo-fast demo-slow lint format clean build upload performance check

# Default target
help: ## Show this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

# Setup and installation
setup: ## Install development dependencies and setup project
	pip install -e .
	pip install pytest black ruff mypy twine build

install: ## Install package in development mode
	pip install -e .

# Testing commands
test: ## Run tests with standard pytest output
	pytest tests/ -v

test-plugin: ## Run plugin-specific tests
	pytest tests/test_plugin.py -v

test-nyan: ## Run tests with nyan cat reporter
	pytest tests/ --nyan -v

test-nyan-only: ## Run tests with only nyan cat reporter (no standard output)
	pytest tests/ --nyan-only

test-verbose: ## Run tests with verbose nyan output and test details
	pytest tests/ --nyan -v -s

# Demo commands
demo: ## Demo nyan cat with 20 simulated tests
	python -m pytest --nyan-sim 20

demo-fast: ## Quick demo with 10 simulated tests
	python -m pytest --nyan-sim 10

demo-slow: ## Longer demo with 50 simulated tests
	python -m pytest --nyan-sim 50

demo-epic: ## Epic demo with 100 simulated tests
	python -m pytest --nyan-sim 100

# Code quality
lint: ## Run linting checks
	ruff check src/ tests/
	mypy src/

format: ## Format code with black and ruff
	black src/ tests/
	ruff format src/ tests/

check: ## Run all checks (lint + format check)
	black --check src/ tests/
	ruff check src/ tests/
	mypy src/

# Performance testing
performance: ## Compare nyan vs standard pytest performance. Usage: make performance TESTS=50 SPEED=10 (defaults: 100 tests, speed 6)
	python scripts/performance.py $(or $(TESTS),100) $(or $(SPEED),6)

benchmark: ## Benchmark the plugin performance
	@echo "Benchmarking nyan vs standard reporter..."
	@echo "Standard pytest:"
	@time python -m pytest tests/ -q > /dev/null 2>&1 || true
	@echo "Nyan pytest:"
	@time python -m pytest tests/ --nyan-only -q > /dev/null 2>&1 || true

# Build and packaging
build: ## Build the package
	python -m build

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf src/*.egg-info/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

upload-test: ## Upload to test PyPI
	twine upload --repository testpypi dist/*

upload: ## Upload to PyPI
	twine upload dist/*

# Development workflow
dev-install: clean install ## Clean install for development

full-check: clean setup check test ## Full development check (clean, setup, lint, test)

release: clean build upload ## Build and release to PyPI

# Fun extras
nyan-stats: ## Show nyan cat in action with real test statistics
	@echo "Running all tests with nyan cat reporter..."
	python -m pytest tests/ --nyan-only -v

party: ## 🎉 Nyan cat party! Usage: make party TESTS=50 (default: 100)
	python -m pytest --nyan-sim $(or $(TESTS),100)