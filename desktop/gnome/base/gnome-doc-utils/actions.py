#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl-3.0.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import shelltools

def setup():
    shelltools.copy("tools/gnome-doc-utils.m4", "m4/")
    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    inarytools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "NEWS")
