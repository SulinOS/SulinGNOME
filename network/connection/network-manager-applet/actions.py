#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from inary.actionsapi import shelltools
from inary.actionsapi import inarytools
from inary.actionsapi import autotools
from inary.actionsapi import mesontools
from inary.actionsapi import get


def setup():
   # autotools.autoreconf("-vfi")
    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("meson --prefix=/usr     \
      --sysconfdir=/etc \
      -Dselinux=false   \
      -Dteam=false      \
      -Dmobile_broadband_provider_info=false \
      -Dgtk_doc=false .. ")

def build():
    shelltools.cd("build")
    shelltools.system("ninja")

def install():
    shelltools.makedirs(get.installDIR())
    shelltools.cd("build")
    shelltools.system("DESTDIR={} ninja install ".format(get.installDIR()))

