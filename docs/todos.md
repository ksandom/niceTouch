# TODOs

Here is a list of stuff that needs to be done to improve this.

## For initial release.

* Detect screens with offsets. - DONE
* Detect touch devices. - IN PROGRESS
* Record state.
* Notice new screen.
* Notice new touch device.
 * Automatically associate new touch device with recent unassociated screen.
* Calibrate each touch device with its associated screen.
* Documentation
 * How to use it.
 * Normal flow.
 * Basic debugging.

## Stuff I invite other peoplee do contribute.

I've ordered them roughly in my order of preference, but feel free to take what ever interests you. If you see anything nissing, you're welcomme to add it.

* Make installation easy. `pip install`?
* Unit tests.
* Add exception handeling.
* Graceful failure.
* Abstract functionality functionality better.
* Improve the code that harvests data about the screens and touch panels.
* Better commandline interaction.
* Make able to run as a service.
 * DBUS integration.
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
