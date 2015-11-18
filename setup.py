# The Logrus
#
# Author: Joe Block <jpb@unixorn.net>
# License: Apache 2.0

from setuptools import setup, find_packages

name = "logrus"
version = "0.0.1"

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
