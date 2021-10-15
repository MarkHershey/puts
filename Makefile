REMOVE = rm -rvf

all:
	check-manifest
	python setup.py sdist bdist_wheel
clean:
	$(REMOVE) dist
	$(REMOVE) build
	$(REMOVE) puts.egg-info
	$(REMOVE) logs
	$(REMOVE) ./**/logs
	$(REMOVE) .pytest_cache
	$(REMOVE) ./**/__pycache__
publish:
	python -m twine upload dist/*