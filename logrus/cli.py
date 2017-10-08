#!/usr/bin/env python
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
#
#
"""
Utility functions for dealing with programs.
"""

import distutils.spawn


def findSubCommand(args):
  """
  Given a list ['foo','bar', 'baz'], attempts to create a command name in the
  format 'foo-bar-baz'. If that command exists, we run it. If it doesn't, we
  check to see if foo-bar exists, in which case we run `foo-bar baz`. We keep
  taking chunks off the end of the command name and adding them to the argument
  list until we find a valid command name we can run.

  This allows us to easily make git-style command drivers where for example we
  have a driver script, foo, and subcommand scripts foo-bar and foo-baz, and when
  the user types `foo bar foobar` we find the foo-bar script and run it as
  `foo-bar foobar`

  :param list|tuple args: list to try and convert to a command args pair
  :returns: command and arguments list
  :rtype: tuple
  :raises StandardError: if the args can't be matched to an executable subcommand
  """
  # If the only command we find is the first element of args, we've found the
  # driver script itself and re-executing it will cause an infinite loop, so
  # don't even look at the first element on its own.
  for n in range(len(args) - 1):
    command = '-'.join(args[:(len(args) - n)])
    commandArgs = args[len(args) - n:]
    if isProgram(command):
      return (command, commandArgs)
  raise StandardError("Could not find a %s subcommand executable" % command)


def isProgram(name):
  """
  Search for a given program in $PATH, and return True if it exists and
  is executable.

  :param str name: Name of program to search for
  :returns: whether or not the program can be found in $PATH
  :rtype: bool
  """
  return distutils.spawn.find_executable(name) is not None
