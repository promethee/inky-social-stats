#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep
import json
import signal
from evdev import uinput, UInput, ecodes as e
import buttonshim
from UserStats import UserStats

def color_scan():
  buttonshim.set_pixel(0xff, 0x00, 0x00)
  sleep(0.1)
  buttonshim.set_pixel(0xff, 0xff, 0x00)
  sleep(0.1)
  buttonshim.set_pixel(0x00, 0xff, 0x00)
  buttonshim.set_pixel(0x00, 0xff, 0xff)
  sleep(0.1)
  buttonshim.set_pixel(0x00, 0x00, 0xff)
  sleep(0.1)
  buttonshim.set_pixel(0xff, 0x00, 0xff)
  sleep(0.1)
  buttonshim.set_pixel(0x00, 0x00, 0x00)
  sleep(0.1)

KEYCODES = [e.KEY_A, e.KEY_B, e.KEY_C, e.KEY_D, e.KEY_E]
BUTTONS = [buttonshim.BUTTON_A, buttonshim.BUTTON_B, buttonshim.BUTTON_C, buttonshim.BUTTON_D, buttonshim.BUTTON_E]

social_handles = list()

color_scan()

# Everything is fine so far
buttonshim.set_pixel(0x00, 0xff, 0x00)

print('[?] will try to open file named "twitter.json"')
try:
  with open('twitter.json') as json_file:
    data = json.load(json_file)
    print('[✓] file found with', len(data), 'handle(s)')
    for i in range(len(data)):
      buttonshim.set_pixel(0x00, 0x00, 0x00)
      print('[✓] twitter handle found at position', i, data[i])
      social_handles.append(data[i])
      buttonshim.set_pixel(0x00, 0x00, 0xff)
except FileNotFoundError as e:
  buttonshim.set_pixel(0xff, 0x00, 0x00)
  print('[⨉] missing file named "twitter.json"')

print('[✓] handles loaded')

Users = list()

for i in range(len(social_handles)):
  # Only twitter for now
  Users.append(UserStats(social_handles[i], 'https://mobile.twitter.com/'))

if len(Users) > 0:
  Users[0].toggle(True)
  Users[0].display()

def update_users():
  while True:
    color_scan()
    for user in Users:
      user.update()
    sleep(60)

user_thread = Thread(target=update_users)
user_thread.start()

@buttonshim.on_press(BUTTONS)
def button_p_handler(button, pressed):
    buttonshim.set_pixel(0xff, 0xff, 0x00)
  
@buttonshim.on_release(BUTTONS)
def button_r_handler(button, pressed):
    color_scan()
    buttonshim.set_pixel(0x00, 0x00, 0x00)
    Users[BUTTONS.index(button)].display()

signal.pause()
