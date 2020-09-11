import cairo
from math import pi
def arc(xc,yc,buff):
    cr = cairo.Context(surface)
    cr.scale(PIXEL_SCALE,PIXEL_SCALE)
    cr.set_line_width(0.07)
    radius = -1
    angle1 = 90.0 * (pi / 180.0)  # angles are specified
    angle2 = 360.0 * (pi / 180.0)  # in radians
    cr.set_line_width(0.03)
    cr.arc(0.5, 0, radius, angle1, angle1)
    cr.line_to(buff, yc)
    #cr.arc(xc, yc, radius, angle2, angle2)
    #cr.line_to(xc, yc)
    cr.stroke()
def pent(buff):
    cr=cairo.Context(surface)
    cr.scale(PIXEL_SCALE,PIXEL_SCALE)
    cr.set_line_width(0.009)
    angle1 = 90.0 * (pi / 180.0) 
    cr.arc(0, 0, width, angle1, angle1)
    cr.line_to(buff, buff+(1/4))
    #cr.close_path()
    cr.set_source_rgb(0.5, 0.5, 1)
    cr.stroke()
def rect(x0,y0):
    cr = cairo.Context(surface)
    cr.scale(PIXEL_SCALE, PIXEL_SCALE)
    cr.set_line_width(((1/4)/4))
    #cairo.SolidPattern(0.1,0,0.5)
    # a custom shape, that could be wrapped in a function
    #x0 = 0.05  # parameters like cairo_rectangle
    #y0 = 0.05
    rect_width = (1/4)
    rect_height = (1/4)
    radius = (1/4)/2  # and an approximate curvature radius

    x1 = x0 + rect_width
    y1 = y0 + rect_height

    if rect_width / 2 < radius:
        if rect_height / 2 < radius:
            cr.move_to(x0, (y0 + y1) / 2)
            cr.curve_to(x0, y0, x0, y0, (x0 + x1) / 2, y0)
            cr.curve_to(x1, y0, x1, y0, x1, (y0 + y1) / 2)
            cr.curve_to(x1, y1, x1, y1, (x1 + x0) / 2, y1)
            cr.curve_to(x0, y1, x0, y1, x0, (y0 + y1) / 2)
        else:
            cr.move_to(x0, y0 + radius)
            cr.curve_to(x0, y0, x0, y0, (x0 + x1) / 2, y0)
            cr.curve_to(x1, y0, x1, y0, x1, y0 + radius)
            cr.line_to(x1, y1 - radius)
            cr.curve_to(x1, y1, x1, y1, (x1 + x0) / 2, y1)
            cr.curve_to(x0, y1, x0, y1, x0, y1 - radius)
    else:
        if rect_height / 2 < radius:
            cr.move_to(x0, (y0 + y1) / 2)
            cr.curve_to(x0, y0, x0, y0, x0 + radius, y0)
            cr.line_to(x1 - radius, y0)
            cr.curve_to(x1, y0, x1, y0, x1, (y0 + y1) / 2)
            cr.curve_to(x1, y1, x1, y1, x1 - radius, y1)
            cr.line_to(x0 + radius, y1)
            cr.curve_to(x0, y1, x0, y1, x0, (y0 + y1) / 2)
        else:
            cr.move_to(x0, y0 + radius)
            cr.curve_to(x0, y0, x0, y0, x0 + radius, y0)
            cr.line_to(x1 - radius, y0)
            cr.curve_to(x1, y0, x1, y0, x1, y0 + radius)
            cr.line_to(x1, y1 - radius)
            cr.curve_to(x1, y1, x1, y1, x1 - radius, y1)
            cr.line_to(x0 + radius, y1)
            cr.curve_to(x0, y1, x0, y1, x0, y1 - radius)

    cr.close_path()
    cr.set_source_rgb(0.5, 0.5, 1)
    cr.fill_preserve()
    cr.set_source_rgba(0.5, 0.5, 0, 0.5)
    cr.stroke()
#In cm
width=WIDTH = height=HEIGHT = 5
PIXEL_SCALE = 100 #400 px width and height

#width, height = width_in_points, height_in_points
with cairo.SVGSurface("logo.svg",  WIDTH*PIXEL_SCALE,HEIGHT*PIXEL_SCALE) as surface:
    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE,PIXEL_SCALE) #scaling
    #setting backgound
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0.9, 0.8, 0.9)
    ctx.fill()
    #making a M
    #ctx.set_line_width(1)
    ctx.move_to(0, 2.5)
    ctx.line_to(2.5, 0)
    ctx.line_to(2.5, 2.5)
    ctx.close_path()
    ctx.set_source_rgb(0.5, 0.5, 0.7)
    ctx.fill()
    ctx.move_to(2.5, 2.5)
    ctx.line_to(5, 2.5)
    ctx.line_to(2.5, 5)
    ctx.fill_preserve()
    ctx.set_source_rgb(0.5, 0.5, 0.7) #color
    #ctx.set_line_width(0.1)
    #ctx.stroke()
    surface.write_to_png('log_png.png')
import os
os.startfile("logo.svg")

