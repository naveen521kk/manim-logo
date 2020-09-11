import cairo

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 300, 200)
#surface = cairo.SVGSurface(cairo.FORMAT_RGB24, 300, 200)
ctx = cairo.Context(surface)

ctx.rectangle(25, 50, 50, 120)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()
ctx.rectangle(125, 50, 50, 120)
ctx.set_source_rgb(0, 1, 1)
ctx.set_line_width(4)
ctx.stroke()
ctx.rectangle(225, 50, 50, 120)
ctx.set_source_rgb(0, 0, 1)
ctx.fill_preserve()
ctx.set_source_rgb(1, 1, 0)
ctx.set_line_width(4)
ctx.stroke()
surface.write_to_png('rectangle.png')
import os
os.startfile('rectangle.png')
