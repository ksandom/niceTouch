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

import time

class Devices():
    def __init__(this):
        this.devices = {}
    
    def getPersistentState(this):
        output = {}
        
        for deviceID in this.devices:
            output[deviceID] = this.devices[deviceID].getState()
        return output

    def setPersistentState(this, state):
        for deviceID in state:
            # TODO This should be done in a more object-oriented way.
            try:
                this.devices[deviceID].mostRecentlyIntroduced = state[deviceID]['mostRecentlyIntroduced']
                this.devices[deviceID].setAbsent(False)
            except:
                # We don't currently have this device. Let's put in a dummy device so we can track that we've had it before.
                this.devices[deviceID] = Device(deviceID, 'dummy')
                this.devices[deviceID].loadState(state[deviceID])
                this.devices[deviceID].setAbsent(True)
    

class Device():
    def __init__(this, deviceID, name):
        this.deviceID = deviceID
        this.name = name
        this.mostRecentlyIntroduced = 0
        this.setAbsent(False)

    def __repr__(self):
        return self.deviceID
    
    def __str__(self):
        return self.deviceID + " " + self.name
    
    def getState(this):
        return {'deviceID':this.deviceID, 'name':this.name, 'mostRecentlyIntroduced':this.mostRecentlyIntroduced}
    
    def loadState(this, state):
        this.name = state['name']
        this.mostRecentlyIntroduced = state['mostRecentlyIntroduced']
    
    def setAbsent(this, isAbsent):
        if (isAbsent):
            this.mostRecentlyIntroduced = 0;
        else:
            if this.mostRecentlyIntroduced == 0:
                this.mostRecentlyIntroduced = timestamp = int(time.time())
