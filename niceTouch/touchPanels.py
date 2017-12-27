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
        this.touchPanels = []

    def scan(this):
        for device in this.getDevices():
            if (this.isDeviceATouchPannel(device)):
                this.touchPanels.append(device)

    def getDevices(this):
        output = []
        
        # TODO This line is horrific. Feel free to submit pull requests making it better, or doing it an entirely different way.
        rawData = subprocess.check_output(['bash', '-c', "xinput list | grep -v Virtual | sed 's/\(↳\|⎜\|id=\)//g;s/\(	\|   *\)/,/g' | cut -d, -f 2,4"]).decode()
        """
            What it's doing:
                * bash -c - so I can simply paste in the command that I know works without messing around converting the input and creating bugs.
                * xinput list - Finds the input devices attached.
                * grep -v Virtual - Removes the virtual devices since we don't need them.
                * sed - manipulates the string to make it easy to grab what we want:
                    * s/\(↳\|⎜\|id=\)//g - Strips out characters that get in our way.
                    * s/\(	\|   *\)/,/g - Converts multiple spaces to a comma to denote a field.
                * cut -d, -f 2,4 - Gives us field 2 and 4 using the comma as the delimeter.
            
            Why it needs to be revisited:
                * It is dependant on specific formatting of the data.
                    * Minor changes to the human readable format will destroy compatiblity.
                    * Different versions of xinput may output the data differently.
                * There is almost certainly a way to get this information within python in a more elegant way.
        """
        
        for line in rawData.splitlines():
            lineParts = line.split(",")
            
            output.append(Device(lineParts[1], lineParts[0]))
        
        return output

    def isDeviceATouchPannel(this, device):
        # TODO This line is horrific. Feel free to submit pull requests making it better, or doing it an entirely different way.
        rawData = subprocess.check_output(['bash', '-c', "xinput list " + device.deviceID + " | grep 'Abs.*\(X\|Y\)' | wc -l"])
        """
            What it's doing:
                * bash -c - so I can simply paste in the command that I know works without messing around converting the input and creating bugs.
                * xinput list - Gives information about a specific device.
                * grep 'Abs.*X\(X\|Y\)': Only find devices with absolute positioning. This may pick up things like drawing tablets. We can figure that out later.
                * wc -l - Gives us a count of matching lines. 0 is not a touch panel. >0 is an absolute device, which is probably a touch panel.
            
            Why it needs to be revisited:
                * It is dependant on specific formatting of the data.
                    * Minor changes to the human readable format will destroy compatiblity.
                    * Different versions of xinput may output the data differently.
                * There is almost certainly a way to get this information within python in a more elegant way.
        """
        
        # If not 0, return true.
        return (rawData.splitlines()[0].decode() != '0')

class Device():
    def __init__(this, deviceID, name):
        this.deviceID = deviceID
        this.name = name

    def __repr__(self):
        return self.deviceID
    
    def __str__(self):
        return self.deviceID + " " + self.name
