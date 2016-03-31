# -*- coding: utf-8 -*-

import sys
import re
from enum import Enum

# String colorize format.
COLORIZE_FORMAT = "\033[{:d};{:d};{:d}m{!s}\033[0m"
        
class FgColor(Enum):
    Black   = 30
    Red     = 31
    Green   = 32
    Yellow  = 33
    Blue    = 34
    Magenta = 35
    Cyan    = 36
    White   = 37
    Null    = 10

class BgColor(Enum):
    Black   = 40
    Red     = 41
    Green   = 42
    Yellow  = 43
    Blue    = 44
    Magenta = 45
    Cyan    = 46
    White   = 47
    Null    = 10

class Base(Enum):
    Reset        = 0
    Bold         = 1
    Faint        = 2
    Italic       = 3
    Underline    = 4
    BlinkSlow    = 5
    BlinkRapid   = 6
    ReverseVideo = 7
    Concealed    = 8
    CrossedOut   = 9
    Null         = 10


def _to_int(member):
    try:
        return member.value
    except:
        return member
        
    
def colorize(bg, base, fg, *text):
    """ colorize(bg, base, fg, *text)
    """
    # All argument types must be str. 
    rtext = [str(f) for f in text]
    
    return COLORIZE_FORMAT.format(
        _to_int(bg), _to_int(base), _to_int(fg), ''.join(rtext)
    )


def uncolorize(text):
    """ uncolorize(text)
    """
    match = re.match('^\033\[[0-9;]+m(.+?)\033\[0m', text)
    try:
        return match.groups()[0]
    except:
        return text


def tr(text, kword, color):
    """ tr(text, keyword, color)
    """
    return re.sub(kword, colorize(BgColor.Null, Base.Null, color, kword), text)


def tr_iter(text, kword, color):
    """ tr_iter(text, kword, color)
    """
    s=''
    for _t in text:
        if _t in kword:
            s += colorize(BgColor.Null, Base.Null, color, _t)
        else:
            s += _t
    return s


def cprint(*text, **kwargs):
    """ cprint(*text, **keywordargs)
    """
    print(
        colorize(
            kwargs.get('bg')   or BgColor.Null,
            kwargs.get('base') or Base.Null,
            kwargs.get('fg')   or FgColor.Null,
            *text
        ),
        file=kwargs.get('file') or sys.stdout
    )

def black(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Black, *text)

def red(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Red, *text)

def green(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Green, *text)

def yellow(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Yellow, *text)

def blue(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Blue, *text)

def magenta(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Magenta, *text)

def cyan(*text):
    return colorize(BgColor.Null, Base.Null, FgColor.Cyan, *text)

def cprint_black(*text):
    cprint(*text, fg=FgColor.Black)

def cprint_red(*text):
    cprint(*text, fg=FgColor.Red)

def cprint_green(*text):
    cprint(*text, fg=FgColor.Green)

def cprint_yellow(*text):
    cprint(*text, fg=FgColor.Yellow)

def cprint_blue(*text):
    cprint(*text, fg=FgColor.Blue)

def cprint_magenta(*text):
    cprint(*text, fg=FgColor.Magenta)

def cprint_cyan(*text):
    cprint(*text, fg=FgColor.Cyan)