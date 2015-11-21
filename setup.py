# The Logrus
#
# Copyright 2015 Joe Block <jpb@unixorn.net>
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


from setuptools import setup, find_packages

name = "logrus"
version = "0.0.3"

setup(
  name = name,
  author = "Joe Block",
  author_email = "jpb@unixorn.net",
  description = "The Logrus is a collection of random utility functions",
  url = "https://github.com/unixorn/logrus",
  packages = find_packages(),
  version = version,
  download_url = "https://github.com/unixorn/logrus/tarball/%s" % version,
  keywords = ["devops", "utility"],
)
