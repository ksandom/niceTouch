# niceTouch
Easily configure multiple touch and non touch screens on a single linux system.

## Use

    $ ./nt.py 
    Touch screen "BYZHYYZHY By ZH851" does not appear to be plugged in. Won't calibrate.
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

## Contributions

See [TODOs](docs/todos.md) for stuff that needs doing.

TODO Contributions
