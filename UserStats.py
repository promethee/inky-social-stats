import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont
from inky.auto import auto

inky_display = auto()

# Uncomment the following if you want to rotate the display 180 degrees
inky_display.h_flip = True
inky_display.v_flip = True

img = Image.new("P", inky_display.resolution)
draw = ImageDraw.Draw(img)

fontsize = 24
font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize)

class UserStats:
  active = False
  handle_position = (0, 0)
  def __init__(self, handle, url):
    self.handle = handle
    self.url = url
    self.tweets = -1
    self.followers = -1
    self.following = -1
    self.show = False
    self.update()
  def toggle(self, _show):
    self.show = _show
  def display(self):
    print('[✓] displaying', self.handle, 'stats')
    draw.rectangle((0, 0, inky_display.resolution[0], inky_display.resolution[1]), fill="white")
    draw.text((0, 0), '@' + self.handle, inky_display.colour, font)
    draw.text((0, 24), str(self.tweets) + ' tweets', inky_display.BLACK, font)
    draw.text((0, 48), str(self.followers) + ' followers', inky_display.BLACK, font)
    draw.text((0, 72), str(self.following) + ' following', inky_display.BLACK, font)
    inky_display.set_image(img)
    inky_display.show(img)

  def update(self):
    print('\n[✓] fetching', self.handle, 'page')
    r = requests.get(self.url + self.handle)
    print('[✓] parsing', self.handle, 'page')
    raw_html = r.text
    soup = BeautifulSoup(raw_html, 'html.parser')
    stats = soup.find_all(class_='statnum')
    self.tweets, self.followers, self.following = [stat.get_text() for stat in stats]
