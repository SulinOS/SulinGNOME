#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from inary.actionsapi import autotools
from inary.actionsapi import inarytools

def setup():
    autotools.configure("--enable-lua --with-system-lua")

def build():
    autotools.make()

def install():
    autotools.install()
    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

    inarytools.remove("/usr/share/themes/*/index.theme")
    inarytools.remove("/usr/share/icons/*/index.theme")
