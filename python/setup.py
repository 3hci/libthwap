#!/usr/bin/env python
from distutils.core import setup
setup(name='THWAP',
      version='0.2.3',
      py_modules=['thwap/__init__', 'thwap/dbm/__init__', 'thwap/dbm/mysql', 'thwap/system/__init__',
			      'thwap/system/daemon', 'thwap/system/display', 'thwap/system/logger', 'thwap/system/stdlib',
				  'thwap/utils/__init__', 'thwap/utils/config', 'thwap/utils/mslurp', 'thwap/utils/mstat', 'thwap/utils/pcrt',
				  'thwap/lvm/__init__','thwap/lvm/config','thwap/lvm/excpt','thwap/lvm/lvm','thwap/lvm/meta','thwap/lvm/parser',
			  ],
      )

