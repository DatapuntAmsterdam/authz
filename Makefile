.PHONY: test coverage docs release

test:
	python setup.py test -a "-p no:cacheprovider tests"

coverage:
	python setup.py test -a "-p no:cacheprovider --verbose --cov=authorization --cov-report=term --cov-config .coveragerc tests"

docs:
	make -C docs/ html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"

release:
	python setup.py sdist upload
	
	