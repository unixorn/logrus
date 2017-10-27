# The Logrus
#
# Copyright 2015-2017 Joe Block <jpb@unixorn.net>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

'''
logrus is a collection of utility functions.
'''

import os
import shutil
import subprocess
from setuptools import setup, find_packages, Command


def systemCall(command):
  '''
  Run a command and return stdout.

  Would be better to use subprocess.check_output, but this works on 2.6,
  which is still the system Python on CentOS 7.
  '''
  p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
  return p.stdout.read()


name = 'logrus'
version = "0.2.%s" % (systemCall('git rev-list HEAD --count').strip())


class CleanCommand(Command):
  '''
  Add a clean option to setup.py's commands
  '''
  description = 'Clean up'
  user_options = []


  def initialize_options(self):
    self.cwd = None


  def finalize_options(self):
    self.cwd = os.getcwd()


  def run(self):
    assert os.getcwd() == self.cwd, "Must be in package root: %s" % self.cwd
    if os.path.isdir('build'):
      shutil.rmtree('build')
    if os.path.isdir('dist'):
      shutil.rmtree('dist')


setup(
  name=name,
  author="Joe Block",
  author_email="jpb@unixorn.net",
  description="The Logrus is a collection of random utility functions",
  url="https://github.com/unixorn/logrus",
  packages=find_packages(),
  version=version,
  download_url="https://github.com/unixorn/logrus/tarball/%s" % version,
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Operating System :: POSIX",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 2.6",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  cmdclass={
    "clean": CleanCommand,
  },
  entry_points={
    "console_scripts": [
      "human-time = %s.time:humanTimeConverter" % name,
    ]
  },
  keywords=["devops", "utility"],
)
