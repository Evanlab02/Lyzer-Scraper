"""
This is module acts as the main entry point for our web scraper program.
"""

# System imports
import sys

def main():
    """
    This is the main function for our web scraper program.
    """
    print("Scraper is running...") # Print to console that scraper is running
    return 0 # Exit code 0

if __name__ == "__main__":
    EXIT_CODE = main() # Call main function
    sys.exit(EXIT_CODE) # Exit program
