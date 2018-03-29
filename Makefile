SOURCES=amadeus specs setup.py
DOC_SOURCES=amadeus docs README.rst

test:
		  mamba --format=documentation --enable-coverage

coverage:
			coverage html
			open htmlcov/index.html

watch:
			make run
			make coverage
			fswatch -o ${SOURCES} | xargs -n1 -I{} make run

run:
			make lint
			make test
			coverage html

lint:
			flake8 $(SOURCES) --exit-zero

docs:
			rm -rf _docs
			sphinx-build -b html docs _docs

watchdocs:
			make docs
			open _docs/index.html
			fswatch -o ${DOC_SOURCES} | xargs -n1 -I{} make docs

.PHONY: test coverage watch run lint docs
