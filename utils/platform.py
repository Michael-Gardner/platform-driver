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
        self.directories    = {}
        self.components     = []
        self.hosts          = []
        self.connection     = Connection(self.hosts)
        # connection object



    def setupRadSSH(self):
        self.login                  = AuthManager(self.user,include_userkeys=True)
        self.console                = RadSSHConsole()
        self.connections            = [(x, None) for x in self.hosts]
        socket.setdefaulttimeout(10)


    def start(self):
        self.setupRadSSH()
        self.cluster = Cluster(self.connections, self.login, console=self.console)
        self.cluster.run_command('hostname')
        for host, job in self.cluster.last_result.items():
            if job.completed and job.result.return_code == 0:
                print("%s" % job.result.stdout)

    def print_output(self):
        '''
        print_output formats output from all command types
        :return: None
        '''
        for host, job in self.cluster.last_result.items():
            if job.completed and job.result.return_code == 0:
                print(job.result.stdout)
            else:
                print("%s   %s" % (host, self.cluster.connections[host]))
                print("%s   %s   %s" % (job, job.result.status, job.result.stderr))


    def restart(self):
        print("Restarting")

    def stop(self):
        print("Stopping")

    def listall(self):
        try:
            print("Listall")
        except OSError as err:
            print(str(err))
            exit(1)

    def checkConnections(self):
        print("Checking Connections")


__author__ = 'adhok'
