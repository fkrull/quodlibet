# Copyright 2004 Joe Wreschnig
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation
#
# $Id$

# Simple proxy to a Python ConfigParser.

import os
from ConfigParser import SafeConfigParser as ConfigParser

_config = ConfigParser()
get = _config.get
set = _config.set
getboolean = _config.getboolean
getint = _config.getint
write = _config.write
options = _config.options

def init(rc_file):
    _config.add_section("settings")
    _config.add_section("memory")
    _config.add_section("header_maps")
    _config.set("settings", "scan", "")
    _config.set("settings", "gain", "2")

    _config.set("settings", "shuffle", "false")
    _config.set("settings", "repeat", "false")

    _config.set("settings", "jump", "true")
    _config.set("settings", "cover", "true")
    _config.set("settings", "color", "true")

    _config.set("settings", "tbp_space", "false")
    _config.set("settings", "addreplace", "0")
    _config.set("settings", "titlecase", "false")
    _config.set("settings", "splitval", "true")
    _config.set("settings", "nbp_space", "false")
    _config.set("settings", "windows", "true")
    _config.set("settings", "ascii", "false")

    _config.set("settings", "backend", "ao:alsa")
    _config.set("settings", "splitters", ",;&/")
    _config.set("settings", "headers", "=# title album artist")
    _config.set("memory", "size", "400 350")
    _config.set("memory", "song", "")
    _config.set("memory", "query", "")
    try: _config.read([rc_file])
    except: pass

def state(arg):
    return _config.getboolean("settings", arg)
