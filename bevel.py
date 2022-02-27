from argparse import ArgumentParser

from numpy import radians
from numpy import tan

from svgwrite import drawing
from svgwrite import mm

import sys

G_WIDTH = 80
G_Y_OFFSET = 12
G_ORIGIN = 150
G_HALF_ANG_WIDTH = 12
G_STYLESHEET = './style.css'

# Calculate the y-coordinate of a line given the x coordinate and the angle
# theta for a bevel gauge with the origin on the right side (righty) and left
# side (lefty) of the gauge.
def righty(x, theta):
    return (G_Y_OFFSET + (G_ORIGIN + G_WIDTH - x) * tan(radians(theta)))

def lefty(x, theta):
    return (G_Y_OFFSET + (G_ORIGIN + x) * tan(radians(theta)))

def ang_line(d, theta, x1=0, x2=G_WIDTH, y_func=righty):
    y1=y_func(x1, theta)
    y2=y_func(x2, theta)

    x1 *= mm
    y1 *= mm
    x2 *= mm
    y2 *= mm

    d.add(d.line((x1, y1), (x2, y2), **{"class": "l"}))

# Fortunately, the labels land in the same place whether it's a lefty or a
# righty bevel gauge :-)
def label(d, theta):
    # Pay no mind to the magic numbers...
    x1=37*mm
    y1=(2 + G_Y_OFFSET + (G_ORIGIN + G_WIDTH / 2) * tan(radians(theta))) * mm
    d.add(d.text(str(theta), (x1, y1), **{"class": "label"}))

def main ():
    parser = ArgumentParser()
    parser.add_argument('--lefty', dest='y_func', action='store_const',
            const=lefty, default=righty)
    parser.add_argument('--link-style', action='store_true')
    parser.add_argument('--max-theta', action='store', default=50, type=int)
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()

    y_func = args.y_func
    max_theta = args.max_theta
    link_style = args.link_style
    filename = args.filename
    
    # Height is the same regardless of handedness.
    # Equivalently, G_Y_OFFSET + lefty(G_WIDTH, max_theta) would work.
    # Useful info if you need to buy some material or figure out if your scrap
    # is big enough.
    # Print to stderr if no filename is specified so stdout can be redirected
    # to a file without crapping up the file with this info.
    height =  G_Y_OFFSET + righty(0, max_theta)
    print("Document height = " + str(height), file=sys.stderr)

    d = drawing.Drawing(filename, (G_WIDTH*mm, height*mm))

    # External stylesheet support is sort of iffy. Browsers seem to be OK with
    # it, CorelDraw seems to be OK with it, other renderers not so much.
    if link_style:
        d.add_stylesheet(G_STYLESHEET, "asdf")
    else:
        with open(G_STYLESHEET, 'r') as style:
            d.embed_stylesheet(style.read())

    # SVG doesn't have a hairline width to define the boundary. Depending on
    # your personal laser cutter, you may need to do something in whatever
    # software you're driving yours with to get a vector cut.
    d.add(d.rect((0*mm, 0*mm), (G_WIDTH*mm, height*mm),
        **{"class": "boundary"}))

    # 5 degree lines
    for theta in range(0, max_theta + 1, 5):
        ang_line(d, theta, 0, 35, y_func=y_func)
        ang_line(d, theta, 44, y_func=y_func)

    # 5 degree labels in the gaps left in the 5 degree lines
    for theta in range(0, max_theta + 1, 5):
        label(d, theta)

    # Whole degree lines, except for the 5 degree lines
    for theta in range(0, max_theta + 1):
        if (theta % 5 == 0):
            continue
        ang_line(d, theta, y_func=y_func)

    # half-degree ticks
    for theta in range(0, max_theta, 1):
        ang_line(d, theta + .5, 0, G_HALF_ANG_WIDTH, y_func=y_func)
        ang_line(d, theta + .5, G_WIDTH - G_HALF_ANG_WIDTH, y_func=y_func)

    if filename is not None:
        with open(filename, 'w', encoding='utf-8') as output:
            d.write(output, pretty=True)
    else:
        d.write(sys.stdout, pretty=True)

if __name__ == "__main__":
    main()
