REMOVE = rm -rvf

all:
	check-manifest
	python setup.py sdist bdist_wheel
clean:
	$(REMOVE) .pytest_cache
	$(REMOVE) build
	$(REMOVE) logs
	$(REMOVE) dist
	$(REMOVE) puts.egg-info
	$(REMOVE) ./**/__pycache__
publish:
	python -m twine upload dist/*