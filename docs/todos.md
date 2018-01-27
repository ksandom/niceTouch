# TODOs

Here is a list of stuff that needs to be done to improve this.

## For initial release.

* Detect screens with offsets. - DONE
* Detect touch devices. - DONE
* Record state. - DONE
* Notice new screen. - DONE
* Notice new touch device. - DONE
  * Automatically associate new touch device with recent unassociated screen. - DONE
* Calibrate each touch device with its associated screen. - DONE
* Remove hard-coded path to persistent state. - DONE
* Documentation - DONE
  * How to use it. - [DONE](docs/howToUseIt.md)
  * Normal flow. - [DONE](docs/howToUseIt.md)
  * Basic debugging. - [DONE](docs/debugging.md)

## Soon

* # -*- coding: utf-8 -*-
* Fix formatting
  * pep8
  * pyflakes
  * yapf
* Unit tests.
  * env python3 -m unittest discover -v
  * pytest
  * coverage
    * pytest-cov
    * colorama
* Make installation easy. `pip install`? - DONE
  * Version
  * Classifiers
  * README.rst
  * https://readthedocs.org/ 
    * sphinx
    * find sphinx tutorial
    * eg https://github.com/palankai/quepy/blob/develop/docs/conf.py
  * travis
* Any bug fixes.

## Stuff I invite other peoplee do contribute.

I've ordered them roughly in my order of preference, but feel free to take what ever interests you. If you see anything nissing, you're welcomme to add it.

* Add more/better exception handeling.
  * Better handle state when a screen has been connected, but not configured yet. Eg `HDMI-1 connected`. For clues, start [here](https://github.com/ksandom/niceTouch/blob/master/niceTouch/screens.py#L56).
* Graceful failure.
* Better identification of the touch panel. At the moment the whole thing will break if it gets a different ID in the future, which is a very real possibility, especially if devices are plugged in in a different order. Name by itself isn't a viable solution, because it won't tolerate duplicates.
* Abstract functionality functionality better.
* Improve the code that harvests data about the screens and touch panels. See TODOs inline in the code.
* Better commandline interaction.
* Make able to run as a service.
  * DBUS integration.
    * New Screen.
    * New Touchpannel.
    * Change resolution.
    * Change layout.
    * Change orientation. - Assumptions may need to be changed at this point.
  * Add polling as another option as well?
* Install as KDE service.
* Intrgrations with other desktop managers.
* Documentation.
  * How to fix it when niceTouch gets it wrong.
* Make code more pythonic.
* Make optional to guess in ambiguous situations (Eg multiple touch interfaces permanently attached.)
* Improve guessing.
  * Default associations with brands/models.
  * Prioritise device order?
  * Other clues?
