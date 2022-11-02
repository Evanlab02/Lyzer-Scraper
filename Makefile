security-check:
	@pipenv check
clean:
	@pipenv clean
install:
	@pipenv install
	@pipenv sync
update-dependencies:
	@pipenv update
update-requirements:
	@pipenv requirements > requirements.txt