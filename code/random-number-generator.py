#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import os

picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V3
from PIL import Image,ImageDraw,ImageFont
import traceback
import random

logging.basicConfig(level=logging.ERROR)

try:
    #logging.info("Writing some stuff")
    epd = epd2in13_V3.EPD()
    epd.init()
    #epd.Clear(0xFF)

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 64)
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

    randomnumber = str(random.randint(1, 1000000))

    #draw.rectangle((20, 10, 220, 105), fill = 255)
    draw.text((18, 22), randomnumber, font = font, fill = 0)
    #image = image.rotate(180, expand = True)
    epd.displayPartBaseImage(epd.getbuffer(image))

    #epd.init()
    #epd.Clear(0xFF)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V3.epdconfig.module_exit(cleanup=True)
    exit()
