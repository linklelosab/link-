from graphics import *
import sys

# Function for flood fill
def flood_fill(x, y, fill_color, default_color, win):
    # Get the color of the pixel at (x, y)
    #current_color = win.getPixel(x, y)
    current_color = win.plot(x, y)

    # Check if the pixel is of the default color
    if current_color == default_color:
        win.getPixel(x, y, fill_color)

        # Recursively fill neighboring pixels
        flood_fill(x + 1, y, fill_color, default_color, win)
        flood_fill(x - 1, y, fill_color, default_color, win)
        flood_fill(x, y + 1, fill_color, default_color, win)
        flood_fill(x, y - 1, fill_color, default_color, win)

def main():
    # Create a graphical window
    win = GraphWin("Flood Fill Example", 400, 400)
    win.setBackground("white")

    # Draw a rectangle (border only)
    rect = Rectangle(Point(50, 50), Point(250, 250))
    rect.setWidth(2)  # Set the width of the rectangle's border
    rect.setOutline("black")
    rect.draw(win)

    # Starting point for the flood fill
    start_x, start_y = 55, 55
    
    # Get the color of the pixel at the start point (this will be the default color to flood)
    #default_color = win.getPixel(start_x, start_y)
    default_color=win.plotPixel(start_x, start_y)
    
    # Perform the flood fill
    flood_fill(start_x, start_y, "yellow", default_color, win)

    # Wait for a mouse click before closing
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()
