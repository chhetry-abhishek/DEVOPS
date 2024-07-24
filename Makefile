.PHONY: clean test build

clean:
    rm -rf __pycache__

test:
    python -m unittest discover -s tests

build:
    python setup.py sdist