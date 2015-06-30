#!/usr/bin/env python
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

from radssh.ssh import Cluster
from radssh.console import RadSSHConsole
from radssh.authmgr import AuthManager
import radssh.config

class Connection(object):
    '''
    wrapper for handling asynchronous connections across cluster
    '''

    def __init__(self,hosts):
        self.hosts = hosts

    @property
    def hosts(self):
        return.__hosts

    @hosts.setter
    def hosts(self,value):
        try:
            self.__hosts.append(str(value))
        except ValueError as err:
            print(str(err))

__author__ = 'michael gardner'