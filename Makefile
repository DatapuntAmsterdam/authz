.PHONY: test coverage docs release

test:
	python setup.py test -a "-p no:cacheprovider tests"

coverage:
	python setup.py test -a "-p no:cacheprovider --verbose --cov=authorization --cov-report=term --cov-config .coveragerc tests"

release:
	python setup.py sdist upload
	
	