# Angle Dangler

## TL;DR:

Download [bevel.svg](bevel.svg) or [lefty.svg](lefty.svg) and get busy lasering.

## What is all this?

This repository contains Python code that creates an SVG file for a bevel setting gauge.

A [sliding bevel](https://en.wikipedia.org/wiki/Sliding_T_bevel), T-bevel, or bevel gauge is used to transfer or lay out angles for woodworking and other applications. It is often useful to be able to set a bevel gauge to a specific, known angle as given on a set of plans. An angle dangler (bevel setting gauge) is used for that purpose.

## Using the included .svg files

### You don't need to download or run any code

I've included the svg files generated by the Python code in this repository. If you want to make use of them without modification, you can download any of the included .svg files. [bevel.svg](bevel.svg) and [lefty.svg](lefty.svg) will be the files most people will want to start with.

### Laser cutting

The only laser cutter I have tested this on is the one at the Makerspace I work out of. It's a GCC LaserPro Spirit, and they drive it with CorelDraw. If you're cutting with a similar setup, you may want to change the boundary line to a hairline in CorelDraw. I did. SVG doesn't have a hairline line width.

If you have to do any scaling, make sure you scale the same percentage in both x and y. If you don't, your angle dangler will come out with incorrect angles.

I don't have a recommended power setting for the cut or the marking. Play around, and don't burn your shop down.

### Now you have an angle dangler. What about a bevel gauge?

For new tools, the Shinwa offering is an excellent tool at a reasonable price. I doubt you can equal its quality without making a substantial step up in price to any of the specialist toolmakers. I don't have firsthand experience with any of their offerings.

I own a vintage Stanley 18 that I quite like except that the blade doesn't seem to be made out of spring steel and thus can be bent out of alignment with careless handling. I also own a vintage Stanley 25 that has a fine blade, but kind of a so-so handle. I don't love the locking mechanism on it either; the lever sometimes ends up in a position that interferes with laying the body against the edge of a workpiece. Nevertheless, I haven't sent it on its way. When I do, I'll probably step up to one of the specialist toolmakers.

### Left- and right-handed angle danglers

The right-handed danglers have the origin to the right of the gauge when 0 is held at the top. The left-handed danglers have the origin to the left of the gauge. If that doesn't make sense, view both of the files and the difference will become readily apparent.

## Using this code

### Python version

The Python code probably requires Python 3.

### Dependencies

The dependencies are specified in [requirements.txt](requirements.txt). Nothing is pinned to a specific version.

### Output

The script defaults to writing the svg file to stdout, but you may specify an output file as a positional argument if you'd like to. The height of the resulting angle dangler is printed to stderr as an aid to determining if you have a big enough piece of material on hand.

### Maximum angle

The maximum angle on the generated angle dangler can be specified with the`--max-theta=` argument. Absolutely no error checking is done on this value. Perhaps surprisingly, if you specify 90 degrees, you'll an svg file that is tall, but not infinitely tall. I don't know why, and I'm not going digging because it's an obviously stupid thing to do.

If you want to do it anyway, and your laser cutter is large enough to cut this, *and* you can find a big enough piece of material, please send a picture of the resulting angle dangler, taken from a satellite. A *practical* maximum is probably somewhere around 70 degrees. The script defaults to 50 degrees, which generates a dangler a little under 300mm/12" tall. 45 degrees will fit on a piece of A4 or US letter paper with some room to spare.

### Handedness

The default angle dangler is right-handed. `--lefty` will generate a left-handed one. I have no idea if this provides any ergonomic benefit to left-handed people.

### Linked stylesheet

The default angle dangler embeds its stylesheet. `--link-style` will generate one with a linked stylesheet instead. This is nerd stuff. You probably want an embedded stylesheet. If you want a linked one, you probably don't need me to explain why.

Browsers and CorelDraw seem to understand external stylesheets. Other svg renderers are a crapshoot.

## Commercial angle danglers

This project came about because I was browsing [Crucible Tool](https://lostartpress.com/collections/tools). Their angle dangler is laser cut, and it occurred to me that the makerspace I work out of has a laser cutter. For the record, I'd have come out ahead just buying one. If I were buying one today, I'd likely buy it from Crucible.

I've also used the iGaging offering in a class, and have found it to be completely satisfactory. I can't imagine how anybody could possibly screw this tool up.

## License

The code in this repository is licensed under the terms of [WTFPL](http://wtfpl.net). This code is of no commercial value to me. I build [furniture](https://longwalkwoodworking.com); I don't make tools to sell.

## Q/A

### Why not an FAQ?

I haven't gotten enough questions to order them by frequency.

### Angle dangler?

Bevel setting gauge doesn't exactly roll off the tongue, does it? All of the existing catchy names are somebody else's trademark. I give you angle dangler as a non-trademarked, generic term for a bevel setting gauge. It came to me in a dream. Take it or leave it.

### Why not just use a protractor?

On most protractors, the center of the arc isn't actually on the flat edge of the protractor. If you aren't convinced that that's a pain, buy a cheap one and see for yourself.

### Where do I get a laser cutter?

Assuming you aren't looking to buy a several thousand dollar tool to make a $40 tool, you have a couple of options:

Find a local makerspace or hackerspace (same thing). If they have a laser cutter they likely offer classes, or there might just be a friendly person who's happy to help you with a project. Or there might be somebody willing to make you one, possibly in exchange for help with their project or money.

Find a commercial laser cutting outfit and pay them to make it.

### What if there's a bug?

I'd be very surprised if there's only one.

If you find a bug, please open an issue and submit a pull request with a fix if you can. I reserve the right to close issues for bugs if there's no pull request and I can't be bothered to fix it myself.

### Will you add a feature?

I doubt it.

If it involves any sort of screwing around with pip, wheels, eggs, or anything else involved in distributing python code, absolutely not. Nor will I take a pull request. I have no desired to spend enough time getting familiar with pip, wheels, eggs, or whatever to review it intelligently.

### What kind of support is that?

The kind you get for zero dollars from a former programmer :-)

I build furniture. This code is good enough to enable me to do my job. Anything beyond that is my own professional courtesy as a recovering programmer.

### Are you really a Python programmer?

I gather you've looked at the code. I've primarily worked professionally writing C and Java. I've written Python as well, but a whole lot less of it.

### Why SVG as an output format?

Because it's a vector format CorelDraw understands and there was a Python module to generate it. Certainly not because I know it well.

### Are there any tests?

Nope. I'm assuming a great many people way smarter than I am are testing [numpy](https://numpy.org). Ditto [svgwrite](https://svgwrite.readthedocs.io/en/latest/svgwrite.html). If the output looks right, it probably is right. If it's not, it's almost certainly my fault, not numpy's or svgwrite's fault.

### Why are the generated files checked in to the repository?

So you don't have to run the python script if you just want to print or laser an angle dangler.

Also because there aren't any tests. If the generated files have changed, it's a reminder to make sure they still look right.

### Can you tell me how to make one of these with my laser cutter?

Nope. My knowledge of laser cutters extends only slightly beyond "Do not look into laser with remaining eye". It would be tantamout to malpractice for me to give you laser cutter advice.

### Can I use this in a commercial product?

Commercial use is governed by the terms of the [license](LICENSE).
