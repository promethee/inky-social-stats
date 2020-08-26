# inky-social-stats

### E-Ink User Stats gadget

Show social stats (followers, stars, etc) of up to 5 accounts, by scrapping web availables data (easier rhyme with lazier)

## Requirements

- [inky pHat](https://shop.pimoroni.com/products/inky-phat?variant=12549254938707)
- [Button shim](https://shop.pimoroni.com/products/button-shim)


## Install
- Run 
  ```
  sudo install.sh
  ```
  to install the required dependencies

- Add a `twitter.json` file where the whole project is install, containing:
  ```
  [
    'some_twitter_handle_without_arobase',
    'up_to_5_handles_can_be_added'
  ]
  ```
- Add  
  ```
  @reboot python ~/inky-social-stats/main.py &
  ```
  to your crontab to launch it upon raspberry start

## Upcoming

- github account stars / follower ?
- [inky wHat](https://shop.pimoroni.com/products/inky-what?variant=21214020436051) support ?
