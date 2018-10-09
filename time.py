#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

ticks = time.time()

print ticks

localtime = time.localtime(ticks)

print localtime

localtime1 = time.asctime(localtime)

print localtime1

print localtime[0]
print localtime[1]
print localtime[2] 