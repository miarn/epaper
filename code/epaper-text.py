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
import datetime
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Writing some stuff")
    epd = epd2in13_V3.EPD()
    epd.init()
    epd.Clear(0xFF)

    font = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 64)
    image = Image.new('1', (epd.height, epd.width), 255)
    draw = ImageDraw.Draw(image)

    today = datetime.date.today()
    end = datetime.date(2042, 6, 6)
    now = datetime.datetime.now()
    days = str((end - today).days)

    # draw.rectangle((20, 10, 220, 105), fill = 255)
    draw.text((20, 10), days, font = font, fill = 0)
    image = image.rotate(180)
    epd.display(epd.getbuffer(image))

    # epd.init()
    # epd.Clear(0xFF)

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13_V3.epdconfig.module_exit(cleanup=True)
    exit()