install:
	@pipenv install
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
test:
	@echo "<TEST> Running Tests"
	@pipenv run pytest testing --cov
	@echo "<TEST> Tests Complete"
build:
	@pipenv run pyinstaller --name Lyzer-Scraper --add-data backup/:data/ lyzer_scraper.py
run:
	@pipenv run python3 lyzer_scraper.py
run-ubuntu: build
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper
refresh:
	@pipenv sync
update:
	@pipenv update
	@pipenv requirements > requirements.txt
security-check:
	@pipenv check
pipeline:
	pip install --upgrade pip
	pip install pipenv
	make install
	make test
	make build