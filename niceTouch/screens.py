"""
Easily configure multiple touch and non touch screens on a single linux system.
Copyright (C) 2017  Kevin Sandom

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import subprocess
import time
from . import devices


class Screens(devices.Devices):
    def __init__(this):
        devices.Devices.__init__(this)
        this.devices = {}

    def scan(this):
        output = {}

        # TODO This command is horrific. Feel free to submit pull requests
        # making it better, or doing it an entirely different way.
        # I've started by at least getting it pep8 compliant.
        command = [
            'bash',
            '-c',
            "xrandr" +
            " | grep ' connected '" +
            " | sed 's/ (.*//g;s/ .* /,/g;s/x/,/g;s/+/,/g'"]
        rawData = subprocess.check_output(command)
        """
            What it's doing:
                * bash -c - so I can simply paste in the command that I know works without messing around converting the input and creating bugs.
                * xrandr - gives the list of attached screens.
                * grep - gives us the data we want.
                * sed - gives us exactly the data we want, and how we want it:
                    * s/ (.*//g - Remove the space and opening bracket all the way to the end of the string.
                    * s/ .* /,/g - Remove everything except the ID and the dimention and position data.
                    * s/x/,/g - Change the x in the resolution to a ,. This plus the next step make the explode easy and one step.
                    * s/+/,/g - Change the + for the offsets to ,s to make the explode one step.

            Why it needs to be revisited:
                * It is dependant on specific formatting of the data.
                    * Minor changes to the human readable format will destroy compatiblity.
                    * Different versions of xinput may output the data differently.
                * There is almost certainly a way to get this information within python in a more elegant way.
        """

        # Process the rawData.
        rawDataLines = rawData.splitlines()
        for line in rawDataLines:
            lineParts = line.decode().split(',')
            try:
                output[lineParts[0]] = Screen(lineParts[0], lineParts[1], lineParts[2], lineParts[3], lineParts[3])
            except:
                print ("The screen data was not as expected. This is known to happen when the layout is being updated, but here is the line just in case\n" + line.decode())

        # Return the output.
        this.devices = output
        return output


class Screen(devices.Device):
    def __init__(this, deviceID, width, height, xOffset, yOffset):
        devices.Device.__init__(this, deviceID, 'unnamed')
        this.deviceID = deviceID
        this.width = width
        this.height = height
        this.xOffset = xOffset
        this.yOffset = yOffset
        this.mostRecentlyIntroduced = timestamp = int(time.time())

    def __repr__(self):
        return self.deviceID
