#In cm
import cairo
width=WIDTH = height=HEIGHT = 5
PIXEL_SCALE = 100 #400 px width and height

#width, height = width_in_points, height_in_points
with cairo.SVGSurface("back_ground.svg",  WIDTH*PIXEL_SCALE,HEIGHT*PIXEL_SCALE) as surface:
    ctx = cairo.Context(surface)
    ctx.scale(PIXEL_SCALE,PIXEL_SCALE) #scaling
    #setting backgound
    ctx.rectangle(0, 0, WIDTH, HEIGHT)
    ctx.set_source_rgb(0.9, 0.8, 0.9)
    ctx.fill()
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
    surface.write_to_png('back_ground.png')
import os
os.startfile("back_ground.svg")
