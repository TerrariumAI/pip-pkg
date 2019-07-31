build-pkg:
	python setup.py bdist_wheel

upload-pkg:
	python -m twine upload dist/*