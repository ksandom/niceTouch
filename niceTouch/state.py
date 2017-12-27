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

import yaml

class State():
    def __init__(this):
        # Figure out where we will store state information.
        this.stateDir="/home/ksandom/.config"
        this.stateFile="niceTouch.yaml"
        this.statePath=this.stateDir+"/"+this.stateFile
        
        this.load()
    
    def __exit__(self):
        self.save()
    
    def load(this):
        try:
            with open(this.statePath, 'r') as stream:
                try:
                    this.state = yaml.load(stream)
                except yaml.YAMLError as error:
                    print ("Could not parse the YAML in "+this.statePath+". Human edited? Try a YAML lint. The error was")
                    print (error)
                    this.state = {}
        except FileNotFoundError as error:
            print ("Could not find the file " + this.statePath + ". If this is the first run, you can safely ignore this error.")
            this.state={}
    
    def save(this):
        # TODO Add try/excepts as conditions become apparrent.
        with open(this.statePath, 'w') as stream:
            yaml.dump(this.state)
