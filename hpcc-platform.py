#!/usr/bin/env python
'''
/*#############################################################################

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
############################################################################ */
'''

import sys
import os
import os.path
import getopt
import Queue
import time
import date
import datetime
import logging
import ConfigParser
import signal

from hpcc.cluster.host import Host
from hpcc.cluster.task import ScriptTask
from hpcc.cluster.thread import ThreadWithQueue

def signal_handler(signal, frame):
    if signal == signal.SIGINT:
        print('\033[0m\nhpcc-run.py interrupted')
    else:
        print('\033[0m\nExiting hpcc-run.py')
    os._exit(int(signal))

signal.signal(signal.SIGINT,  signal_handler)
signal.signal(signal.SIGQUIT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

class HPCC(object):
    '''
    This class implements the logic necessary for driving the HPCC Platform
    and it's specified components within the environment.xml and configuration
    files
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.environment_directory  = "/etc/HPCCSystems"
        self.component              = None
        self.save                   = False
        self.force_stop             = False
        self.debug                  = False

    def usage(self):
        print("Usage:  hpcc-platform [option(s)]\n")
        print(" -c|--component      -c <component_name>")
        print(" -l|--list           list all components and their respective addresses")
        print(" -d|--debug          debug logging level")
        print(" -f|--force          sigkill on components that fail to stop")
        print(" -v|--verbose        print all information to STDOUT"
        print(" -?|--help           print help")

if __name__ == '__main__':
