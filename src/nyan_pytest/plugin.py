"""Pytest plugin for Nyan Cat test reporter."""

import os
import sys
import time
import pytest
from typing import Dict, List, Optional, Tuple, Any

TERM_WIDTH = 80
try:
    # Get terminal width if supported
    from shutil import get_terminal_size

    TERM_WIDTH = get_terminal_size().columns
except (ImportError, AttributeError):
    pass


def is_interactive_terminal() -> bool:
    """Check if we're running in an interactive terminal."""
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


class NyanReporter:
    """Nyan Cat pytest reporter."""

    # ANSI escape codes for colors
    COLORS = {
        "reset": "\033[0m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
        "bg_black": "\033[40m",
        "bg_red": "\033[41m",
        "bg_green": "\033[42m",
        "bg_yellow": "\033[43m",
        "bg_blue": "\033[44m",
        "bg_magenta": "\033[45m",
        "bg_cyan": "\033[46m",
        "bg_white": "\033[47m",
    }

    # Move cursor up n lines
    UP = "\033[{0}A"
    # Clear from cursor to end of screen
    CLEAR_SCREEN = "\033[0J"
    # Save cursor position
    SAVE_CURSOR = "\033[s"
    # Restore cursor position
    RESTORE_CURSOR = "\033[u"

    # Rainbow colors for the trail
    RAINBOW_COLORS = ["red", "yellow", "green", "cyan", "blue", "magenta"]

    # Nyan cat frames with consistent head position and moving paws
    NYAN_FRAMES = [
        [
            "≈≈╭━━━━━━━━━━━━╮",
            "≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮",
            "≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)",
            "≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈  ╰┛ ╰┛ ╰┛ ╰┛",
        ],
        [
            "≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮",
            "≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)",
            "≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈╰┛ ╰┛  ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈╭┫ ♥ * ♥ * ♥ *┣╮ ╮",
            "≈≈≈┃┃* ♥ * ♥ * ♥ (^ᴥ^)",
            "≈≈≈-┫ ♥ * ♥ * ♥ *┣ ",
            "≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈╰┛ ╰┛ ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈╭┫ ♥ * ♥ * ♥ *┣╮ ╮",
            "≈≈≈≈┃┃* ♥ * ♥ * ♥ (^ᴥ^)",
            "≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈╰┛ ╰┛  ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮",
            "≈≈≈≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)",
            "≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈≈  ╰┛ ╰┛ ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮",
            "≈≈≈≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)",
            "≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈≈≈ ╰┛ ╰┛  ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┣╮ ╮",
            "≈≈≈≈≈┃┃* ♥ * ♥ * ♥ (^ᴥ^)",
            "≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣ ",
            "≈≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈≈≈╰┛ ╰┛ ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┣╮ ╮",
            "≈≈≈≈≈┃┃* ♥ * ♥ * ♥ (^ᴥ^)",
            "≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈≈╰┛ ╰┛  ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮",
            "≈≈≈≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)",
            "≈≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈≈  ╰┛ ╰┛ ╰┛ ╰┛",
        ],
        [
            "≈≈≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈≈≈╭┫ ♥ * ♥ * ♥ *┃ ╮ ╮",
            "≈≈≈≈┃┃* ♥ * ♥ * ♥ ┃(^ᴥ^)",
            "≈≈≈≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈≈≈ ╰┛ ╰┛  ╰┛ ╰┛",
        ],
        [
            "≈≈≈╭━━━━━━━━━━━━╮",
            "≈≈╭┫ ♥ * ♥ * ♥ *┣╮ ╮",
            "≈≈┃┃* ♥ * ♥ * ♥ (^ᴥ^)",
            "≈≈-┫ ♥ * ♥ * ♥ *┣ ",
            "≈≈≈╰━━━━━━━━━━━━╯",
            "≈≈≈≈╰┛ ╰┛ ╰┛ ╰┛",
        ],
        [
            "≈≈╭━━━━━━━━━━━━╮",
            "≈╭┫ ♥ * ♥ * ♥ *┣╮ ╮",
            "≈┃┃* ♥ * ♥ * ♥ (^ᴥ^)",
            "≈-┫ ♥ * ♥ * ♥ *┣╯",
            "≈≈╰━━━━━━━━━━━━╯",
            "≈≈╰┛ ╰┛  ╰┛ ╰┛",
        ],
    ]

    def __init__(self, config: pytest.Config) -> None:
        """Initialize the reporter."""
        self.config = config
        self.nyan_only = config.getoption("--nyan-only")
        self.interactive = is_interactive_terminal()
        self.width = min(TERM_WIDTH, 80)

        # Test counters
        self.passed = 0
        self.failed = 0
        self.skipped = 0
        self.total = 0

        # Animation state
        self.tick = 0
        self.trail_length = 0
        self.max_trail_length = max(
            0, self.width - 24
        )  # Reserve more space for wider cat

        self.started = False
        self.finished = False

    def pytest_configure(self, config: pytest.Config) -> None:
        """Configure the plugin."""
        if self.nyan_only:
            # Unregister other reporters
            standard_reporter = config.pluginmanager.getplugin("terminalreporter")
            if standard_reporter:
                config.pluginmanager.unregister(standard_reporter)

    def pytest_collection_finish(self, session: pytest.Session) -> None:
        """Called after collection is finished."""
        self.total = len(session.items)
        if self.interactive:
            for _ in range(12):  # Reserve more lines for the taller nyan cat display
                sys.stdout.write("\n")
            # Move cursor back up and save position
            sys.stdout.write(self.UP.format(12))
            sys.stdout.write(self.SAVE_CURSOR)
            sys.stdout.flush()
            self.started = True

    def pytest_runtest_logreport(self, report: pytest.TestReport) -> None:
        """Called for test setup/call/teardown."""
        if report.when != "call":
            return

        # Update counters
        if report.passed:
            self.passed += 1
        elif report.failed:
            self.failed += 1
        elif report.skipped:
            self.skipped += 1

        # Update display
        self.update_display()

    def update_display(self) -> None:
        """Update the display."""
        if not self.interactive or self.finished:
            return

        # Calculate progress percentage for trail length
        if self.total > 0:
            progress = min(1.0, (self.passed + self.failed + self.skipped) / self.total)
            self.trail_length = int(progress * self.max_trail_length)

        # Frame animation
        frame = self.NYAN_FRAMES[self.tick % len(self.NYAN_FRAMES)]
        self.tick += 1

        # Restore cursor position and clear screen
        sys.stdout.write(self.RESTORE_CURSOR)
        sys.stdout.write(self.CLEAR_SCREEN)

        # Draw rainbow trail and nyan cat
        for i, line in enumerate(frame):
            rainbow_segment = ""
            if 0 <= i <= 8:  # Draw rainbow on all body lines including paws
                for j in range(self.trail_length):
                    color_idx = (j + i + self.tick) % len(self.RAINBOW_COLORS)
                    color = self.RAINBOW_COLORS[color_idx]
                    rainbow_segment += f"{self.COLORS[color]}={self.COLORS['reset']}"

            # Apply colors to specific characters in the line
            colored_line = ""
            for char in line:
                if char == "♥":
                    colored_line += (
                        f"{self.COLORS['bright_magenta']}{char}{self.COLORS['reset']}"
                    )
                elif char == "*":
                    colored_line += (
                        f"{self.COLORS['bright_yellow']}{char}{self.COLORS['reset']}"
                    )
                else:
                    colored_line += char

            # Print the line with rainbow trail and colored characters
            sys.stdout.write(f"{rainbow_segment}{colored_line}\n")

        # Print stats
        status = (
            f"Tests: {self.passed + self.failed + self.skipped}/{self.total} "
            f"✅ {self.passed} ❌ {self.failed} ⏭️  {self.skipped}"
        )
        sys.stdout.write(f"\n{status}\n")
        sys.stdout.flush()

        # Slow down animation to reduce CPU usage
        time.sleep(0.1)

    def pytest_terminal_summary(self, terminalreporter: Any, exitstatus: int) -> None:
        """Called at the end of the test session."""
        self.finished = True

        if self.interactive:
            # Print the final frame with full rainbow and status
            sys.stdout.write(self.RESTORE_CURSOR)
            sys.stdout.write(self.CLEAR_SCREEN)

            # Draw a victory frame with full rainbow
            frame = self.NYAN_FRAMES[0]  # Use the first frame for the final display

            # Set trail length to maximum for a complete rainbow
            self.trail_length = self.max_trail_length

            # Draw rainbow trail and final nyan cat
            for i, line in enumerate(frame):
                rainbow_segment = ""
                if 0 <= i <= 8:  # Draw rainbow on all body lines including paws
                    for j in range(self.trail_length):
                        color_idx = (j + i) % len(self.RAINBOW_COLORS)
                        color = self.RAINBOW_COLORS[color_idx]
                        rainbow_segment += (
                            f"{self.COLORS[color]}={self.COLORS['reset']}"
                        )

                # Apply colors to specific characters in the line
                colored_line = ""
                for char in line:
                    if char == "♥":
                        colored_line += f"{self.COLORS['bright_magenta']}{char}{self.COLORS['reset']}"
                    elif char == "*":
                        colored_line += f"{self.COLORS['bright_yellow']}{char}{self.COLORS['reset']}"
                    else:
                        colored_line += char

                # Print the line with rainbow trail and colored characters
                sys.stdout.write(f"{rainbow_segment}{colored_line}\n")

            # Print final status below the cat
            result = "passed" if exitstatus == 0 else "failed"
            color = "green" if exitstatus == 0 else "red"
            status = (
                f"{self.COLORS[color]}Tests {result}!{self.COLORS['reset']} "
                f"✅ {self.passed} ❌ {self.failed} ⏭️  {self.skipped}"
            )
            sys.stdout.write(f"\n{status}\n")
            sys.stdout.flush()


def pytest_addoption(parser: pytest.Parser) -> None:
    """Add nyan-cat options to pytest."""
    group = parser.getgroup("nyan", "nyan cat reporting")
    group.addoption("--nyan", action="store_true", help="Enable nyan cat output")
    group.addoption(
        "--nyan-only",
        action="store_true",
        help="Enable nyan cat output and disable default reporter",
    )
    group.addoption(
        "--nyan-sim",
        metavar="NUM_TESTS",
        type=int,
        default=0,
        help="Simulate nyan cat animation with specified number of tests",
    )


def pytest_configure(config: pytest.Config) -> None:
    """Configure the pytest session."""
    # Only register if the option is enabled
    nyan_option = config.getoption("--nyan")
    nyan_only = config.getoption("--nyan-only")
    nyan_sim = config.getoption("--nyan-sim")

    if nyan_option or nyan_only or nyan_sim > 0:
        try:
            nyan_reporter = NyanReporter(config)
            config.pluginmanager.register(nyan_reporter, "nyan-reporter")

            # If simulation mode is enabled, register a plugin with a session hook
            if nyan_sim > 0:

                class SimulationPlugin:
                    @staticmethod
                    def pytest_sessionstart(session):
                        simulate_tests(session, nyan_sim, nyan_reporter)

                config.pluginmanager.register(SimulationPlugin(), "nyan-simulation")

        except Exception as e:
            # Provide better error handling
            import sys

            print(f"Error initializing nyan-pytest reporter: {e}", file=sys.stderr)
            raise


def simulate_tests(session, num_tests, reporter):
    """Simulate test execution for the nyan cat animation."""
    import time
    import random

    # Set total number of tests for the reporter
    reporter.total = num_tests

    # Notify that we're starting simulation
    print(f"\nSimulating {num_tests} tests for nyan cat animation...")
    time.sleep(1)  # Give time for message to be read

    # Start reporter's display
    reporter.started = True

    # Simulate test results with random outcomes
    for i in range(num_tests):
        # Create a mock report
        class MockReport:
            def __init__(self):
                self.when = "call"
                r = random.random()
                if r < 0.85:  # 85% pass rate
                    self.passed = True
                    self.failed = False
                    self.skipped = False
                elif r < 0.95:  # 10% failure rate
                    self.passed = False
                    self.failed = True
                    self.skipped = False
                else:  # 5% skip rate
                    self.passed = False
                    self.failed = False
                    self.skipped = True

        # Update reporter with mock report
        reporter.pytest_runtest_logreport(MockReport())

        # Slow down simulation to make it visible (faster than real tests would run)
        time.sleep(0.02)

    # Let the animation complete
    time.sleep(1)

    # Signal the end
    print(
        f"\nSimulation complete! {reporter.passed} passed, {reporter.failed} failed, {reporter.skipped} skipped"
    )

    # Exit pytest - we don't want to run actual tests in simulation mode
    session.exitstatus = 0
    exit(0)
