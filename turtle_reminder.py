import turtle as t
import sys
from datetime import date

def display_turtle_banner(reminder_text):
    """
    Displays a yellow-filled rectangle with bold green text in the center
    using the turtle graphics module.
    """
    if not reminder_text:
        reminder_text = "REMINDER: No text provided!"

    screen = t.Screen()
    screen.setup(width=600, height=300) # Adjust window size as needed
    screen.title(f"Reminder! - {date.today().strftime('%d-%b-%Y')}")
    screen.bgcolor("lightgray") # Background color of the window itself

    pen = t.Turtle()
    pen.speed(0) # Fastest speed for drawing
    pen.hideturtle() # Hide the turtle icon

    # 1. Draw the yellow-filled rectangle
    rect_width = 400
    rect_height = 150

    pen.penup()
    # Move to the starting position for the rectangle (center - half_width, center - half_height)
    pen.goto(-rect_width / 2, -rect_height / 2)
    pen.pendown()

    pen.fillcolor("yellow")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(rect_width)
        pen.left(90)
        pen.forward(rect_height)
        pen.left(90)
    pen.end_fill()

    # 2. Write the bold green text in the center
    pen.penup()
    pen.goto(0, -10) # Center for text (slight Y offset for visual balance)
    pen.color("green") # Text color

    # Font properties: Big, bold font
    # You might need to experiment with font size for optimal display on your system
    font_size = 24
    font_style = ("Arial", font_size, "bold")
    
    # Write the text
    pen.write(reminder_text, align="center", font=font_style)

    # Keep the window open until manually closed
    screen.mainloop()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        reminder_message = "No text provided. Default Reminder!"
    else:
        reminder_message = " ".join(sys.argv[1:])

    display_turtle_banner(reminder_message)

