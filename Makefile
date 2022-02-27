BEVEL_GAUGES := bevel.svg lefty.svg bevel-embed.svg lefty-embed.svg
all: $(BEVEL_GAUGES)

$(filter %embed.svg,$(BEVEL_GAUGES)) : SCRIPT_ARGS += --embed-style
$(filter lefty%,$(BEVEL_GAUGES)) : SCRIPT_ARGS += --lefty

$(BEVEL_GAUGES): %: bevel.py Makefile style.css
	python3 $< $(SCRIPT_ARGS) $@

.PHONY: clean
clean:
	-rm $(BEVEL_GAUGES)
