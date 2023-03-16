echo "Requires python 3.10"
echo "Requires pip - On path"
echo "Requires pipenv - On path"
echo "Requires chrome-browser"
echo "Requires Make"
echo "Requires zip"
read -p "Press any key to continue..." -n1 -s

echo ""
echo "--------------------------------------------------------------------------------"
echo "Do not press CTRL+C to close this window, as it will not stop the installation."
echo ""
echo "DISCLAIMER: This install script should work on any ubuntu machine and some other linux distros."
echo "However, there is no guarantee that it will work on all devices."
echo "As the owner of this software, I am not responsible for any damage caused by this software."
echo "If you do not agree to this disclaimer, please close this window and do not continue."
read -p "Please press any key if you agree to the disclaimer..." -n1 -s
echo ""

echo "--------------------------------------------------------------------------------"
echo ""
echo "This installer requires pipenv to be installed."
echo "Please install pipenv before continuing."
echo "To install pipenv please open another terminal and run the following command:"
echo "pip install pipenv"
echo ""
echo "If you already have pipenv installed, you can press any key to continue"
read -p "Press any key to continue..." -n1 -s
echo ""

echo "--------------------------------------------------------------------------------"
echo "Installing dependencies..."
pipenv install
echo "Installed dependencies!"
echo ""

echo "--------------------------------------------------------------------------------"
echo "Testing current code to prevent faulty builds..."
pipenv run pytest -v testing
echo "Testing complete!"

echo "--------------------------------------------------------------------------------"
echo "Building project..."
pipenv run pyinstaller --name Lyzer-Scraper --add-data backup/:data/ lyzer_scraper.py


echo "--------------------------------------------------------------------------------"
echo "Finalizing install..."
make package
echo "Cleaning..."
make clean
echo "Install Complete"
echo "--------------------------------------------------------------------------------"