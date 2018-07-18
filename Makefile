test:
	pytest -v

ship:
	python setup.py sdist bdist_wheel
	twine upload dist/* --skip-existing

dev:
	gulp --cwd oembeder/staticapp/

database:
	dropdb oembeder --if-exists
	createdb oembeder
