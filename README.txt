Linux watchdog device API for Python
====================================

    This distribution contains implementation of Linux watchdog device API for
    Python (see Documentation/watchdog/watchdog-api.txt in Linux kernel source
    tree).

    The built-in type included in extension module provides wrapper methods for
    ioctl commands as well as simple write access to the device.


Installation
============

    The module can be installed using standard setuptools script:

        python setup.py install

Usage
=====

    Make sure your watchdog driver is loaded and /dev/watchdog exists and is
    writeable.

    After that you should be able to import the module and open the watchdog
    device:

    >>> from watchdogapi import *
    >>> wdt = watchdog('/dev/watchdog')
    >>> wdt.get_support()
    >>> wdt.identity
    'Mediatek watchdog'
    ... 
    >>> 

