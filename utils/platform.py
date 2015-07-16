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
        logging.info('Platform.__init__(self)')
        self.directories    = {}
        self.components     = []
        self.hosts          = []

    def list(self,value=None):
        logging.info("I listed!")

    def show(self,value=None):
        logging.info("I showed!")

    def start(self,value=None):
        print "oogabooga"
        logging.info("I started!")

    def stop(self,value=None):
        logging.info("I stopped!")

    def restart(self,value=None):
        logging.info("I restarted!")

    def status(self,value=None):
        logging.info("I statused!")
