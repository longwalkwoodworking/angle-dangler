BEVEL_GAUGES := bevel.svg lefty.svg bevel-linked.svg lefty-linked.svg
all: $(BEVEL_GAUGES)

$(filter %linked.svg,$(BEVEL_GAUGES)) : SCRIPT_ARGS += --link-style
$(filter lefty%,$(BEVEL_GAUGES)) : SCRIPT_ARGS += --lefty

$(BEVEL_GAUGES): %: bevel.py Makefile style.css
	python3 $< $(SCRIPT_ARGS) $@

.PHONY: clean
clean:
	-rm $(BEVEL_GAUGES)
