# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.5] - 2025-06-28

### Added
- **Animation Speed Control**: New `--nyan-speed` parameter (1-100) to control animation speed
  - 1 = fastest, 6 = default, 100 = slowest
  - Speed affects both nyan cat frames and rainbow trail animation
- **Modular Frame Architecture**: Extracted animation frames to separate `frames.py` module
  - 12 distinct nyan cat animation frames
  - Rainbow color definitions
  - Animation constants for easier modification
- **Comprehensive Test Suite**: Added complete test coverage for plugin functionality
  - Frame selection logic testing to prevent animation flicker
  - Speed functionality validation
  - Plugin integration tests
  - Mock report testing for simulation mode
  - Edge case and boundary condition testing
- **Developer Tooling**: Created extensive Makefile with 20+ development commands
  - Setup, testing, linting, performance benchmarking
  - Demo commands with different simulation sizes
  - Performance comparison tools
- **Performance Benchmarking**: Added performance comparison script
  - Benchmarks nyan vs standard pytest execution
  - Supports configurable test counts and speed settings
  - Shows timing statistics and overhead analysis

### Performance Improvements
- **Major Speed Optimization**: Removed blocking `time.sleep(0.1)` delay
  - Reduced overhead from ~10s to ~2.3s for 100 tests
  - Animation now driven by test execution rate instead of artificial delays
- **Optimized Rendering**: Batched stdout operations into single writes
  - Pre-computed colored frames to avoid repeated string processing
  - Cached rainbow segments with efficient string joins
  - Eliminated multiple small stdout writes per frame update

### Enhanced
- **Animation Quality**: Improved frame selection algorithm
  - Refactored frame selection into testable methods
  - Synchronized rainbow trail with nyan cat animation
  - Prevented frame skipping and animation flicker
- **Documentation**: Updated README with comprehensive usage instructions
  - Performance analysis section with benchmark results
  - Speed selection guide for different use cases
  - Individual developer perspective (removed "we" language)

### Fixed
- **Simulation Exit**: Fixed pytest internal error during simulation mode
  - Replaced `exit(0)` with proper `pytest.exit()` call
  - Added proper exit status handling
- **Package Structure**: Enhanced .gitignore and removed tracked build artifacts
  - Added appropriate Python package exclusions
  - Cleaned up egg-info directories from git tracking

### Technical Details
- **Frame Selection Logic**: Implemented efficient speed-based frame calculation
  ```python
  animation_tick = self.tick // self.animation_speed
  frame_idx = animation_tick % len(self._colored_frames)
  ```
- **Performance Metrics**: Achieved consistent ~2.3s overhead regardless of test count
- **Test Coverage**: 51 comprehensive tests across 6 test classes
- **Animation Frames**: 12 unique nyan cat poses with 6 lines each

## [0.1.4] - Previous Release
- Initial performance optimizations
- Basic nyan cat animation implementation