import pygame as py

def draw_circle() -> None:
    size = (300,400)
    screen = py.display.set_mode(size)
    radius = 20
    width = 5
    print("press any key to stop...")

    while True:
        for ev in py.event.get():
            if ev.type == py.MOUSEBUTTONUP:
                pos = py.mouse.get_pos()
                col = (0,255,255)

                py.draw.circle(screen,col,pos,radius,width)
                py.display.update()

            elif ev.type == py.KEYUP:
                return

if __name__ == "__main__":
    draw_circle()

