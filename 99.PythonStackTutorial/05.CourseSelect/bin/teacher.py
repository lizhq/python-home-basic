#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


path = os.path.join(BASEDIR, 'db', 'admin')
r = os.listdir(path)
print(r)
