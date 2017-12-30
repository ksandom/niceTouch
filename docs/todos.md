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
* Documentation
 * How to use it.
 * Normal flow.
 * Basic debugging.

## For the second release

* Unit tests.
* Make installation easy. `pip install`?
* Any bug fixes.

## Stuff I invite other peoplee do contribute.

I've ordered them roughly in my order of preference, but feel free to take what ever interests you. If you see anything nissing, you're welcomme to add it.

* Add more/better exception handeling.
* Graceful failure.
* Abstract functionality functionality better.
* Improve the code that harvests data about the screens and touch panels.
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
