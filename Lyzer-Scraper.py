"""
This is module acts as the main entry point for our web scraper program.
"""

# System imports
import sys

# Third party imports
import PyInstaller

def main():
    """
    This is the main function for our web scraper program.
    """
    print("Scraper is running...") # Print to console that scraper is running
    pyinstaller_details() # Print PyInstaller details to console
    return 0 # Exit code 0

def pyinstaller_details():
    """
    This function prints the PyInstaller details to the console.
    """
    print("\nPYINSTALLER")
    print("PLATFORM ->", PyInstaller.PLATFORM)
    print("VERSION", PyInstaller.__version__)
    print("")

if __name__ == "__main__":
    exit_code = main() # Call main function
    sys.exit(exit_code) # Exit program
