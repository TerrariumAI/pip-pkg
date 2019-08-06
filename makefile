build-pkg:
	python setup.py bdist_wheel

upload-pkg:
	python -m twine upload dist/terrariumai-${VERSION}-py3-none-any.whl