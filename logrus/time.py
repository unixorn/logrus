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

'''
Time utility functions
'''
import sys
from dateutil.relativedelta import relativedelta as deltaTime

def humanTime(seconds):
  '''
  Convert seconds to something more human-friendly
  '''
  intervals = ['days', 'hours', 'minutes', 'seconds']
  x = deltaTime(seconds=seconds)
  return ' '.join('{} {}'.format(getattr(x, k), k) for k in intervals if getattr(x, k))


def humanTimeConverter():
  '''
  Cope whether we're passed a time in seconds on the command line or via stdin
  '''
  if len(sys.argv) == 2:
    print humanFriendlyTime(seconds=int(sys.argv[1]))
  else:
    for line in sys.stdin:
      print humanFriendlyTime(int(line))
      sys.exit(0)


if __name__ == '__main__':
  print 'This is a library, not a stand alone script'
  sys.exit(1)
