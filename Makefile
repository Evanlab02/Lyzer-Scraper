clean:
	@echo "<CLEAN> Unused Dependencies"
	@pipenv clean
	@echo "<CLEAN> Coverage File"
	@rm -rf .coverage
	@echo "<CLEAN> Build Folder"
	@rm -rf build/
	@echo "<CLEAN> Dist Folder"
	@rm -rf dist/
	@echo "<CLEAN> Spec File"
	@rm -rf Lyzer-Scraper.spec
	@echo "<CLEAN> Pytest Cache"
	@rm -rf .pytest_cache
	@echo "<CLEAN> Data Folder"
	@rm -rf data/
	@rm -rf release/CURRENT/

install:
	@pipenv install

refresh:
	@pipenv sync

update:
	@pipenv update
	@pipenv requirements > requirements.txt

test:
	@echo "<TEST> Running Tests"
	@pipenv run pytest -v testing --cov
	@echo "<TEST> Tests Complete"

build:
	@pipenv run pyinstaller --name Lyzer-Scraper --add-data backup/:data/ lyzer_scraper.py

build-windows:
	@pipenv run pyinstaller --name Lyzer-Scraper --add-data "backup/;data/" lyzer_scraper.py 

backup: build
	@rm -rf backup/
	@mkdir backup/
	@cp -r dist/Lyzer-Scraper/data/. backup/ 

run:
	@clear
	@pipenv run python3 lyzer_scraper.py

run-bin: build
	@clear
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper

run-bin-backlog: build
	@clear
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper --clear-backlog

run-bin-update: build
	@clear
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper --update

package:
	@echo "<PACKAGE> Creating Package"
	@cd dist/Lyzer-Scraper/ && zip -r Lyzer-Scraper.zip .
	@rm -rf release/CURRENT
	@mkdir release/CURRENT
	@cp -r dist/Lyzer-Scraper/Lyzer-Scraper.zip release/CURRENT/
	@echo "<PACKAGE> Package Complete"

package-ubuntu-lts: build
	@echo "<PACKAGE> Creating Package"
	@cd dist/Lyzer-Scraper/ && zip -r Lyzer-Scraper.zip .
	@rm -rf release/Ubuntu-22.04
	@mkdir release/Ubuntu-22.04
	@mv dist/Lyzer-Scraper/Lyzer-Scraper.zip release/Ubuntu-22.04/Ubuntu-22.04-Lyzer-Scraper.zip
	@echo "<PACKAGE> Package Complete"
