echo "Requires python 3.10"
echo "Requires pip - On path"
echo "Requires pipenv - On path"
echo "Requires chrome-browser"
echo "Requires Make"
echo "--------------------------------------------------------------------------------"
echo ""
echo "This installer requires pipenv to be installed."
echo "Please install pipenv before continuing."
echo "To install pipenv please open another terminal and run the following command:"
echo "pip install pipenv"
echo ""
echo "If you already have pipenv installed, you can press any key to continue"
echo "--------------------------------------------------------------------------------"
read -p "Press any key to continue..." -n1 -s
echo ""
echo "--------------------------------------------------------------------------------"
echo "Installing dependencies..."
pipenv install
echo "Installed dependencies!"
echo "--------------------------------------------------------------------------------"

echo "--------------------------------------------------------------------------------"
echo "Testing current code to prevent faulty builds..."
pipenv run pytest -v testing
echo "Testing complete!"
echo "--------------------------------------------------------------------------------"

echo "--------------------------------------------------------------------------------"
echo "Building project..."
pipenv run pyinstaller --name Lyzer-Scraper --add-data backup/:data/ lyzer_scraper.py
echo "--------------------------------------------------------------------------------"


echo "--------------------------------------------------------------------------------"
echo "Finalizing install..."
make package
echo "Cleaning..."
make clean
echo "Install Complete"
echo "--------------------------------------------------------------------------------"