security-check:
	@pipenv check
clean:
	@pipenv clean
	@rm -r .coverage
	@rm -r build/
	@rm -r dist/
	@rm lyzer_scraper.spec
run:
	@pipenv run python3 lyzer_scraper.py
install:
	@pipenv install
	@pipenv sync
update-dependencies:
	@pipenv update
update-requirements:
	@pipenv requirements > requirements.txt
test:
	@pipenv run pytest testing
coverage:
	@pipenv run coverage run -m unittest discover -s testing/ -p "test_*.py"
	@pipenv run coverage report
build:
	@pipenv run pyinstaller --onefile lyzer_scraper.py