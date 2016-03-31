#!/usr/bin/env python
# -*- coding: utf-8 -*-

from color import *
from optparse import OptionParser

import sys


def _parse_args():
    parser = OptionParser(
        usage='colorize [options] <text>',
        description='Simple program for Python Colorize Library.',
        version='pycolorize 0.1'
    )
        
    parser.add_option(
        '-f', '--fg',
        dest='fgcolor',
        type='int',
        help='set foreground color',
        default=FgColor.White.value
    )
    
    parser.add_option(
        '-B', '--base',
        type='int',
        help='expand the other operations',
        default=Base.Null.value
    )
    
    parser.add_option(
        '-b', '--bg',
        dest='bgcolor',
        type='int',
        help='set backround color',
        default=BgColor.Null.value
    )
    
    (opts, args) = parser.parse_args()

    if not args:
        parser.print_help()
        sys.exit(1)
        
    return opts, args[0]
    

def _colorize(arg, fakedict):
    opts = fakedict.__dict__
    cprint(arg, fg=opts['fgcolor'], bg=opts['bgcolor'], base=opts['base'])
    
def main():
    (opts, arg) = _parse_args()
    _colorize(arg, opts)
    
if __name__ == '__main__':
    main()