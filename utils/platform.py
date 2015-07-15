'''
#############################################################################

    HPCC SYSTEMS software Copyright (C) 2012 HPCC Systems.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
#############################################################################
'''
import logging

from utils.connection import Connection

class Platform(object):
    '''
    This class implements the logic necessary for driving the HPCC Platform
    and it's specified components within the environment.xml and configuration
    files
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.logger = logging.getLogger(__name__)
        self.directories    = {}
        self.components     = []
        self.hosts          = []

    def list(self,value=None):
        self.logger.info("I listed!")

    def show(self,value=None):
        self.logger.info("I showed!")

    def start(self,value=None):
        print "oogabooga"
        self.logger.info("I started!")

    def stop(self,value=None):
        self.logger.info("I stopped!")

    def restart(self,value=None):
        self.logger.info("I restarted!")

    def status(self,value=None):
        self.logger.info("I statused!")
