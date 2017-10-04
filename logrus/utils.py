#!/usr/bin/env python
#
# Copyright 2017 Joe Block <jpb@unixorn.net>
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
#
#
'''
Random utility functions
'''

import errno
import logging
import os
import subprocess


def squashDicts(*dict_args):
  '''
  Given any number of dicts, shallow copy and merge into a new dict,
  precedence goes to key value pairs in latter dicts.
  '''
  result = {}
  for dictionary in dict_args:
    result.update(dictionary)
  return result


def getCustomLogger(name, logLevel):
  '''
  Set up logging

  :param str name: What log level to set
  :param str logLevel: What log level to use
  :rtype: logger
  '''
  assert isinstance(name, basestring), ("name must be a string but is %r" % name)

  validLogLevels = ['CRITICAL', 'DEBUG', 'ERROR', 'INFO', 'WARNING']

  if not logLevel:
    logLevel = 'DEBUG'

  # If they don't specify a valid log level, err on the side of verbosity
  if logLevel.upper() not in validLogLevels:
    logLevel = 'DEBUG'

  numericLevel = getattr(logging, logLevel.upper(), None)
  if not isinstance(numericLevel, int):
    raise ValueError("Invalid log level: %s" % logLevel)

  logging.basicConfig(level=numericLevel, format='%(asctime)s %(levelname)-9s:%(name)s:%(module)s:%(funcName)s: %(message)s')
  logger = logging.getLogger(name)
  return logger


def mkdir_p(path):
  '''
  Mimic `mkdir -p` since os module doesn't provide one.

  :param str name: Name of program to search for

  '''
  try:
    os.makedirs(path)
  except OSError as exception:
    if exception.errno != errno.EEXIST:
      raise


def systemCall(command):
  '''
  Run a command and return stdout.

  Would be better to use subprocess.check_output, but this works on 2.6,
  which is still the system Python on CentOS 7.

  :param str command: Command to run
  :rtype: str
  '''
  assert isinstance(command, basestring), ("command must be a string but is %r" % command)

  p = subprocess.Popen([command], stdout=subprocess.PIPE, shell=True)
  return p.stdout.read()
