# improvement because I am actually using the luma library properly having imported it as module
# and not just using DEMO_OPTS as a crutch
# standalone pif script for functional demo

#!/bin/env python3

import os, random
import time
from time import sleep

#from demo_opts import get_device
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1351
from luma.core.virtual import viewport

serial = spi(device=0, port=0)
device = ssd1351(serial)

from PIL import ImageFont, ImageDraw

# Mostly crawl.py example also using http://codelectron.com/setup-oled-display-raspberry-pi-python/ for info

# importing a text file (raw poem) and then splitting into a line with 3 words each line:
# how to split into 1 word each line https://stackoverflow.com/questions/16922214/reading-a-text-file-and-splitting-it-into-single-words-in-python
# how to split with specifying a number of words / strings https://www.w3schools.com/python/ref_string_split.asp

def main():

    poemdir = random.choice(os.listdir("/home/pi/Documents/Pif/pif_poems/"))
    randompoem = "/home/pi/Documents/Pif/pif_poems/" + poemdir

    blurb = open(randompoem,"r").read()
    virtual = viewport(device, width=device.width, height=768)

    for _ in range(1):
        with canvas(device) as draw:
            font = ImageFont.truetype('/home/pi/Documents/Pif/luma.examples/examples/fonts/pixelmix.ttf',9)
            for i, line in enumerate(blurb.split("\n")):
                draw.text((0, 0 + (i * 12)), text=line, font=font, fill="white")

            time.sleep(4.0)
x = 0
if __name__ == "__main__":
    while x < 50:
        try:
            #device = get_device()
            main()
        except KeyboardInterrupt:
            pass
