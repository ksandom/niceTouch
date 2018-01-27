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

from . import devices,screens,touchPanels,state


class NiceTouch():
    def __init__(this):
        this.screens = screens.Screens()
        this.touchPanels = touchPanels.TouchPanels()
        this.state = state.State()
    
    
    def scan(this):
        this.screens.scan();
        this.touchPanels.scan();
        this.load() # Load existing saved state and bring it into the current state.
    
    def associateNewDevices(this):
        newestTouchPanelID = this.touchPanels.getNewestUnassociatedDeviceID()
        lastDeviceID = ''
        
        while (newestTouchPanelID and newestTouchPanelID != lastDeviceID):
            newestScreenID = this.screens.getNewestUnassociatedDeviceID()
            
            if newestScreenID:
                this.associateDevices(newestTouchPanelID, newestScreenID)
            else:
                print ("Touch panel " + newestTouchPanelID + " found, but no matching screen was found. Be sure to plug in the screen first.")
            
            lastDeviceID = newestTouchPanelID
            newestTouchPanelID = this.touchPanels.getNewestUnassociatedDeviceID()
    
    def associateDevices(this, touchPanelID, screenID):
        this.touchPanels.devices[touchPanelID].associateWith(screenID)
        this.screens.devices[screenID].associateWith(touchPanelID)
    
    def calibrateDevices(this):
        for deviceID in this.touchPanels.devices:
            # TODO reaching into other classes is not ideal. This should be abstracted away.
            try:
                screenID = this.touchPanels.devices[deviceID].associatedWith
                this.touchPanels.devices[deviceID].calibrate(this.screens.devices[screenID])
            except AttributeError:
                print ("Touch screen \"" + this.touchPanels.devices[deviceID].name + "\" does not appear to be plugged in. Won't calibrate.")
    
    
    def load(this):
        this.screens.setPersistentState(this.state.getState()['screens'])
        this.touchPanels.setPersistentState(this.state.getState()['touchPanels'])
    
    def save(this):
        this.state.setState({
            'screens':this.screens.getPersistentState(),
            'touchPanels':this.touchPanels.getPersistentState()})
        this.state.save()
    
    
    def showState(this):
        print (this.screens.devices)
        print (this.touchPanels.devices)
    
    # TODO Compare to current state to figure out what's new.
    # TODO Associate what's new if possible. And save knowledge.
    # TODO Calibrate everything we know.
    
