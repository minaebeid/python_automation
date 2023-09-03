
from PIL import Image, ImageOps
import pyautogui
import os
import mss
import time
import numpy as np


# ##################################################################################################
# OVERVIEW
# ##################################################################################################
# HOW TO USE:
# - open Chrome
# - open Chrome dinoasur game by disconnecting computer from the internet
# - run this Python script with command "python3 t_rex.py"
# - if the script complains about missing packages then install them using pip3
#
# LOGIC:
# - python takes the screenshot and saves the image to "screen.png" as fast as it can
# - then the script opens that image for analysis
# - if the section of the image in front of t-rex contains obstacles then script hits space bar
# - this causes t-rex to jump
# - this section is basically just a little square in front of the dinosaur
# - you can think of it as his very simple eye
# - obstacle detection works by calculating how dark or light the section in front of t-rex really is
# - this is done by taking color values of all the pixels in the section and taking an average value
# - completely white pixels have values of 255 and completely dark pixels have values of 0
# ##################################################################################################


def press_space():
    # this simulates keypress (pressing key down and moving finger back up)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')


def restart_game():
    pyautogui.click((960, 230))  # click somewhere on the browser to put it in focus
    press_space()  # start the game


def jump():
    print('JUMP')
    press_space()


def update_saved_screen():
    with mss.mss() as sct:
        sct.shot(output='screen.png')  # taking a screenshot and saving it to an image file


def get_image_section_color_average():
    frame = Image.open('./screen.png')  # opening latest screenshot from the image file

    # you can find these locations by opening "t_rex_gameplay.png" in some image editor
    # they usually show coordinates of your pointer location
    origin_x = 730  # top left corner of the image section
    origin_y = 200  # top left corner of the image section
    size_x = 150  # section width
    size_y = 50  # section height

    # this is the selected image section
    image_section = frame.crop((origin_x, origin_y, origin_x + size_x, origin_y + size_y))

    # turning it into black and white image so we only have 0-255 values (ignoring the colors)
    # in the dinosaur game you don't have any colors
    # but if you did you could use this to simplify image brightness calculation
    gray_image_section = ImageOps.grayscale(image_section)
    image_pixel_values = np.array(gray_image_section.getdata())  # turn it into an array of numbers (0-255)

    image_color_average = np.mean(image_pixel_values)  # calculates average brightness of the image section
    print(image_color_average)  # you can see in the console what section values the script receives

    return image_color_average


def shouldJump(image_mean):
    if image_mean < 248:  # this is an arbitrary value - you can adjust it to be more or less sensitive
        return True
    return False


restart_game()  # runs only the first time when you start the python script


while True:
    update_saved_screen()  # gets new t-rex and obstacle positions by taking a screenshot
    image_color_average = get_image_section_color_average()  # calculates image section brightness
    if shouldJump(image_color_average) is True:  # if brightness is smaller than usual then jump
        jump()