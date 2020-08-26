#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import json
from PIL import Image, ImageDraw, ImageFont
from inky.auto import auto
import signal
from evdev import uinput, UInput, ecodes as e
import buttonshim
from UserStats import UserStats

inky_display = auto()

# Uncomment the following if you want to rotate the display 180 degrees
inky_display.h_flip = True
inky_display.v_flip = True


KEYCODES = [e.KEY_A, e.KEY_B, e.KEY_C, e.KEY_D, e.KEY_E]
BUTTONS = [buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E]

img = Image.new("P", inky_display.resolution)
draw = ImageDraw.Draw(img)

fontsize = 40
font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize)

draw.text((0, 0), 'Starting', inky_display.BLACK, font)
inky_display.set_image(img)
inky_display.show(img)

social_handles = list()

print('[?] will try to open file named "twitter.json"')
try:
  with open('twitter.json') as json_file:
    data = json.load(json_file)
    print('[✓] file found with', len(data), 'handle(s)')
    for i in range(len(data)):
      print('[✓] twitter handle found at position', i, data[i])
      social_handles.append(data[i])
except FileNotFoundError as e:
  print('[⨉] missing file named "twitter.json"')

print('[✓] handles loaded')

Users = list()

for i in range(len(social_handles)):
  # Only twitter for now
  Users.append(UserStats(social_handles[i], 'https://mobile.twitter.com/'))

if len(Users) > 0:
  Users[0].toggle(True)
  Users[0].display()

@buttonshim.on_press(BUTTONS)
def button_p_handler(button, pressed):
    for i in range(len(Users)):
      Users[i].toggle(i == BUTTONS.index(button))
    Users[BUTTONS.index(button)].update()
  
@buttonshim.on_release(BUTTONS)
def button_r_handler(button, pressed):
    Users[BUTTONS.index(button)].display()

signal.pause()
