.PHONY: test coverage docs release

test:
	python setup.py test -a "-p no:cacheprovider tests"

release:
	python setup.py sdist upload
	
	