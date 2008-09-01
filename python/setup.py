#!/usr/bin/env python
import os
if os.path.isfile('../version'):
	myVersion = open('../version', 'r').readline().strip()

from distutils.core import setup
setup(
				name='THWAP',
				version=myVersion,
				py_modules=[
					'THWAP/__init__', 
					'THWAP/core/__init__', 
					'THWAP/core/config',
					'THWAP/core/connectionPools',
					'THWAP/core/jobQueues',
					'THWAP/core/threadPools',
					'THWAP/core/abstracts/__init__',
					'THWAP/core/abstracts/dbmAbstract',
					'THWAP/core/abstracts/networkAbstract',
					'THWAP/core/abstracts/threadAbstract',
					'THWAP/core/dbm/__init__',
					'THWAP/core/dbm/metaDbm',
					'THWAP/core/drivers/__init__',
					'THWAP/core/drivers/ftpDriver',
					'THWAP/core/drivers/httpDriver',
					'THWAP/core/drivers/mysqlDriver',
					'THWAP/core/drivers/pgsqlDriver',
					'THWAP/core/drivers/sqliteDriver',
					'THWAP/core/drivers/sshDriver',
					'THWAP/core/drivers/webdavDriver',
					'THWAP/monitor/__init__',
					'THWAP/monitor/mstat',
					'THWAP/monitor/plugins/__init__',
					'THWAP/os/__init__',
					'THWAP/os/daemon',
					'THWAP/os/display',
					'THWAP/os/bsd/__init__',
					'THWAP/os/bsd/dfly/__init__',
					'THWAP/os/bsd/free/__init__',
					'THWAP/os/bsd/net/__init__',
					'THWAP/os/bsd/open/__init__',
					'THWAP/os/linux/gentoo/__init__',
					'THWAP/os/linux/gentoo/glsa',
					'THWAP/os/linux/lvm/__init__',
					'THWAP/os/linux/lvm/excpt',
					'THWAP/os/linux/lvm/lvm',
					'THWAP/os/linux/lvm/meta',
					'THWAP/os/linux/lvm/parser',
			  ],
      )
