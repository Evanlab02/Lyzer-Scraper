"""
This module contains the functions for logging to the console using rich.
"""

from rich import print as rich_print

def create_prefix(type_of_log: str) -> str:
    """Create the prefix for the log message.

    Args:
        type_of_log (str): The type of log.

    Returns:
        str: The prefix for the log message.
    """
    type_of_log = type_of_log.upper()
    match type_of_log:
        case "ERROR":
            return "<[bold red]ERROR[/bold red]> "
        case "WARNING":
            return "<[bold yellow]WARNING[/bold yellow]> "
        case "SUCCESS":
            return "<[bold green]SUCCESS[/bold green]> "
        case "LINK":
            return "<[bold blue]LINK[/bold blue]> "
        case "MESSAGE":
            return "<[bold magenta]MESSAGE[/bold magenta]> "
        case _:
            return "<[bold cyan]INFO[/bold cyan]> "

def log_to_console(message: str, type_of_log: str = "INFO"):
    """Log a message to the console.

    Args:
        message (str): The message to log.
        type_of_log (str, optional): The type of log. Defaults to "INFO".

    Returns:
        str: The message that was logged.
    """
    message_prefix = create_prefix(type_of_log)
    console_message = f"{message_prefix}{message}"
    rich_print(console_message)
    return console_message
