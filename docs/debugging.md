# Debugging

There are a limited number of things that can go wrong.

IMPORTANT: Messing with ~/.config/niceTouch.yaml is short term until the program matures. I've intentionally chosen yaml so people *can* mess with it, but in due time that will be discouraged as better solutions get implemented.

## Calibrates against the wrong screen

I haven't seen this yet. If things get drastic, you can remove ~/.config/niceTouch.yaml

But preferably, have a read and see if you can see what's wrong. 

Possible causes

* The touchpanel ID has changed. - I hope to have better handeling of this soon. In the mean time, the cleanest course of action is probably to delete the yaml file, and go through [the process](howToUseIt.md) again.
* The touchpanel was plugged in less than 10 seconds after a non-touch screen.

## Touch screen interacts with the entire desktop area

Sounds like calibration hasn't happened. Have you run `nt` after the device was plugged in? See [hoToUseIt.md](hoToUseIt.md) to make sure you're doing it right.

Failing that, Have a look at the output when running the command. Pull requests are welcome.
