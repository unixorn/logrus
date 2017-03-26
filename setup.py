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

"""
logrus is a collection of utility functions.
"""

from setuptools import setup, find_packages, Command
import os
import shutil

name = "logrus"
version = "0.0.5"


class CleanCommand(Command):
  """
  Add a clean option to setup.py's commands
  """
  description = "Clean up"
  user_options = []


  def initialize_options(self):
    self.cwd = None


  def finalize_options(self):
    self.cwd = os.getcwd()


  def run(self):
    assert os.getcwd() == self.cwd, "Must be in package root: %s" % self.cwd
    if os.path.isdir("build"):
      shutil.rmtree("build")
    if os.path.isdir("dist"):
      shutil.rmtree("dist")


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
  keywords=["devops", "utility"],
)
