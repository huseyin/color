# color [![Build Status](https://drone.io/github.com/htaslan/color/status.png)](https://drone.io/github.com/htaslan/color/latest)

String Colorize Module for Python 3.x

Color chart

![chart](http://i.imgur.com/zGQ6f6z.png)

# Installation

```sh
$ pip install color
```

or

```sh
$ easy_install color
```

or make it

```sh
$ python setup.py install
```

# Usage

```py
# -*- coding: utf-8 -*-
#
# You use to specific functions
#
# from color import colorize
# from color import uncolorize

from color import *

# colorize function. set the other code.
print(colorize(38, 5, 197, 'foo bar baz'))

# uncolorize funciton
print(uncolorize(red('foo')))

# tr function.
print(tr('foo bar baz', 'o', FgColor.Red))      # colorized: 'o' chars.
print(tr('foo bar baz', 'foo', FgColor.Yellow)) # colorized: 'foo' words.

# tr_iter function.
print(tr_iter('foo bar baz', 'oa', FgColor.Green)) # colorized: all of 'o' and 'a' chars.

# cprint function.
cprint('hellooo', base=Base.Bold)
cprint('foo bar', fg=FgColor.Red, file=sys.stderr)
cprint('foo') # Stdout

# OTHERS
r = red('ops!')
g = green('hmmm...')
cprint(r, g)

cprint_yellow('yooo!!!')
cprint_green('success')
cprint_black('cocoa bitter')

# ...
```

# Credits

* [Hüseyin Tekinaslan](http://github.com/htaslan)

# License

The MIT License (MIT) - see [LICENSE](https://github.com/htaslan/python-colorize/blob/master/LICENSE) for more details
