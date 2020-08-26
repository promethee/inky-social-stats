#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import json
from PIL import Image, ImageDraw, ImageFont
import signal
from evdev import uinput, UInput, ecodes as e
import buttonshim
from TwitterUserStats import TwitterUserStats

KEYCODES = [e.KEY_A, e.KEY_B, e.KEY_C, e.KEY_D, e.KEY_E]
BUTTONS = [buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E]

twitter_index = 0
twitter_handles = list()

print('[?] will try to open file named "twitter.json"')
try:
  with open('twitter.json') as json_file:
    data = json.load(json_file)
    print('[✓] file found with', len(data), 'handle(s)')
    for i in range(len(data)):
      print('[✓] twitter handle found at position', i, data[i])
      twitter_handles.append(data[i])
except FileNotFoundError as e:
  print('[⨉] missing file named "twitter.json"')

print('[✓] twitter handles loaded')

TwitterUsers = list()

for i in range(len(twitter_handles)):
  TwitterUsers.append(TwitterUserStats(twitter_handles[i], i))

if len(TwitterUsers) > 0:
  TwitterUsers[0].toggle(True)

try:
    ui = UInput({e.EV_KEY: KEYCODES}, name="Button-SHIM", bustype=e.BUS_USB)

except uinput.UInputError as e:
    print(e.message)
    print("Have you tried running as root? sudo {}".format(sys.argv[0]))
    sys.exit(0)

@buttonshim.on_press(BUTTONS)
def button_p_handler(button, pressed):
    for i in range(len(TwitterUsers)):
      TwitterUsers[i].toggle(i == BUTTONS.index(button))
    TwitterUsers[BUTTONS.index(button)].update()
  
@buttonshim.on_release(BUTTONS)
def button_r_handler(button, pressed):
    TwitterUsers[BUTTONS.index(button)].display()

signal.pause()
