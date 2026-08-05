PYTHON ?= python3
LATEX ?= lualatex

.PHONY: all data generate pdf clean validate

all: pdf

data:
	$(PYTHON) scripts/fetch_dhatupatha.py

generate: data
	$(PYTHON) scripts/generate.py

validate: generate
	$(PYTHON) scripts/validate.py

pdf: validate
	mkdir -p build
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=build main.tex
	$(LATEX) -interaction=nonstopmode -halt-on-error -output-directory=build main.tex

clean:
	rm -rf build/*
