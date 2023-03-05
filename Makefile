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

install:
	@pipenv install

refresh:
	@pipenv sync

update:
	@pipenv update
	@pipenv requirements > requirements.txt
	@rm -rf backup/
	@mkdir backup/
	@cp -r dist/Lyzer-Scraper/data/. backup/ 

test:
	@echo "<TEST> Running Tests"
	@pipenv run pytest -v testing --cov
	@echo "<TEST> Tests Complete"

build:
	@pipenv run pyinstaller --name Lyzer-Scraper --add-data backup/:data/ lyzer_scraper.py

run:
	@pipenv run python3 lyzer_scraper.py

run-bin: build
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper

run-bin-backlog: build
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper --clear-backlog

run-bin-update: build
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper --update

build-windows:
	@pipenv run pyinstaller --name Lyzer-Scraper --add-data "backup/;data/" lyzer_scraper.py 
