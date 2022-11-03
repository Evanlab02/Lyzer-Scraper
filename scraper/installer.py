"""
This module will contain the class that will be used to install the scraper.
"""

import os
import PyInstaller

class Installer:
    """
    This class will be used to install the scraper.
    """

    def __init__(self):
        """
        This is the constructor for the installer class.
        """
        self.pyinstaller_version = PyInstaller.__version__ # Version of PyInstaller
        self.platform = PyInstaller.PLATFORM # Platform that PyInstaller is running on4
        self.home_directory = os.path.expanduser("~") # Home directory

    def introduce(self):
        """
        This will introduce the installer to the user.

        Returns:
            self (Installer): The installer object.
        """
        print("\nHello, I am the installer for the scraper.")
        print("I was created using PyInstaller version " + self.pyinstaller_version)
        print("I am from platform " + self.platform)
        print("I have found your home directory to be " + self.home_directory)
        print()
        return self

    def install_data_directory(self, data_directory: str = ".lyzer/"):
        """
        This will install the data directory.

        Args:
            data_directory (str): The data directory to install.

        Returns:
            (Bool): True if the data directory was installed, False otherwise.
        """
        data_directory = os.path.join(self.home_directory, data_directory)
        if not os.path.exists(data_directory):
            os.makedirs(data_directory)
            print("Found that data directory did not exist, created data directory at " \
                + data_directory)
            return True
        return False

    def remove_data_directory(self, data_directory: str):
        """
        This will remove the data directory.

        Args:
            data_directory (str): The data directory to remove.

        Returns:
            (Bool): True if the data directory was removed, False otherwise.
        """
        data_directory = os.path.join(self.home_directory, data_directory)
        if os.path.exists(data_directory):
            os.removedirs(data_directory)
            print("Removed data directory at " + data_directory)
            return True
        return False

    def install_data_file(self, data_file: str, data_directory: str=".lyzer/"):
        """
        This will install the data file.

        Args:
            data_file (str): The data file to install.

        Returns:
            (Bool): True if the data file was installed, False otherwise.
        """
        data_directory = os.path.join(self.home_directory, data_directory)
        data_file = os.path.join(data_directory, data_file)
        if not os.path.exists(data_file):
            with open(data_file, "w", encoding="utf-8"):
                print("Found that data file did not exist, created data file at " + data_file)
                return True
        return False


    def remove_data_file(self, data_file: str, data_directory: str=".lyzer/"):
        """
        This will remove the data file.

        Args:
            data_file (str): The data file to remove.

        Returns:
            (Bool): True if the data file was removed, False otherwise.
        """
        data_directory = os.path.join(self.home_directory, data_directory)
        data_file = os.path.join(data_directory, data_file)
        if os.path.exists(data_file):
            os.remove(data_file)
            print("Removed data file at " + data_file)
            return True
        return False
