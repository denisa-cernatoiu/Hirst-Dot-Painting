import colorgram

# Extracting 15 colors from an image.
colors_palette = colorgram.extract('hirst_painting.jpg', 30)
rgb_colors = []
for color in colors_palette:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

print(rgb_colors)