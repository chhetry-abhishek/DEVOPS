.PHONY: clean test build

clean:
	if exist __pycache__ (rmdir /s /q __pycache__)

test:
	python -m unittest discover -s tests

build:
	python setup.py sdist
package:
	python setup.py bdist
