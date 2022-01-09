from numpy import radians
from numpy import tan

from svgwrite import drawing
from svgwrite import mm

G_WIDTH = 80
G_Y_OFFSET = 12
G_ORIGIN = 150
G_HALF_ANG_WIDTH = 12
G_MAX_THETA = 35

def ang_line(d, theta, x1=0, x2=G_WIDTH):
    y1=(G_Y_OFFSET + (G_ORIGIN + G_WIDTH - x1) * tan(radians(theta)))
    y2=(G_Y_OFFSET + (G_ORIGIN + G_WIDTH - x2) * tan(radians(theta)))

    x1 *= mm
    y1 *= mm
    x2 *= mm
    y2 *=mm

    d.add(d.line((x1, y1), (x2, y2), **{"class": "l"}))

def label(d, theta):
    x1=37*mm
    y1=(2 + G_Y_OFFSET + (G_ORIGIN + 40) * tan(radians(theta))) * mm
    d.add(d.text(str(theta), (x1, y1), **{"class": "label"}))

def main ():
    height = 2 * G_Y_OFFSET + (G_ORIGIN + G_WIDTH) * tan(radians(G_MAX_THETA))
    print(height)
    d = drawing.Drawing("bevel.svg", (G_WIDTH*mm, height*mm))
    d.add_stylesheet("./style.css", "asdf")
    d.add(d.rect((0*mm, 0*mm), (G_WIDTH*mm, height*mm), **{"class": "boundary"}))

    # 5 degree lines
    for theta in range(0, G_MAX_THETA + 1, 5):
        ang_line(d, theta, 0, 35)
        ang_line(d, theta, 44)

    # 5 degree labels in the gaps left in the 5 degree lines
    for theta in range(0, G_MAX_THETA + 1, 5):
        label(d, theta)

    # Whole degree lines, except for the 5 degree lines
    for theta in range(0, G_MAX_THETA + 1):
        if (theta % 5 == 0):
            continue
        ang_line(d, theta)

    # half-degree ticks
    for theta in range(0, G_MAX_THETA, 1):
        ang_line(d, theta + .5, 0, G_HALF_ANG_WIDTH)
        ang_line(d, theta + .5, G_WIDTH - G_HALF_ANG_WIDTH)
    d.save(pretty=True)

if __name__ == "__main__":
    main()
