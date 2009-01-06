#!/usr/bin/env python

import setuptools
core_packages = setuptools.find_packages(exclude=('test','supergenpass*'))
main_packages = setuptools.find_packages(exclude=('test','sgpcore*'))

author='Tim Cuthbertson',
author_email='tim3d.junk+sgp@gmail.com',

if __name__ == '__main__':
	for k,v in globals().items():
		if k.startswith('_'):
			continue
		print "%s = %r" % (k,v)
