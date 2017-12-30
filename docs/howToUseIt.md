# How to use it

* First run it with the least number of sccreen/touchpanels connected. - Preferably, one connected pair.
* Now connect your next screen/touchpannel pair and run it again.
  * Repeat until all your displays are connected.

Every time you connect a screen that doesn't have a corresponding touchpanel, you will need to wait at least 10 seconds before proceeding to the next step.

Once it knows all your devices and has calibrated them correctly, you should be able to simply plug them all in, in one go.

# For best results

* Order
  * Plug in the screen (HDMI, DP, VGA etc) first.
  * Plug in the touch panel second.
* Wait 10 seconds when plugging in a touchscreen after a non-touchscreen. Otherwise the touchpanel of the new touchscreen may get associated with the non-touch screen.

# How it works

When it runs it

* Looks for anything it doesn't know.
* When it sees a new touchpanel, it will try to associate it with a screen that is less than 10 seconds old. If no screen exists yet, no association will happen.
* Calibrate all known touchpanes.

