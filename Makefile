requirements:
	@pipenv requirements > requirements.txt
install:
	@pipenv install
	@pipenv sync
update:
	@pipenv update
	@pipenv requirements > requirements.txt
build:
	@pipenv run pyinstaller lyzer_scraper.py --name Lyzer-Scraper -i images/Lyzer-Scraper.PNG
clean:
	@pipenv clean
	@rm -rf .coverage
	@rm -rf build/
	@rm -rf dist/
	@rm -rf lyzer_scraper.spec
	@rm -rf .pytest_cache
coverage:
	@pipenv run coverage run -m unittest discover -s testing/ -p "test_*.py"
	@pipenv run coverage report
run:
	@pipenv run python3 lyzer_scraper.py
security-check:
	@pipenv check
test:
	@pipenv run pytest testing --cov
ubuntu-install: build
	@chmod +x dist/lyzer_scraper
	@sudo cp dist/lyzer_scraper /usr/local/bin/