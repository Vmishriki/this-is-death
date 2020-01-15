print("Hello World!")
import math
wall_height = int(input("Enter wall height (feet):"))
print()
wall_width = int(input("Enter wall width (feet):"))
print()
wall_area = (wall_height * wall_width)
print("Wall area:" ,wall_area, "square feet")
gallon_of_paint = float(wall_area / 350)
print("Paint needed: %f"% gallon_of_paint, "gallons")
cans_needed = round(gallon_of_paint)
print("Cans needed:" , cans_needed , "can(s)\n")

paint_colors = {'red':15,'blue':18,'green':22}

color_chosen = input("Choose a color to paint the wall:\n")
price = paint_colors[color_chosen] * cans_needed
print("Cost of purchasing %s paint: $%d" % (color_chosen,price)) #recieved help from my TA for this line
scaffold = 30
fall_protection = 20
dropcloth = 2*wall_width
spray_gun = 50
total_cost = 0
if wall_height > 20:
    total_cost = int(price + scaffold)
    print("Scaffold rental needed at $30. Total cost: $%d" % total_cost)
if wall_height > 30:
    total_cost = int(total_cost + fall_protection)
    print("Fall protection needed at $20. Total cost: $%d" % total_cost)
if wall_height > 30 and wall_area > 500:
    total_cost = int(total_cost + spray_gun)
    print("Spray gun needed at $50. Total cost: $%d" % total_cost)
elif wall_height < 20:
    total_cost = int(price + dropcloth)
    print("Drop cloth needed at $2 per foot. Total cost: $%d" % total_cost)
