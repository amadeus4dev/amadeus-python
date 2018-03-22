SOURCES=amadeus specs setup.py

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

lint:
			flake8 $(SOURCES) --exit-zero

.PHONY: test coverage watch run lint
