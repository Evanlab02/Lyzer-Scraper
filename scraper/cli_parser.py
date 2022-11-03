"""
This module will contain the cli parser that will be used to parse the command line arguments.
"""

def get_link(args: list):
    """
    This will process the arguments passed to find the link passed to the scraper.

    Returns:
        list(str): The link that was passed to the scraper.
    """
    print("\nParsing arguments...")
    args.pop(0) # Remove the first argument
    link = ""
    for index, arg in enumerate(args):
        if arg in ["-l", "--link"]:
            link = (args[index + 1])
    print("Here is what I found:")
    print("Link ->", link)
    return link
