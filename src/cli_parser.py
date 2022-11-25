"""
This module will contain the cli parser that will be used to parse the command line arguments.
"""

from rich import print as rich_print

def get_link(args: list[str]) -> str:
    """
    This will process the arguments passed to find the link passed to the scraper.

    Args:
        args (list): The list of arguments passed to the program.

    Returns:
        str: The link that was passed to the program.
    """
    if remove_first_item(args) != 0:
        return "Unexpected Error 2"

    return find_link_in_args(args)


def remove_first_item(args: list[str]) -> int:
    """
    This function will remove the first item from the list.

    Args:
        args (list): The list to remove the first item from.

    Returns:
        int: The exit code of the function.
    """
    try:
        args.pop(0)
        return 0
    except IndexError:
        rich_print("[red]Unexpected Error 2[/red]")
        return 2


def find_link_in_args(args: list[str]) -> str:
    """
    This function will find the link in the list of arguments.

    Args:
        args (list): The list of arguments passed to the program.

    Returns:
        str: The link that was passed to the program.
    """
    try:
        link = ""
        for index, arg in enumerate(args):
            if arg in ["-l", "--link"]:
                link = (args[index + 1])
        return link
    except IndexError:
        rich_print("[red]No link passed.[/red]")
        return "No Link Passed"
