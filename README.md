# logrus

[![GitHub stars](https://img.shields.io/github/stars/unixorn/logrus.svg)](https://github.com/unixorn/logrus/stargazers)
[![Code Climate](https://codeclimate.com/github/unixorn/logrus/badges/gpa.svg)](https://codeclimate.com/github/unixorn/logrus)
[![Issue Count](https://codeclimate.com/github/unixorn/logrus/badges/issue_count.svg)](https://codeclimate.com/github/unixorn/logrus)


The logrus is a collection of random utility functions. Nothing in here
is all that special, they're just yet another implementation of functions
I've rewritten at every job to use in various utility scripts. By open
sourcing them now, I'm hoping to not have to write them again.

# Installation

`pip install logrus`

# License

Everything in this repository is Apache 2.0 licensed.

# Included Commands

## human-time

Takes a value in seconds either from stdin or as arg 1 and converts it to a more meat-friendly format using the humanTime function.

`human-time 1234` will print "20 minutes, 34 seconds"

# Included functions

## logrus.cli

### findSubCommand(args)

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

Example usage:

```
def fooDriver():
  """
  Process the command line arguments and run the appropriate foo subcommand.

  We want to be able to do git-style handoffs to subcommands where if we
  do `foo blah foo bar` and the executable foo-blah-foo exists, we'll call
  it with the argument bar.

  We deliberately don't do anything with the arguments other than hand
  them off to the foo subcommand. Subcommands are responsible for their
  own argument parsing.
  """
  try:
    (command, args) = findSubCommand(sys.argv)

    # If we can't construct a subcommand from sys.argv, it'll still be able
    # to find this foo driver script, and re-running ourself isn't useful.
    if os.path.basename(command) == 'foo':
      print "Could not find a subcommand for %s" % ' '.join(sys.argv)
      sys.exit(1)
  except StandardError:
    print "Could not find a subcommand for %s" % ' '.join(sys.argv)
    sys.exit(1)
  check_call([command] + args)

```

### isProgram(name)

Search for a given program in `$PATH`, and return True if it exists and
is executable.

:param str name: Name of program to search for
:returns: whether or not the program can be found in $PATH
:rtype: bool

## logrus.time

### humanTime(seconds)

Takes a value in seconds, returns it in meat-friendly format. `humanFriendlyTime(8675309)` would return "100 days 9 hours 48 minutes 29 seconds".

## logrus.utils

### getCustomLogger(name, logLevel)

Returns a custom logger with nicely formatted output.

:param str name: What log level to set
:param str logLevel: What log level to use
:rtype: logger

### mkdir_p(path)

os module doesn't have a `mkdir -p` equivalent so added one.

### squashDicts(*dict_args)

Return a dict that is all the dict_args squashed together.
