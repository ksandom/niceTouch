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

class TouchPanels():
    def __init__(this):
        pass

    def scan(this):
        for deviceID in this.getDevicesIDs():
            if (this.isDeviceATouchPannel(deviceID)):
                print (deviceID)

    def getDevicesIDs(this):
        # TODO This line is horrific. Feel free to submit pull requests making it better, or doing it an entirely different way.
        rawData = subprocess.check_output(['bash', '-c', "xinput list | grep -v 'Virtual' | sed 's/^.*=//g;s/\(	\| \).*$//g'"]).decode()
        """
            What it's doing:
                * bash -c - so I can simply paste in the command that I know works without messing around converting the input and creating bugs.
                * xinput list - Finds the input devices attached.
                * sed - gives us exactly the data we want, and how we want it:
                    * s/^.*=//g - Remove everything up to and include the id=.
                    * s/\(	\| \).*$//g - Remove everything after the id.
        """
        
        return rawData.splitlines()

    def isDeviceATouchPannel(this, deviceID):
        # TODO This line is horrific. Feel free to submit pull requests making it better, or doing it an entirely different way.
        rawData = subprocess.check_output(['bash', '-c', "xinput list " + deviceID + " | grep 'Abs.*\(X\|Y\)' | wc -l"])
        """
            What it's doing:
                * bash -c - so I can simply paste in the command that I know works without messing around converting the input and creating bugs.
                * xinput list - Gives information about a specific device.
                * grep 'Abs.*X\(X\|Y\)': Only find devices with absolute positioning. This may pick up things like drawing tablets. We can figure that out later.
                * wc -l - Gives us a count of matching lines. 0 is not a touch panel. >0 is an absolute device, which is probably a touch panel.
        """
        
        # If not 0, return true.
        return (rawData.splitlines()[0].decode() != '0')
        
