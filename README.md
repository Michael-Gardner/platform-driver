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

<h1>platform-driver</h1>

<p>This repository is for developing an alternate driver for the
HPCC-Platform that is based on python instead of bash scripts</p>

<ul>
    <li>validation of environment.xml on host node</li>
    <li>diff of all machines environment.xml to insure consistency across environment</li>
    <li>stopall</li>
    <li>selective pssh or radSSH driver</li>
</ul>
<h3>Library</h3>

- hpcc
  - cluster
    - thread.py
    - host.py
    - task.py

<p>This library of classes is inherited from https://github.com/hpcc-systems/HPCC-Platform.git and is released under the Apache 2.0 license</p>
