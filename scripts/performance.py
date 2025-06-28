#!/usr/bin/env python3
"""Performance comparison script for nyan-pytest."""

import subprocess
import sys
import time
import os
from pathlib import Path


def run_standard_simulation(num_tests: int) -> tuple[float, int]:
    """Run standard simulation without nyan animation."""
    print(f"1. Standard pytest output simulation ({num_tests} tests):")
    
    start = time.time()
    result = subprocess.run([
        'python', '-c',
        f'import time; '
        f'print("Simulating {num_tests} tests for standard pytest..."); '
        f'[time.sleep(0.01) for i in range({num_tests})]; '
        f'print("Simulation complete! Standard pytest output")'
    ])
    elapsed = time.time() - start
    
    avg_ms = (elapsed / num_tests) * 1000
    print(f"\nTime: {elapsed:.3f}s | Tests: {num_tests} | Avg: {avg_ms:.1f}ms/test", file=sys.stderr)
    
    return elapsed, num_tests


def run_nyan_simulation(num_tests: int) -> tuple[float, int]:
    """Run nyan simulation with full animation."""
    print(f"\n2. Nyan pytest simulation ({num_tests} tests - with animation):")
    
    start = time.time()
    result = subprocess.run(['python', '-m', 'pytest', '--nyan-sim', str(num_tests)])
    elapsed = time.time() - start
    
    avg_ms = (elapsed / num_tests) * 1000
    print(f"\nTime: {elapsed:.3f}s | Tests: {num_tests} | Avg: {avg_ms:.1f}ms/test", file=sys.stderr)
    
    return elapsed, num_tests


def print_comparison(std_time: float, std_tests: int, nyan_time: float, nyan_tests: int):
    """Print performance comparison table."""
    print("\n📊 Performance Summary:")
    print("======================")
    
    std_avg = (std_time / std_tests) * 1000
    nyan_avg = (nyan_time / nyan_tests) * 1000
    overhead = nyan_time - std_time
    overhead_pct = (overhead / max(std_time, 0.001)) * 100
    
    print(f"Standard:  {std_time:.3f}s total | {std_avg:.1f}ms/test")
    print(f"Nyan:      {nyan_time:.3f}s total | {nyan_avg:.1f}ms/test")
    print(f"Overhead:  {overhead:+.3f}s total | {overhead_pct:+.1f}% slower")


def main():
    """Main performance comparison function."""
    # Get number of tests from command line or default to 100
    num_tests = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    
    print(f"Performance comparison: {num_tests} simulated tests")
    print("=" * 42)
    
    # Run standard simulation
    std_time, std_tests = run_standard_simulation(num_tests)
    
    # Run nyan simulation
    nyan_time, nyan_tests = run_nyan_simulation(num_tests)
    
    # Print comparison
    print_comparison(std_time, std_tests, nyan_time, nyan_tests)


if __name__ == "__main__":
    main()