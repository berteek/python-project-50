.PHONY: gendiff, coverage

lint:
	poetry run flake8 gendiff

install:
	poetry install 

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest -v

test-cov:
	poetry run pytest --cov=gendiff tests/

test-json:
	poetry run gendiff ./tests/fixtures/json/file1.json ./tests/fixtures/json/file2.json

test-reporter-before-build:
	./test-reporter-latest-linux-amd64 before-build

test-reporter-format-coverage:
	./test-reporter-latest-linux-amd64 format-coverage coverage.xml -t coverage.py

test-reporter-sum-coverage:
	./test-reporter-latest-linux-amd64 sum-coverage

test-reporter-upload-coverage:
	./test-reporter-latest-linux-amd64 upload-coverage

coverage:
	poetry run coverage run -m pytest | poetry run coverage xml
