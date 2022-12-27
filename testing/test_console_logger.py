"""
This module contains the class to test the console logger.
"""

import unittest

from logs.console_logger import create_prefix, log_to_console

class TestConsoleLogger(unittest.TestCase):
    """This class contains the tests for the console logger."""

    def test_create_prefix_error(self):
        """Test the create_prefix function with the error type of log."""
        self.assertEqual(create_prefix("error"), "<[bold red]ERROR[/bold red]> ")

    def test_create_prefix_warning(self):
        """Test the create_prefix function with the warning type of log."""
        self.assertEqual(create_prefix("warning"), "<[bold yellow]WARNING[/bold yellow]> ")

    def test_create_prefix_success(self):
        """Test the create_prefix function with the success type of log."""
        self.assertEqual(create_prefix("success"), "<[bold green]SUCCESS[/bold green]> ")

    def test_create_prefix_link(self):
        """Test the create_prefix function with the link type of log."""
        self.assertEqual(create_prefix("link"), "<[bold blue]LINK[/bold blue]> ")

    def test_create_prefix_message(self):
        """Test the create_prefix function with the message type of log."""
        self.assertEqual(create_prefix("message"), "<[bold magenta]MESSAGE[/bold magenta]> ")

    def test_create_prefix_info(self):
        """Test the create_prefix function with the info type of log."""
        self.assertEqual(create_prefix("info"), "<[bold cyan]INFO[/bold cyan]> ")

    def test_create_prefix_should_default_to_info(self):
        """Test the create_prefix function with a type of log that doesn't exist."""
        self.assertEqual(create_prefix("not_a_type_of_log"), "<[bold cyan]INFO[/bold cyan]> ")

    def test_log_to_console_error(self):
        """Test the log_to_console function with the error type of log."""
        self.assertEqual(log_to_console(
            "This is an error.",
            "error"),
            "<[bold red]ERROR[/bold red]> This is an error.")

    def test_log_to_console_warning(self):
        """Test the log_to_console function with the warning type of log."""
        self.assertEqual(log_to_console(
            "This is a warning.",
            "warning"),
            "<[bold yellow]WARNING[/bold yellow]> This is a warning.")

    def test_log_to_console_success(self):
        """Test the log_to_console function with the success type of log."""
        self.assertEqual(log_to_console(
            "This is a success.",
            "success"),
            "<[bold green]SUCCESS[/bold green]> This is a success.")

    def test_log_to_console_link(self):
        """Test the log_to_console function with the link type of log."""
        self.assertEqual(log_to_console(
            "This is a link.",
            "link"),
            "<[bold blue]LINK[/bold blue]> This is a link.")

    def test_log_to_console_message(self):
        """Test the log_to_console function with the message type of log."""
        self.assertEqual(log_to_console(
            "This is a message.",
            "message"),
            "<[bold magenta]MESSAGE[/bold magenta]> This is a message.")

    def test_log_to_console_info(self):
        """Test the log_to_console function with the info type of log."""
        self.assertEqual(log_to_console(
            "This is an info message.",
            "info"),
            "<[bold cyan]INFO[/bold cyan]> This is an info message.")

    def test_log_to_console_should_default_to_info(self):
        """Test the log_to_console function with a type of log that doesn't exist."""
        self.assertEqual(
            log_to_console(
                "This is an info message.",
                "not_a_type_of_log"),
                "<[bold cyan]INFO[/bold cyan]> This is an info message.")
