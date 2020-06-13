"""drep

drep is the supporter for weekly reporting dlg community.


"""
from __future__ import print_function

import argparse
import logging
import os
import sys

from drep.dreplib import errors

__version__ = '0.0.1'

def main(argv):
    """Main program.

    Arguments:
        argv: command-line arguments, such as sys.argv (including the program name in argv[0]).
        
    Returns:
    Zero on successful program termination, non-zero otherwise.
    With --diff: zero if there were no changes, non-zero otherwise.
    """
    pass


def run_main():
  try:
    sys.exit(main(sys.argv))
  except errors.DrepError as e:
    sys.stderr.write('drep: ' + str(e) + '\n')
    sys.exit(1)


if __name__ == "__main__":
    run_main()