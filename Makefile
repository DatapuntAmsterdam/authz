.PHONY: docs

test:
	AUTH_SKIP_CONF_CHECK=1 python setup.py test -a "-p no:cacheprovider tests"

coverage:
	AUTH_SKIP_CONF_CHECK=1 python setup.py test -a "-p no:cacheprovider --verbose --cov=authz --cov-report=term --cov-config .coveragerc tests"

pep8:
	# we make pep8 ignores the following rules
	# E501 line too long
	python setup.py test -a "-p no:cacheprovider --verbose --pep8 --ignore=E501 authorization"

docs:
	make -C docs/ html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
