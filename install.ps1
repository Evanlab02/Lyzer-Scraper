echo "Requires python 3.10"
echo "Requires pip - On path"
echo "Requires pipenv - On path"
echo "Requires chrome-browser"
Read-Host -Prompt 'Press any key to continue...'

echo "--------------------------------------------------------------------------------"
echo "Do not press CTRL+C to close this window, as it will not stop the installation."
echo ""
echo "DISCLAIMER: This install script should work on any windows 10 machine."
echo "However, there is no guarantee that it will work on all devices."
echo "As the owner of this software, I am not responsible for any damage caused by this software."
echo "If you do not agree to this disclaimer, please close this window and do not continue."
Read-Host -Prompt 'Please press any key if you agree to the disclaimer...'

echo "--------------------------------------------------------------------------------"
echo ""
echo "This installer requires pipenv to be installed."
echo "Please install pipenv before continuing."
echo "To install pipenv please open another terminal and run the following command:"
echo "pip install pipenv"
echo ""
echo "If you already have pipenv installed, you can press any key to continue"
echo ""
Read-Host -Prompt 'Press any key to continue...'
echo ""
echo "--------------------------------------------------------------------------------"
echo "Installing dependencies..."
pipenv install
echo "Installed dependencies!"
echo ""

echo "--------------------------------------------------------------------------------"
echo "Testing current code to prevent faulty builds..."
pipenv run pytest -v testing --cov
echo "Testing complete!"
echo ""

echo "--------------------------------------------------------------------------------"
echo "Building project..."
pipenv run pyinstaller --name Lyzer-Scraper --add-data "backup/;data/" lyzer_scraper.py 
echo ""

echo "--------------------------------------------------------------------------------"
echo "Finalizing install..."
Compress-Archive -Path 'dist/Lyzer-Scraper/'-DestinationPath 'dist/Lyzer-Scraper/Lyzer-Scraper.zip'
rm -fo release/Windows_10/*.*
rm -fo release/Windows_10/
mkdir release/Windows_10/
cp dist/Lyzer-Scraper/Lyzer-Scraper.zip release/Windows_10/

echo "Cleaning Up..."
pipenv clean
rm -fo .coverage
echo "Press enter for all the following prompts to delete the build, dist and cache folders"
echo "It is recommended to delete these folders to prevent any issues with future builds and installations"
rm -fo build/*.*
rm -fo build/
rm -fo dist/*.*
rm -fo dist/
rm -fo Lyzer-Scraper.spec
rm -fo .pytest_cache/*.*
rm -fo .pytest_cache/
rm -fo data/*.*
echo "Install Complete"
echo "--------------------------------------------------------------------------------"