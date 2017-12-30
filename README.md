# niceTouch
Easily configure multiple touch and non touch screens on a single linux system.

## Use

For best results, read [how to use it](docs/howToUseIt.md).

* First run it with the least number of sccreen/touchpanels connected. - Preferably, one connected pair.
* Now connect your next screen/touchpannel pair and run it again.
  * Repeat until all your displays are connected.

Every time you connect a screen that doesn't have a corresponding touchpanel, you will need to wait at least 10 seconds before proceeding to the next step.

Eg

    $ ./nt.py 
    Calibrate: touchPanel 9 to screen eDP-1

Then I plug in an HDMI/USB touch screen, and run it again.

    $ ./nt.py 
    Calibrate: touchPanel 14 to screen HDMI-1
    Calibrate: touchPanel 9 to screen eDP-1

Soon, I want to have this running as a service listening to DBUS so that it will automatically calibrate all touch screens as soon as something changes. See [TODOs](docs/todos.md).

## Install

At the moment I'm running this from within the cloned repo. One of my next [TODOs](docs/todos.md) is to make it really easy.

### Pre-requisites
* Python 3
* xrandr

## Contributions/Progress

See [TODOs](docs/todos.md) for stuff that needs doing and what I'm focussing on.

Feel free to

* Create [issues](https://github.com/ksandom/niceTouch/issues) to report bugs or suggestions.
* [Pull requests](https://github.com/ksandom/niceTouch/pulls)
  * Fix bugs
  * Add features
