all: bevel.svg lefty.svg

.PHONY: righty
right: bevel.svg

bevel.svg: bevel.py Makefile
	python3 $< >$@

.PHONY: lefty
lefty: lefty.svg

lefty.svg: bevel.py Makefile
	python3 $< --lefty $@

.PHONY: clean
clean:
	git clean -dfx
