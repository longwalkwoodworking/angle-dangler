BEVEL_GAUGES := bevel.svg lefty.svg
all: $(BEVEL_GAUGES)

bevel.svg: bevel.py Makefile
	python3 $< >$@

lefty.svg: bevel.py Makefile
	python3 $< --lefty $@

.PHONY: clean
clean:
	-rm $(BEVEL_GAUGES)
