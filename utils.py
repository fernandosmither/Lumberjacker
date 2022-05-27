import time
import PIL.ImageGrab
import win32com.client as comclt
from ctypes import windll


def calibrate():
    print("A config.txt file doesn't exist, "
          "therefore we need to calibrate the coordinates.")
    print("Please move the mouse to the left side of the Lumberjack"
          "in the lowest point the branches reach.")
    for second in range(5, 0, -1):
        print(f"Capturing the left coordinates in {second}...")
        time.sleep(1)
    print("Left position:", left_position:=py.position())
    print("Please move the mouse to the right side of the Lumberjack")
    for second in range(5, 0, -1):
        print(f"Capturing the right coordinates in {second}...")
        time.sleep(1)
    print("Right position:", right_position:=py.position())
    with open("config.txt", "w") as file:
        file.write(f"LEFT_POSITION={left_position[0]},{left_position[1]}\n"
                    f"RIGHT_POSITION={right_position[0]},{right_position[1]}")


def move(key):
    if key == "Right":
        comclt.Dispatch("WScript.Shell").SendKeys("{RIGHT}")
    elif key == "Left":
        comclt.Dispatch("WScript.Shell").SendKeys("{LEFT}")


def get_pixel_colour(x, y):
    # return PIL.ImageGrab.grab().load()[i_x, i_y]
    dc = windll.user32.GetDC(0)
    return windll.gdi32.GetPixel(dc, x, y)
