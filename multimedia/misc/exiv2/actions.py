#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import autotools
from inary.actionsapi import inarytools
from inary.actionsapi import cmaketools
from inary.actionsapi import get

def setup():
    cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr  \
      -DCMAKE_BUILD_TYPE=Release   \
      -DEXIV2_ENABLE_VIDEO=yes     \
      -DEXIV2_ENABLE_WEBREADY=yes  \
      -DEXIV2_ENABLE_CURL=yes      \
      -DEXIV2_BUILD_SAMPLES=no     \
      -G \"Unix Makefiles\"")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    inarytools.dodoc("COPYING", "doc/ChangeLog")
