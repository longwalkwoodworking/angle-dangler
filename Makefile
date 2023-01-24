# Copyright © 2022 Eric Diven

# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://www.wtfpl.net/ for more details. */

BEVEL_GAUGES := bevel.svg lefty.svg bevel-linked.svg lefty-linked.svg scott.svg
all: $(BEVEL_GAUGES)

$(filter %linked.svg,$(BEVEL_GAUGES)) : SCRIPT_ARGS += --link-style
$(filter lefty%,$(BEVEL_GAUGES)) : SCRIPT_ARGS += --lefty
scott.svg : SCRIPT_ARGS += --bassackwards --max-theta=65

$(BEVEL_GAUGES): %: bevel.py Makefile style.css
	python3 $< $(SCRIPT_ARGS) $@

.PHONY: clean
clean:
	-rm $(BEVEL_GAUGES)
