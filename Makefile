security-check:
	@pipenv check
clean:
	@pipenv clean
	@rm -r build/
	@rm -r dist/
	@rm Lyzer-Scraper.spec
run:
	@pipenv run python3 Lyzer-Scraper.py
install:
	@pipenv install
	@pipenv sync
update-dependencies:
	@pipenv update
update-requirements:
	@pipenv requirements > requirements.txt
test:
	@python -m unittest discover -s testing/ -p "test_*.py"
coverage:
	@coverage run -m unittest discover -s testing/ -p "test_*.py"
	@coverage report