import arcade


WIDTH = 640
HEIGHT = 480

# x, y, radius
x = int(input("What is the x-value: "))
y = int(input("What is the y-value: "))
radius = int(input("What is the raidus: "))

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.BLUE_GREEN)

# End drawing
arcade.finish_render()
arcade.run()