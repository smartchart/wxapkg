# -*- coding: utf-8 -*-

import os
import fnmatch
from unpack_wxapkg import wxapkg

if __name__ == '__main__':
    files = fnmatch.filter(os.listdir(), '*.wxapkg')
    for i in files:
        apk = wxapkg(i)
        apk.open_wxapkg()
