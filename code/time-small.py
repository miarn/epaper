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
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.INFO)

try:
    logging.info("Display time badly")
    epd = epd2in13_V3.EPD()
    epd.init()
    epd.Clear(0xFF)

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    time_image = Image.new('1', (epd.height, epd.width), 255)
    time_draw = ImageDraw.Draw(time_image)
    num = 0

    while (True):
        time_draw.rectangle((120, 80, 220, 105), fill = 255)
        time_draw.text((120, 80), time.strftime('%H:%M:%S'), font = font, fill = 0)
        epd.display(epd.getbuffer(time_image))
        num = num + 1
        if(num == 2):
            break

    epd.init()
    epd.Clear(0xFF)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V3.epdconfig.module_exit(cleanup=True)
    exit()