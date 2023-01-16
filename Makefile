all:
	@make install
	@make test
	@make build
install:
	@pipenv install
test:
	@pipenv run pytest testing --cov
build:
	@pipenv run pyinstaller lyzer_scraper.py --name Lyzer-Scraper --add-data backup/:data/
build-windows:
	@pipenv run pyinstaller lyzer_scraper.py --name Lyzer-Scraper -i images/Lyzer-Scraper.PNG --add-data backup/;data/
clean:
	@pipenv clean
	@rm -rf .coverage
	@rm -rf build/
	@rm -rf dist/
	@rm -rf Lyzer-Scraper.spec
	@rm -rf .pytest_cache
	@rm -rf data/
refresh:
	@pipenv sync
run:
	@pipenv run python3 lyzer_scraper.py
run-ubuntu: build
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper
run-windows: build-windows
	@cd dist/Lyzer-Scraper/ && ./Lyzer-Scraper.exe
update:
	@pipenv update
	@pipenv requirements > requirements.txt
security-check:
	@pipenv check